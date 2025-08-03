import pytest
from tortrack.bot import TelegramBot
from tortrack.database import Database
from tortrack.spotify import SpotifyService

@pytest.fixture
def bot():
    """Provides a default bot instance with Tor disabled."""
    return TelegramBot(token="12345:dummy_token", use_tor=False)

def test_bot_instantiation(bot):
    """Test that the TelegramBot class can be instantiated correctly."""
    assert bot.token == "12345:dummy_token"
    assert bot.use_tor is False
    assert bot.bot is None
    assert bot.dp is None

@pytest.mark.asyncio
async def test_database_connection_failure():
    """Test that the Database class handles connection failures gracefully."""
    # Using a porta that is unlikely to be open
    db = Database(mongo_uri="mongodb://localhost:9999/test")
    await db.init()
    assert db.db is None, "Database object should be None after a connection failure."

@pytest.mark.asyncio
async def test_spotify_service_no_credentials():
    """Test that the SpotifyService handles missing credentials gracefully."""
    spotify_service = SpotifyService()
    assert spotify_service.sp is None, "Spotify client should be None without credentials."

    # Test that calling a method doesn't crash and returns the expected None
    track_info = await spotify_service.get_track_info("https://open.spotify.com/track/dummy")
    assert track_info is None

@pytest.mark.asyncio
async def test_bot_setup_runs_without_errors(bot):
    """Test that the bot's main setup function runs without raising exceptions."""
    try:
        await bot.setup()
        # Ensure cleanup is also tested
        await bot.cleanup()
    except Exception as e:
        pytest.fail(f"bot.setup() raised an unexpected exception: {e}")
