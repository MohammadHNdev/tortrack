# 📚 API Reference

Complete documentation for TorTrack classes and methods.

## 🏗️ Core Classes

### TelegramBot

Main bot class - handles all bot operations.

```python
from tortrack import TelegramBot

bot = TelegramBot(
    token="YOUR_BOT_TOKEN",
    use_tor=True,
    mongo_uri="mongodb://localhost:27017/tortrack"
)
```

#### Constructor Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `token` | `str` | Required | Telegram bot token from @BotFather |
| `use_tor` | `bool` | `True` | Enable Tor anonymity |
| `mongo_uri` | `str` | `mongodb://localhost:27017/tortrack` | MongoDB connection URI |

#### Methods

##### `run()`
Start the bot and begin polling for messages.

```python
bot.run()  # Runs forever until stopped
```

**Returns**: None (blocks until stopped)

##### `send_message(chat_id, text)` (async)
Send a message to a specific chat (advanced usage).

```python
await bot.send_message(12345, "Hello!")
```

**Parameters**:
- `chat_id` (int): Target chat ID
- `text` (str): Message text

---

### TorManager

Handles Tor proxy configuration and management.

```python
from tortrack import TorManager

tor = TorManager(socks_port=9050, control_port=9051)
await tor.start()
```

#### Constructor Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `socks_port` | `int` | `9050` | Tor SOCKS5 proxy port |
| `control_port` | `int` | `9051` | Tor control port |

#### Methods

##### `start()` (async)
Start Tor service and establish connection.

```python
success = await tor.start()
```

**Returns**: `bool` - True if successful

##### `stop()` (async)
Stop Tor service.

```python
await tor.stop()
```

##### `get_session()`
Get requests session configured with Tor proxy.

```python
session = tor.get_session()
response = session.get("https://httpbin.org/ip")
```

**Returns**: `requests.Session` object

##### `rotate_identity()` (async)
Get new Tor identity (new IP).

```python
await tor.rotate_identity()
```

##### `get_current_ip()`
Get current external IP address.

```python
ip = tor.get_current_ip()
print(f"Current IP: {ip}")
```

**Returns**: `str` - Current IP address

---

## 🎵 Internal Services

These classes are used internally but can be accessed for advanced usage.

### SpotifyService

Handles Spotify API integration.

```python
from tortrack.spotify import SpotifyService

spotify = SpotifyService(tor_manager=tor_manager)
```

#### Methods

##### `get_track_info(spotify_url)` (async)
Extract track information from Spotify URL.

```python
info = await spotify.get_track_info("https://open.spotify.com/track/...")
```

**Returns**: `dict` or `list` - Track information

**Track dict structure**:
```python
{
    "id": "spotify_track_id",
    "name": "Song Title",
    "artist": "Artist Name", 
    "album": "Album Name",
    "duration_ms": 180000,
    "cover_url": "https://...",
    "spotify_url": "https://open.spotify.com/track/..."
}
```

---

### MusicDownloader

Handles music downloading from various sources.

```python
from tortrack.downloader import MusicDownloader

downloader = MusicDownloader(tor_manager=tor_manager)
```

#### Methods

##### `download_track(track_info)` (async)
Download track and return file path.

```python
file_path = await downloader.download_track(track_info)
```

**Parameters**:
- `track_info` (dict): Track info from SpotifyService

**Returns**: `str` or `None` - Path to downloaded file

##### `cleanup_file(file_path)`
Clean up downloaded file.

```python
downloader.cleanup_file("/path/to/file.mp3")
```

---

### Database

Handles user management and archiving.

```python
from tortrack.database import Database

db = Database("mongodb://localhost:27017/tortrack")
await db.init()
```

#### Methods

##### `get_user_downloads_today(user_id)` (async)
Get user's download count for today.

```python
count = await db.get_user_downloads_today(123456)
```

**Returns**: `int` - Number of downloads today

##### `increment_user_downloads(user_id)` (async)
Increment user's download count.

```python
await db.increment_user_downloads(123456)
```

##### `is_vip_user(user_id)` (async)
Check if user has VIP status.

```python
is_vip = await db.is_vip_user(123456)
```

**Returns**: `bool` - True if user is VIP

##### `is_track_archived(spotify_id)` (async)
Check if track is already downloaded.

```python
file_id = await db.is_track_archived("spotify_track_id")
```

**Returns**: `str` or `None` - Telegram file ID if archived

##### `archive_track(spotify_id, file_id, track_info)` (async)
Save track to archive.

