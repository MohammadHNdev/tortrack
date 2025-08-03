import asyncio
from tortrack.bot import TelegramBot
from tortrack.spotify import SpotifyService
from tortrack.database import Database
import logging

# Suppress aiogram's INFO logging to keep the output clean
logging.basicConfig(level=logging.WARNING)

async def main():
    print("--- Starting Limited Health Check ---")

    # 1. Test TelegramBot instantiation
    print("\n[1] Testing TelegramBot instantiation...")
    try:
        # Using a dummy token as we are not actually connecting to Telegram
        bot = TelegramBot(token="12345:dummy_token", use_tor=False)
        print("✅ TelegramBot instantiated successfully.")
    except Exception as e:
        print(f"❌ FAILED: Could not instantiate TelegramBot. Error: {e}")
        return

    # 2. Test graceful failure of Database connection
    print("\n[2] Testing Database connection failure...")
    try:
        # Using a non-existent MongoDB URI to test failure handling
        db = Database(mongo_uri="mongodb://localhost:9999/test")
        await db.init()
        # The `init` method should not raise an exception, only log a warning.
        if db.db is None:
            print("✅ Database connection failed gracefully as expected.")
        else:
            print("❌ FAILED: Database object was created with a bad URI.")
    except Exception as e:
        print(f"❌ FAILED: Database init raised an unexpected exception: {e}")

    # 3. Test graceful handling of missing Spotify credentials
    print("\n[3] Testing SpotifyService without credentials...")
    try:
        spotify_service = SpotifyService()
        if spotify_service.sp is None:
            print("✅ SpotifyService handled missing credentials gracefully.")
        else:
            print("❌ FAILED: Spotify client was created without credentials.")

        # Test that calling a method doesn't crash
        track_info = await spotify_service.get_track_info("https://open.spotify.com/track/dummy")
        if track_info is None:
            print("✅ `get_track_info` returned None as expected without a client.")
        else:
            print("❌ FAILED: `get_track_info` returned a value without a client.")

    except Exception as e:
        print(f"❌ FAILED: SpotifyService raised an unexpected exception: {e}")

    # 4. Test Bot Setup process (without running the polling)
    print("\n[4] Testing bot's internal setup process...")
    try:
        # We expect this to work without crashing, even with dummy credentials
        # and no DB, because we are not starting the polling.
        await bot.setup()
        print("✅ Bot setup() method completed without errors.")
        # Check that services are initialized (even if not connected)
        if bot.db is not None and bot.dp is not None:
             print("✅ Bot components (db, dp) are initialized.")
        else:
             print("❌ FAILED: Bot components were not initialized correctly.")
    except Exception as e:
        print(f"❌ FAILED: Bot setup raised an unexpected exception: {e}")
    finally:
        # Ensure cleanup is called
        await bot.cleanup()
        print("✅ Bot cleanup() method called.")


    print("\n--- Limited Health Check Complete ---")

if __name__ == "__main__":
    asyncio.run(main())
