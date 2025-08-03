import asyncio
import unittest
from unittest.mock import Mock
from tortrack.downloader import MusicDownloader
from tortrack.spotify import SpotifyService

class TestErrorHandling(unittest.TestCase):

    def test_downloader_invalid_input(self):
        """Test that the downloader handles invalid track info."""
        async def run_test():
            downloader = MusicDownloader()
            # Test with None
            result = await downloader.download_track(None)
            self.assertIsNone(result)
            # Test with empty dict
            result = await downloader.download_track({})
            self.assertIsNone(result)
            # Test with dict missing 'name'
            result = await downloader.download_track({'artist': 'Some Artist'})
            self.assertIsNone(result)
        asyncio.run(run_test())

    def test_spotify_invalid_url(self):
        """Test that the Spotify service handles invalid URLs."""
        async def run_test():
            # Mock the spotipy client so we don't need credentials
            spotify_service = SpotifyService()
            spotify_service.sp = Mock()

            # Test with a non-Spotify URL
            result = await spotify_service.get_track_info("https://example.com")
            self.assertIsNone(result)

            # Test with a malformed Spotify URL
            result = await spotify_service.get_track_info("https://open.spotify.com/invalid/url")
            self.assertIsNone(result)

            # Test with a completely invalid string
            result = await spotify_service.get_track_info("not a url")
            self.assertIsNone(result)

        asyncio.run(run_test())

if __name__ == "__main__":
    unittest.main()