```python
await db.archive_track("spotify_id", "telegram_file_id", track_info)
```

---

## 🔧 Configuration

### Environment Variables

TorTrack reads these environment variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `SPOTIFY_CLIENT_ID` | Spotify API client ID | `abc123def456` |
| `SPOTIFY_CLIENT_SECRET` | Spotify API client secret | `xyz789uvw012` |
| `BOT_TOKEN` | Telegram bot token | `123456789:ABC...` |
| `MONGO_URI` | MongoDB connection URI | `mongodb://localhost:27017/tortrack` |
| `TOR_SOCKS_PORT` | Tor SOCKS proxy port | `9050` |
| `TOR_CONTROL_PORT` | Tor control port | `9051` |

### Settings Constants

```python
# Daily download limits
DAILY_LIMIT = 5  # Free users
VIP_DAILY_LIMIT = 100  # VIP users (unlimited in practice)

# Download quality
AUDIO_QUALITY = "192"  # kbps
AUDIO_FORMAT = "mp3"

# Tor settings
DEFAULT_SOCKS_PORT = 9050
DEFAULT_CONTROL_PORT = 9051
```

---

## 🎯 Usage Examples

### Basic Bot
```python
from tortrack import TelegramBot

bot = TelegramBot("YOUR_BOT_TOKEN")
bot.run()
```

### Advanced Configuration
```python
import os
from tortrack import TelegramBot, TorManager

# Custom Tor setup
tor_manager = TorManager(socks_port=9150, control_port=9151)

# Bot with custom settings
bot = TelegramBot(
    token=os.getenv('BOT_TOKEN'),
    use_tor=True,
    mongo_uri=os.getenv('MONGO_URI')
)

# Manual setup (advanced)
async def setup():
    await tor_manager.start()
    print(f"Tor IP: {tor_manager.get_current_ip()}")
    bot.run()

import asyncio
asyncio.run(setup())
```

### Custom Handler Integration
```python
from tortrack import TelegramBot
from aiogram import Router
from aiogram.types import Message

# Create custom router
custom_router = Router()

@custom_router.message()
async def custom_handler(message: Message):
    await message.answer("Custom response!")

# Add to bot (requires modifying handlers.py)
# This is advanced usage - see source code for details
```

### Database Operations
```python
from tortrack.database import Database
import asyncio

async def check_user_stats(user_id):
    db = Database("mongodb://localhost:27017/tortrack")
    await db.init()
    
    downloads = await db.get_user_downloads_today(user_id)
    is_vip = await db.is_vip_user(user_id)
    
    print(f"User {user_id}: {downloads} downloads, VIP: {is_vip}")
    
    await db.close()

asyncio.run(check_user_stats(123456))
```

---

## 🐛 Error Handling

### Common Exceptions

```python
try:
    bot = TelegramBot("invalid_token")
    bot.run()
except ValueError as e:
    print(f"Configuration error: {e}")
except ConnectionError as e:
    print(f"Network error: {e}")
except KeyboardInterrupt:
    print("Bot stopped by user")
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Tor-Specific Errors

```python
from tortrack import TorManager

tor = TorManager()
try:
    success = await tor.start()
    if not success:
        print("Tor failed to start - running without anonymity")
except Exception as e:
    print(f"Tor error: {e}")
```

### Database Errors

```python
from tortrack.database import Database

try:
    db = Database("mongodb://invalid:27017/db")
    await db.init()
except Exception as e:
    print(f"Database error: {e}")
    print("Running without database features")
```

---

## 🔍 Debugging

### Enable Verbose Logging
```python
import logging
logging.basicConfig(level=logging.DEBUG)

from tortrack import TelegramBot
bot = TelegramBot("YOUR_TOKEN")
bot.run()
```

### Check Component Status
```python
import asyncio
from tortrack import TelegramBot, TorManager

async def debug_setup():
    # Test Tor
    tor = TorManager()
    tor_ok = await tor.start()
    print(f"Tor status: {'✅' if tor_ok else '❌'}")
    
    if tor_ok:
        print(f"Current IP: {tor.get_current_ip()}")
    
    # Test bot creation
    try:
        bot = TelegramBot("test_token", use_tor=False)
        print("Bot creation: ✅")
    except Exception as e:
        print(f"Bot creation: ❌ {e}")

asyncio.run(debug_setup())
```

---

Need more help? Check the [Examples](Examples) page or [open an issue](https://github.com/MohammadHNdev/tortrack/issues)!