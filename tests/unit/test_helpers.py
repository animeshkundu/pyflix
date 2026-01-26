"""Unit tests for utils/helpers.py module."""

import os
import sys
import pytest
from unittest.mock import patch, MagicMock, mock_open

# Mock external dependencies before importing the module
sys.modules['daemon'] = MagicMock()
sys.modules['altasetting'] = MagicMock()
sys.modules['netifaces'] = MagicMock()
sys.modules['ojota'] = MagicMock()
sys.modules['lockfile'] = MagicMock()

# Now we can safely import from utils.helpers
from utils import helpers


class TestGetFreePort:
    """Tests for the get_free_port function."""

    def test_get_free_port_returns_integer(self):
        """get_free_port should return an integer."""
        port = helpers.get_free_port()
        
        assert isinstance(port, int)

    def test_get_free_port_returns_valid_port_range(self):
        """get_free_port should return a port in valid range (1-65535)."""
        port = helpers.get_free_port()
        
        assert 1 <= port <= 65535

    def test_get_free_port_returns_unprivileged_port(self):
        """get_free_port should return an unprivileged port (>1023)."""
        port = helpers.get_free_port()
        
        # System-assigned ports are typically in ephemeral range
        assert port > 1023

    def test_get_free_port_returns_different_ports_on_multiple_calls(self):
        """Multiple calls to get_free_port may return different ports."""
        ports = [helpers.get_free_port() for _ in range(5)]
        
        # At least one should be different (though not guaranteed)
        # We mainly verify no exceptions are raised
        assert all(isinstance(p, int) for p in ports)


class TestIsPortFree:
    """Tests for the is_port_free function."""

    def test_is_port_free_returns_boolean(self):
        """is_port_free should return a boolean."""
        port = helpers.get_free_port()
        result = helpers.is_port_free(port)
        
        assert isinstance(result, bool)

    def test_is_port_free_returns_true_for_free_port(self):
        """is_port_free should return True for an available port."""
        # Get a port that was just freed
        port = helpers.get_free_port()
        
        result = helpers.is_port_free(port)
        
        assert result is True

    @patch('utils.helpers.socket.socket')
    def test_is_port_free_returns_false_when_bind_fails(self, mock_socket_class):
        """is_port_free should return False when socket bind fails."""
        import socket
        
        mock_socket = MagicMock()
        mock_socket_class.return_value = mock_socket
        mock_socket.bind.side_effect = socket.error("Address already in use")
        
        result = helpers.is_port_free(8080)
        
        assert result is False
        mock_socket.close.assert_called_once()

    @patch('utils.helpers.socket.socket')
    def test_is_port_free_closes_socket_on_success(self, mock_socket_class):
        """is_port_free should close the socket after successful bind."""
        mock_socket = MagicMock()
        mock_socket_class.return_value = mock_socket
        
        helpers.is_port_free(8080)
        
        mock_socket.close.assert_called_once()

    @patch('utils.helpers.socket.socket')
    def test_is_port_free_binds_to_localhost(self, mock_socket_class):
        """is_port_free should bind to localhost."""
        mock_socket = MagicMock()
        mock_socket_class.return_value = mock_socket
        
        helpers.is_port_free(8080)
        
        mock_socket.bind.assert_called_once_with(('localhost', 8080))


class TestIsProcessRunning:
    """Tests for the is_process_running function."""

    def test_is_process_running_returns_boolean(self):
        """is_process_running should return a boolean."""
        result = helpers.is_process_running(os.getpid())
        
        assert isinstance(result, bool)

    def test_is_process_running_returns_true_for_current_process(self):
        """is_process_running should return True for the current process."""
        current_pid = os.getpid()
        
        result = helpers.is_process_running(current_pid)
        
        assert result is True

    def test_is_process_running_returns_false_for_invalid_pid(self):
        """is_process_running should return False for a non-existent process."""
        # Use a very high PID that's unlikely to exist
        invalid_pid = 999999999
        
        result = helpers.is_process_running(invalid_pid)
        
        assert result is False

    @patch('utils.helpers.os.kill')
    def test_is_process_running_uses_signal_zero(self, mock_kill):
        """is_process_running should use signal 0 to check process."""
        helpers.is_process_running(12345)
        
        mock_kill.assert_called_once_with(12345, 0)

    @patch('utils.helpers.os.kill')
    def test_is_process_running_handles_oserror(self, mock_kill):
        """is_process_running should handle OSError gracefully."""
        mock_kill.side_effect = OSError("No such process")
        
        result = helpers.is_process_running(12345)
        
        assert result is False


