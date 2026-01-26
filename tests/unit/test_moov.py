"""Unit tests for torrent/moov.py module."""

import sys
import pytest
from unittest.mock import patch, mock_open, MagicMock

# Mock external dependencies before importing the module
sys.modules['qtfaststart'] = MagicMock()
sys.modules['qtfaststart.processor'] = MagicMock()
sys.modules['qtfaststart.exceptions'] = MagicMock()

# Create a proper exception class for FastStartException
class MockFastStartException(Exception):
    pass

sys.modules['qtfaststart.exceptions'].FastStartException = MockFastStartException

# Mock internal dependencies that have issues
sys.modules['Pyflix'] = MagicMock()
sys.modules['Pyflix.utils'] = MagicMock()
sys.modules['Pyflix.utils.settings'] = MagicMock()
sys.modules['Pyflix.utils.settings'].SKIP_MOOV = True

# Mock thread module (Python 2 compatibility issue in torrent/__init__.py)
sys.modules['thread'] = MagicMock()

# Now import the module under test directly (not via torrent package)
import importlib.util
spec = importlib.util.spec_from_file_location("moov", "torrent/moov.py")
moov = importlib.util.module_from_spec(spec)
sys.modules['torrent.moov'] = moov
spec.loader.exec_module(moov)


class TestHaveMoov:
    """Tests for the have_moov function."""

    @patch.object(moov, 'SKIP_MOOV', True)
    def test_have_moov_returns_true_when_skip_moov_enabled(self):
        """When SKIP_MOOV is True, should return True without processing."""
        result = moov.have_moov("any_file.mp4")
        
        assert result is True

    @patch.object(moov, 'SKIP_MOOV', False)
    @patch.object(moov, 'get_index')
    @patch('builtins.open', new_callable=mock_open, read_data=b'fake video data')
    def test_have_moov_returns_true_when_moov_before_mdat(
        self, mock_file, mock_get_index
    ):
        """When moov atom is before mdat, should return True."""
        # Create mock atoms where moov (100) < mdat (200)
        mock_atom_moov = MagicMock()
        mock_atom_moov.name = 'moov'
        mock_atom_moov.position = 100
        
        mock_atom_mdat = MagicMock()
        mock_atom_mdat.name = 'mdat'
        mock_atom_mdat.position = 200
        
        mock_atom_ftyp = MagicMock()
        mock_atom_ftyp.name = 'ftyp'
        mock_atom_ftyp.position = 0
        
        mock_atom_free = MagicMock()
        mock_atom_free.name = 'free'
        mock_atom_free.position = 50
        
        mock_get_index.return_value = [
            mock_atom_ftyp, mock_atom_free, mock_atom_moov, mock_atom_mdat
        ]
        
        result = moov.have_moov("test_video.mp4")
        
        assert result is True
        mock_file.assert_called_once_with("test_video.mp4", 'rb')
        mock_get_index.assert_called_once()

    @patch.object(moov, 'SKIP_MOOV', False)
    @patch.object(moov, 'get_index')
    @patch('builtins.open', new_callable=mock_open, read_data=b'fake video data')
    def test_have_moov_returns_tuple_when_moov_after_mdat(
        self, mock_file, mock_get_index
    ):
        """When moov atom is after mdat, should return (True, 'after_mdat')."""
        # Create mock atoms where moov (300) > mdat (200)
        mock_atom_moov = MagicMock()
        mock_atom_moov.name = 'moov'
        mock_atom_moov.position = 300
        
        mock_atom_mdat = MagicMock()
        mock_atom_mdat.name = 'mdat'
        mock_atom_mdat.position = 200
        
        mock_atom_ftyp = MagicMock()
        mock_atom_ftyp.name = 'ftyp'
        mock_atom_ftyp.position = 0
        
        mock_atom_free = MagicMock()
        mock_atom_free.name = 'free'
        mock_atom_free.position = 50
        
        mock_get_index.return_value = [
            mock_atom_ftyp, mock_atom_free, mock_atom_mdat, mock_atom_moov
        ]
        
        result = moov.have_moov("test_video.mp4")
        
        assert result == (True, "after_mdat")

    @patch.object(moov, 'SKIP_MOOV', False)
    @patch.object(moov, 'get_index')
    @patch('builtins.open', new_callable=mock_open, read_data=b'fake video data')
    def test_have_moov_returns_false_on_faststart_exception(
        self, mock_file, mock_get_index
    ):
        """When FastStartException occurs, should return False."""
        mock_get_index.side_effect = moov.FastStartException("Invalid file format")
        
        result = moov.have_moov("invalid_video.mp4")
        
        assert result is False

    @patch.object(moov, 'SKIP_MOOV', False)
    @patch.object(moov, 'get_index')
    @patch('builtins.open', new_callable=mock_open, read_data=b'fake video data')
    def test_have_moov_logs_info_message(self, mock_file, mock_get_index, caplog):
        """Should log info message when checking moov data."""
        import logging
        
        mock_atom_moov = MagicMock()
        mock_atom_moov.name = 'moov'
        mock_atom_moov.position = 100
        
        mock_atom_mdat = MagicMock()
        mock_atom_mdat.name = 'mdat'
        mock_atom_mdat.position = 200
        
        mock_atom_ftyp = MagicMock()
        mock_atom_ftyp.name = 'ftyp'
        mock_atom_ftyp.position = 0
        
        mock_atom_free = MagicMock()
        mock_atom_free.name = 'free'
        mock_atom_free.position = 50
        
        mock_get_index.return_value = [
            mock_atom_ftyp, mock_atom_free, mock_atom_moov, mock_atom_mdat
        ]
        
        with caplog.at_level(logging.INFO):
            moov.have_moov("test_video.mp4")
        
        assert "Checking moov data of test_video.mp4" in caplog.text

    @patch.object(moov, 'SKIP_MOOV', False)
    @patch.object(moov, 'get_index')
    @patch('builtins.open', new_callable=mock_open, read_data=b'fake video data')
    def test_have_moov_logs_error_on_exception(
        self, mock_file, mock_get_index, caplog
    ):
        """Should log error message when FastStartException occurs."""
        import logging
        
        mock_get_index.side_effect = moov.FastStartException("Corrupted file")
        
        with caplog.at_level(logging.ERROR):
            moov.have_moov("corrupted.mp4")
        
        assert "Couldn't get Atoms data" in caplog.text
        assert "Corrupted file" in caplog.text

    @patch.object(moov, 'SKIP_MOOV', False)
    @patch.object(moov, 'get_index')
    @patch('builtins.open', new_callable=mock_open, read_data=b'fake video data')
    def test_have_moov_opens_file_in_binary_read_mode(
        self, mock_file, mock_get_index
    ):
        """Should open the video file in binary read mode."""
        mock_atom_moov = MagicMock()
        mock_atom_moov.name = 'moov'
        mock_atom_moov.position = 100
        
        mock_atom_mdat = MagicMock()
        mock_atom_mdat.name = 'mdat'
        mock_atom_mdat.position = 200
        
        mock_atom_ftyp = MagicMock()
        mock_atom_ftyp.name = 'ftyp'
        mock_atom_ftyp.position = 0
        
        mock_atom_free = MagicMock()
        mock_atom_free.name = 'free'
        mock_atom_free.position = 50
        
        mock_get_index.return_value = [
            mock_atom_ftyp, mock_atom_free, mock_atom_moov, mock_atom_mdat
        ]
        
        moov.have_moov("/path/to/video.mp4")
        
        mock_file.assert_called_once_with("/path/to/video.mp4", 'rb')

    @patch.object(moov, 'SKIP_MOOV', False)
    @patch.object(moov, 'get_index')
    @patch('builtins.open', new_callable=mock_open, read_data=b'fake video data')
    def test_have_moov_handles_equal_positions(self, mock_file, mock_get_index):
        """When moov and mdat have equal positions, should return True (not tuple)."""
        # Edge case: equal positions (moov not > mdat)
        mock_atom_moov = MagicMock()
        mock_atom_moov.name = 'moov'
        mock_atom_moov.position = 200
        
        mock_atom_mdat = MagicMock()
        mock_atom_mdat.name = 'mdat'
        mock_atom_mdat.position = 200
        
        mock_atom_ftyp = MagicMock()
        mock_atom_ftyp.name = 'ftyp'
        mock_atom_ftyp.position = 0
        
        mock_atom_free = MagicMock()
        mock_atom_free.name = 'free'
        mock_atom_free.position = 50
        
        mock_get_index.return_value = [
            mock_atom_ftyp, mock_atom_free, mock_atom_moov, mock_atom_mdat
        ]
        
        result = moov.have_moov("test_video.mp4")
        
        assert result is True
