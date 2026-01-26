# Shared pytest fixtures for pyflix tests

import pytest
import tempfile
import os


@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir


@pytest.fixture
def mock_settings(monkeypatch):
    """Mock settings for testing."""
    class MockSettings:
        class Strategy:
            piece_st = 4
            last_piece_st = 4
            chunks_strat = 10
            always_sequential = False
        
        strategy = Strategy()
    
    def mock_get_settings():
        return MockSettings()
    
    monkeypatch.setattr('utils.helpers.get_settings', mock_get_settings)
    return MockSettings()


@pytest.fixture
def sample_video_file(temp_dir):
    """Create a mock video file for testing."""
    video_path = os.path.join(temp_dir, "test_video.mp4")
    # Create a minimal file (not a real MP4, just for path testing)
    with open(video_path, 'wb') as f:
        f.write(b'\x00' * 1024)
    return video_path