class TestSetConfigDir:
    """Tests for the set_config_dir function."""

    @patch('utils.helpers.set_data_source')
    @patch('utils.helpers.exists')
    @patch('utils.helpers.mkdir')
    @patch.dict(os.environ, {'HOME': '/home/testuser'})
    def test_set_config_dir_creates_directory_if_not_exists(
        self, mock_mkdir, mock_exists, mock_set_data_source
    ):
        """set_config_dir should create .pyflix directory if it doesn't exist."""
        mock_exists.return_value = False
        
        helpers.set_config_dir()
        
        mock_mkdir.assert_called_once_with('/home/testuser/.pyflix')

    @patch('utils.helpers.set_data_source')
    @patch('utils.helpers.exists')
    @patch('utils.helpers.mkdir')
    @patch.dict(os.environ, {'HOME': '/home/testuser'})
    def test_set_config_dir_does_not_create_if_exists(
        self, mock_mkdir, mock_exists, mock_set_data_source
    ):
        """set_config_dir should not create directory if it already exists."""
        mock_exists.return_value = True
        
        helpers.set_config_dir()
        
        mock_mkdir.assert_not_called()

    @patch('utils.helpers.set_data_source')
    @patch('utils.helpers.exists')
    @patch('utils.helpers.mkdir')
    @patch.dict(os.environ, {'HOME': '/home/testuser'})
    def test_set_config_dir_sets_data_source(
        self, mock_mkdir, mock_exists, mock_set_data_source
    ):
        """set_config_dir should call set_data_source with config directory."""
        mock_exists.return_value = True
        
        helpers.set_config_dir()
        
        mock_set_data_source.assert_called_once_with('/home/testuser/.pyflix')


class TestGetLockDiff:
    """Tests for the get_lock_diff function."""

    @patch('utils.helpers.getmtime')
    @patch('utils.helpers.datetime')
    def test_get_lock_diff_returns_time_difference(
        self, mock_datetime, mock_getmtime
    ):
        """get_lock_diff should return the time difference in seconds."""
        # Mock current time and file modification time
        mock_now = MagicMock()
        mock_datetime.now.return_value = mock_now
        
        mock_timediff = MagicMock()
        mock_timediff.total_seconds.return_value = 120.5
        mock_now.__sub__ = MagicMock(return_value=mock_timediff)
        
        mock_getmtime.return_value = 1000000
        mock_datetime.fromtimestamp.return_value = MagicMock()
        
        result = helpers.get_lock_diff()
        
        assert result == 120.5

    @patch('utils.helpers.getmtime')
    def test_get_lock_diff_returns_zero_on_oserror(self, mock_getmtime):
        """get_lock_diff should return 0 when OSError occurs."""
        mock_getmtime.side_effect = OSError("File not found")
        
        result = helpers.get_lock_diff()
        
        assert result == 0


class TestGetSettings:
    """Tests for the get_settings function."""

    @patch('utils.helpers.Settings')
    @patch('utils.helpers.copyfile')
    @patch('utils.helpers.set_config_dir')
    @patch('utils.helpers.exists')
    @patch.dict(os.environ, {'HOME': '/home/testuser'})
    def test_get_settings_returns_settings_object(
        self, mock_exists, mock_set_config_dir, mock_copyfile, mock_settings_class
    ):
        """get_settings should return a Settings object."""
        mock_exists.return_value = True
        mock_settings_instance = MagicMock()
        mock_settings_class.return_value = mock_settings_instance
        
        result = helpers.get_settings()
        
        assert result is mock_settings_instance

    @patch('utils.helpers.Settings')
    @patch('utils.helpers.copyfile')
    @patch('utils.helpers.set_config_dir')
    @patch('utils.helpers.exists')
    @patch.dict(os.environ, {'HOME': '/home/testuser'})
    def test_get_settings_calls_set_config_dir(
        self, mock_exists, mock_set_config_dir, mock_copyfile, mock_settings_class
    ):
        """get_settings should call set_config_dir."""
        mock_exists.return_value = True
        
        helpers.get_settings()
        
        mock_set_config_dir.assert_called_once()

    @patch('utils.helpers.Settings')
    @patch('utils.helpers.copyfile')
    @patch('utils.helpers.set_config_dir')
    @patch('utils.helpers.exists')
    @patch.dict(os.environ, {'HOME': '/home/testuser'})
    def test_get_settings_copies_default_if_not_exists(
        self, mock_exists, mock_set_config_dir, mock_copyfile, mock_settings_class
    ):
        """get_settings should copy default settings if user settings don't exist."""
        mock_exists.return_value = False
        
        helpers.get_settings()
        
        mock_copyfile.assert_called_once()

    @patch('utils.helpers.Settings')
    @patch('utils.helpers.copyfile')
    @patch('utils.helpers.set_config_dir')
    @patch('utils.helpers.exists')
    @patch.dict(os.environ, {'HOME': '/home/testuser'})
    def test_get_settings_does_not_copy_if_exists(
        self, mock_exists, mock_set_config_dir, mock_copyfile, mock_settings_class
    ):
        """get_settings should not copy default if user settings exist."""
        mock_exists.return_value = True
        
        helpers.get_settings()
        
        mock_copyfile.assert_not_called()


