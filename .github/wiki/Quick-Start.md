# 🚀 Quick Start Guide

Get your TorTrack music bot running in under 60 seconds!

## ⚡ Super Quick Setup

### 1. Install TorTrack
```bash
pip install tortrack
```

### 2. Get Bot Token
Message [@BotFather](https://t.me/BotFather) on Telegram:
```
/newbot
YourBotName
yourbotname_bot
```
Copy the token (looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

### 3. Run Your Bot
```bash
tortrack YOUR_BOT_TOKEN_HERE
```

**That's it!** Your bot is now running with:
- ✅ Tor anonymity enabled
- ✅ User limits (5 downloads/day)
- ✅ Smart archiving
- ✅ Multi-format support

## 📱 Test Your Bot

1. Open Telegram and find your bot
2. Send `/start` to see the welcome message
3. Send a Spotify link like: `https://open.spotify.com/track/4iV5W9uYEdYUVa79Axb7Rh`
4. Wait for your music download! 🎵

## 🐍 Python Method

Prefer Python code? Use this:

```python
from tortrack import TelegramBot

# Replace with your actual token
bot = TelegramBot("123456789:ABCdefGHIjklMNOpqrsTUVwxyz")
bot.run()
```

## 🔧 Optional: Spotify API Setup

For better metadata and faster searches:

1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Create new app
3. Get Client ID and Secret
4. Set environment variables:

```bash
export SPOTIFY_CLIENT_ID="your_client_id"
export SPOTIFY_CLIENT_SECRET="your_client_secret"
```

## 🧅 Optional: Tor Setup

TorTrack works with or without Tor, but for maximum anonymity:

```bash
# Ubuntu/Debian
sudo apt install tor

# macOS
brew install tor

# Then restart your bot
tortrack YOUR_BOT_TOKEN
```

## 🗄️ Optional: Database Setup

For user limits and archiving, install MongoDB:

```bash
# Ubuntu/Debian
sudo apt install mongodb

# macOS
brew install mongodb-community

# Use custom database
tortrack YOUR_BOT_TOKEN --mongo mongodb://localhost:27017/mybot
```

## 🎯 What Your Users See

When someone uses your bot:

1. **Send `/start`**:
```
🎵 TorTrack Music Bot

Welcome! Send me a Spotify link and I'll download it for you.

Supported links:
• Spotify tracks
• Spotify albums  
• Spotify playlists

Features:
• Anonymous downloads via Tor
• High quality MP3 (192kbps)
• Fast and reliable

Just send me a link to get started! 🚀
```

2. **Send Spotify link**:
```
⏳ Processing your request...
🎵 Downloading: Song Name - Artist Name
📤 Uploading...
```

3. **Receive music file** with metadata and cover art!

## 🔍 Troubleshooting Quick Fixes

### Bot doesn't respond?
- Check token is correct
- Make sure bot is running
- Try `/start` command first

### Downloads fail?
- Check internet connection
- Verify Spotify links are valid
- Try without Tor: `tortrack YOUR_TOKEN --no-tor`

### Permission errors?
- Use virtual environment
- Don't run as root/administrator
- Check Python version (3.8+ required)

## ⚙️ Advanced Quick Setup

### Production deployment:
```python
import os
from tortrack import TelegramBot

TOKEN = os.getenv('BOT_TOKEN')
bot = TelegramBot(
    token=TOKEN,
    use_tor=True,
    mongo_uri=os.getenv('MONGO_URI', 'mongodb://localhost:27017/music')
)
bot.run()
```

### Docker quick start:
```dockerfile
FROM python:3.11-slim
RUN apt-get update && apt-get install -y tor
RUN pip install tortrack
ENV BOT_TOKEN=""
CMD ["sh", "-c", "tortrack $BOT_TOKEN"]
```

## 🎉 Next Steps

Now that your bot is running:

- **[Read Full Documentation](Installation)** - Complete setup guide
- **[Check Examples](Examples)** - Real-world usage patterns  
- **[Deploy to Cloud](Deployment)** - Host on various platforms
- **[API Reference](API-Reference)** - Advanced customization
- **[Persian Guide](Persian-Quick-Start)** - راهنمای فارسی

## 💡 Pro Tips

- **Test locally first**: Use `--no-tor` for faster local testing
- **Monitor logs**: Enable verbose mode to see what's happening
- **Set limits**: Default is 5 downloads/day per user (customizable)
- **Use environment variables**: Keep tokens secure with `.env` files

---

**🎵 Enjoy your new music bot!** Need help? Check [Troubleshooting](Troubleshooting) or [open an issue](https://github.com/MohammadHNdev/tortrack/issues).