"""Unit tests for utils/output.py module."""

import pytest
from unittest.mock import patch, MagicMock


class TestOutput:
    """Tests for the Output base class."""

    def test_output_init_stores_stream_url(self):
        """Output should store the stream URL on initialization."""
        from utils.output import Output
        
        stream_url = "http://localhost:8080/stream.mp4"
        parent = MagicMock()
        
        output = Output(stream_url, parent)
        
        assert output.stream_url == stream_url

    def test_output_init_stores_parent(self):
        """Output should store the parent reference on initialization."""
        from utils.output import Output
        
        stream_url = "http://localhost:8080/stream.mp4"
        parent = MagicMock()
        
        output = Output(stream_url, parent)
        
        assert output.parent is parent

    @patch('utils.output.system')
    def test_output_run_calls_system_with_command(self, mock_system):
        """Output.run() should call system with the player command."""
        from utils.output import Output
        
        stream_url = "http://localhost:8080/stream.mp4"
        parent = MagicMock()
        output = Output(stream_url, parent)
        
        output.run()
        
        mock_system.assert_called_once()

    @patch('utils.output.system')
    def test_output_run_uses_empty_player_command(self, mock_system):
        """Base Output class should have empty player command."""
        from utils.output import Output
        
        stream_url = "http://localhost:8080/stream.mp4"
        parent = MagicMock()
        output = Output(stream_url, parent)
        
        output.run()
        
        # Base class returns empty string from _player()
        mock_system.assert_called_once_with(" ")

    def test_output_player_returns_empty_string(self):
        """Base Output._player() should return empty string."""
        from utils.output import Output
        
        stream_url = "http://localhost:8080/stream.mp4"
        parent = MagicMock()
        output = Output(stream_url, parent)
        
        result = output._player()
        
        assert result == ""

    @patch('utils.output.system')
    def test_output_run_logs_debug_message(self, mock_system, caplog):
        """Output.run() should log the command at debug level."""
        from utils.output import Output
        import logging
        
        stream_url = "http://localhost:8080/stream.mp4"
        parent = MagicMock()
        output = Output(stream_url, parent)
        
        with caplog.at_level(logging.DEBUG):
            output.run()
        
        assert "VLC command" in caplog.text


class TestVLCOutput:
    """Tests for the VLCOutput class."""

    def test_vlcoutput_inherits_from_output(self):
        """VLCOutput should inherit from Output."""
        from utils.output import VLCOutput, Output
        
        assert issubclass(VLCOutput, Output)

    def test_vlcoutput_init_stores_stream_url(self):
        """VLCOutput should store the stream URL on initialization."""
        from utils.output import VLCOutput
        
        stream_url = "http://localhost:8080/stream.mp4"
        parent = MagicMock()
        
        output = VLCOutput(stream_url, parent)
        
        assert output.stream_url == stream_url

    def test_vlcoutput_init_stores_parent(self):
        """VLCOutput should store the parent reference on initialization."""
        from utils.output import VLCOutput
        
        stream_url = "http://localhost:8080/stream.mp4"
        parent = MagicMock()
        
        output = VLCOutput(stream_url, parent)
        
        assert output.parent is parent

    def test_vlcoutput_player_returns_vlc_command(self):
        """VLCOutput._player() should return VLC command with stream URL."""
        from utils.output import VLCOutput
        
        stream_url = "http://localhost:8080/stream.mp4"
        parent = MagicMock()
        output = VLCOutput(stream_url, parent)
        
        result = output._player()
        
        assert result == "vlc http://localhost:8080/stream.mp4 -q"

    def test_vlcoutput_player_includes_quiet_flag(self):
        """VLCOutput._player() should include the -q (quiet) flag."""
        from utils.output import VLCOutput
        
        stream_url = "http://localhost:8080/stream.mp4"
        parent = MagicMock()
        output = VLCOutput(stream_url, parent)
        
        result = output._player()
        
        assert "-q" in result

    def test_vlcoutput_player_starts_with_vlc(self):
        """VLCOutput._player() command should start with 'vlc'."""
        from utils.output import VLCOutput
        
        stream_url = "http://localhost:8080/stream.mp4"
        parent = MagicMock()
        output = VLCOutput(stream_url, parent)
        
        result = output._player()
        
        assert result.startswith("vlc ")

    @patch('utils.output.system')
    def test_vlcoutput_run_calls_system_with_vlc_command(self, mock_system):
        """VLCOutput.run() should call system with VLC command."""
        from utils.output import VLCOutput
        
        stream_url = "http://localhost:8080/stream.mp4"
        parent = MagicMock()
        output = VLCOutput(stream_url, parent)
        
        output.run()
        
        mock_system.assert_called_once()
        call_args = mock_system.call_args[0][0]
        assert "vlc" in call_args
        assert stream_url in call_args

    def test_vlcoutput_player_handles_url_with_special_characters(self):
        """VLCOutput._player() should handle URLs with special characters."""
        from utils.output import VLCOutput
        
        stream_url = "http://localhost:8080/stream.mp4?token=abc&id=123"
        parent = MagicMock()
        output = VLCOutput(stream_url, parent)
        
        result = output._player()
        
        assert stream_url in result

    def test_vlcoutput_player_handles_empty_url(self):
        """VLCOutput._player() should handle empty URL."""
        from utils.output import VLCOutput
        
        stream_url = ""
        parent = MagicMock()
        output = VLCOutput(stream_url, parent)
        
        result = output._player()
        
        assert result == "vlc  -q"

    def test_vlcoutput_player_handles_url_with_spaces(self):
        """VLCOutput._player() should include URL even with spaces."""
        from utils.output import VLCOutput
        
        stream_url = "http://localhost:8080/my video.mp4"
        parent = MagicMock()
        output = VLCOutput(stream_url, parent)
        
        result = output._player()
        
        assert stream_url in result


class TestOutputIntegration:
    """Integration tests for Output classes."""

    @patch('utils.output.system')
    def test_vlcoutput_full_workflow(self, mock_system):
        """Test complete VLCOutput workflow from init to run."""
        from utils.output import VLCOutput
        
        stream_url = "http://192.168.1.100:1149/video.mp4"
        parent = MagicMock()
        parent.name = "test_parent"
        
        output = VLCOutput(stream_url, parent)
        
        # Verify initialization
        assert output.stream_url == stream_url
        assert output.parent is parent
        
        # Run the output
        output.run()
        
        # Verify system was called with correct command
        mock_system.assert_called_once()
        command = mock_system.call_args[0][0]
        assert "vlc" in command
        assert stream_url in command
        assert "-q" in command

    def test_output_classes_accept_none_parent(self):
        """Output classes should accept None as parent."""
        from utils.output import Output, VLCOutput
        
        stream_url = "http://localhost:8080/stream.mp4"
        
        output = Output(stream_url, None)
        vlc_output = VLCOutput(stream_url, None)
        
        assert output.parent is None
        assert vlc_output.parent is None