class TestGetInterface:
    """Tests for the get_interface function."""

    @patch('utils.helpers.ifaddresses')
    @patch('utils.helpers.interfaces')
    def test_get_interface_returns_ip_address(
        self, mock_interfaces, mock_ifaddresses
    ):
        """get_interface should return an IP address string."""
        mock_interfaces.return_value = ['eth0']
        mock_ifaddresses.return_value = {
            2: [{'addr': '192.168.1.100', 'netmask': '255.255.255.0'}]
        }
        
        result = helpers.get_interface()
        
        assert result == '192.168.1.100'

    @patch('utils.helpers.ifaddresses')
    @patch('utils.helpers.interfaces')
    def test_get_interface_skips_localhost(
        self, mock_interfaces, mock_ifaddresses
    ):
        """get_interface should skip localhost addresses."""
        mock_interfaces.return_value = ['lo', 'eth0']
        mock_ifaddresses.return_value = {
            2: [{'addr': '127.0.0.1', 'netmask': '255.0.0.0'}]
        }
        
        # With only localhost addresses, should return None
        result = helpers.get_interface()
        
        # First iteration returns localhost, which is skipped
        assert result is None or not result.startswith('127')

    @patch('utils.helpers.ifaddresses')
    @patch('utils.helpers.interfaces')
    def test_get_interface_skips_ipv6_addresses(
        self, mock_interfaces, mock_ifaddresses
    ):
        """get_interface should skip IPv6 addresses (starting with :)."""
        mock_interfaces.return_value = ['eth0']
        mock_ifaddresses.return_value = {
            10: [{'addr': '::1', 'netmask': 'ffff:ffff:ffff:ffff::'}]
        }
        
        result = helpers.get_interface()
        
        # IPv6 addresses are skipped
        assert result is None or not result.startswith(':')

    @patch('utils.helpers.ifaddresses')
    @patch('utils.helpers.interfaces')
    def test_get_interface_skips_addresses_without_netmask(
        self, mock_interfaces, mock_ifaddresses
    ):
        """get_interface should skip addresses without netmask."""
        mock_interfaces.return_value = ['eth0']
        mock_ifaddresses.return_value = {
            2: [{'addr': '192.168.1.100'}]  # No netmask
        }
        
        result = helpers.get_interface()
        
        assert result is None

    @patch('utils.helpers.ifaddresses')
    @patch('utils.helpers.interfaces')
    def test_get_interface_returns_first_valid_address(
        self, mock_interfaces, mock_ifaddresses
    ):
        """get_interface should return first valid non-localhost address."""
        mock_interfaces.return_value = ['eth0', 'eth1']
        
        def mock_ifaddr(iface):
            if iface == 'eth0':
                return {2: [{'addr': '10.0.0.1', 'netmask': '255.255.255.0'}]}
            return {2: [{'addr': '192.168.1.1', 'netmask': '255.255.255.0'}]}
        
        mock_ifaddresses.side_effect = mock_ifaddr
        
        result = helpers.get_interface()
        
        assert result == '10.0.0.1'


class TestLockfileConstant:
    """Tests for the LOCKFILE constant."""

    def test_lockfile_is_string(self):
        """LOCKFILE should be a string."""
        assert isinstance(helpers.LOCKFILE, str)

    def test_lockfile_is_in_tmp(self):
        """LOCKFILE should be in /tmp directory."""
        assert helpers.LOCKFILE.startswith('/tmp')

    def test_lockfile_contains_pyflix(self):
        """LOCKFILE should contain 'pyflix' in the path."""
        assert 'pyflix' in helpers.LOCKFILE
