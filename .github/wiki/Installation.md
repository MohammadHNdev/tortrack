# 🔧 Complete Installation Guide

This guide covers everything you need to know about installing and configuring TorTrack.

## 📋 System Requirements

- **Python 3.8+** (Python 3.10+ recommended)
- **10MB+ free disk space** for the package
- **Internet connection** for downloads
- **Optional**: MongoDB for user management
- **Optional**: Tor for anonymity

## ⚡ Quick Installation

### Method 1: PyPI (Recommended)
```bash
pip install tortrack
```

### Method 2: From Source
```bash
git clone https://github.com/MohammadHNdev/tortrack.git
cd tortrack
pip install -e .
```

### Method 3: Development Install
```bash
git clone https://github.com/MohammadHNdev/tortrack.git
cd tortrack
pip install -e .[dev]  # Includes development tools
```

## 🤖 Telegram Bot Setup

### Step 1: Create Bot
1. Open Telegram and message [@BotFather](https://t.me/BotFather)
2. Send `/newbot`
3. Choose a name: `Your Music Bot`
4. Choose a username: `yourmusicbot_bot`
5. **Copy the token** - looks like: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`

### Step 2: Configure Bot (Optional)
```
/setdescription - Simple music download bot
/setabouttext - Downloads music from Spotify links
/setuserpic - Upload a nice profile picture
/setcommands - Set these commands:
start - Welcome message
help - Usage instructions  
stats - Download statistics
```

## 🎵 Spotify API Setup (Optional but Recommended)

### Why You Need This
- **Better metadata** - Accurate song titles, artists, albums
- **Faster searches** - Direct API access vs web scraping
- **More reliable** - Less likely to break with website changes

### Step 1: Create Spotify App
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Log in with your Spotify account
3. Click **"Create App"**
4. Fill in details:
   - **App name**: `My Music Bot`
   - **App description**: `Personal music download tool`
   - **Website**: Leave blank or use your GitHub
   - **Redirect URI**: `http://localhost:8080` (won't be used)
   - **APIs used**: Check **Web API**
5. Click **"Save"**

### Step 2: Get Credentials
1. Click on your new app
2. Click **"Settings"**
3. Copy **Client ID**
4. Click **"View client secret"** and copy **Client Secret**

### Step 3: Set Environment Variables

#### Linux/macOS:
```bash
export SPOTIFY_CLIENT_ID="your_client_id_here"
export SPOTIFY_CLIENT_SECRET="your_client_secret_here"

# Make it permanent (add to ~/.bashrc or ~/.zshrc):
echo 'export SPOTIFY_CLIENT_ID="your_client_id_here"' >> ~/.bashrc
echo 'export SPOTIFY_CLIENT_SECRET="your_client_secret_here"' >> ~/.bashrc
source ~/.bashrc
```

#### Windows (Command Prompt):
```cmd
set SPOTIFY_CLIENT_ID=your_client_id_here
set SPOTIFY_CLIENT_SECRET=your_client_secret_here
```

#### Windows (PowerShell):
```powershell
$env:SPOTIFY_CLIENT_ID="your_client_id_here"
$env:SPOTIFY_CLIENT_SECRET="your_client_secret_here"
```

#### Using .env File:
```bash
# Create .env file in your project directory
echo "SPOTIFY_CLIENT_ID=your_client_id_here" > .env
echo "SPOTIFY_CLIENT_SECRET=your_client_secret_here" >> .env
```

## 🧅 Tor Installation & Configuration

### Why Use Tor?
- **Complete anonymity** - Your server IP is never exposed
- **Bypass blocks** - Avoid IP-based rate limiting
- **Geographic freedom** - Access content from anywhere
- **Production safety** - Servers won't get blacklisted

### Install Tor

#### Ubuntu/Debian:
```bash
sudo apt update
sudo apt install tor
sudo systemctl enable tor
sudo systemctl start tor
```

#### CentOS/RHEL/Fedora:
```bash
sudo dnf install tor  # Fedora
sudo yum install tor  # CentOS/RHEL
sudo systemctl enable tor
sudo systemctl start tor
```

#### macOS:
```bash
brew install tor
brew services start tor
```

#### Windows:
1. Download from [https://www.torproject.org/download/](https://www.torproject.org/download/)
2. Install Tor Browser (includes Tor daemon)
3. Or use [Tor Expert Bundle](https://www.torproject.org/download/tor/)

### Verify Tor Installation
```bash
# Check if Tor is running
sudo netstat -tlnp | grep 9050  # Should show Tor SOCKS proxy

# Test Tor connection (optional)
curl --socks5 127.0.0.1:9050 https://check.torproject.org/api/ip
```

## 🗄️ MongoDB Setup (Optional)

### Why Use MongoDB?
- **User management** - Track download limits per user
- **Smart archiving** - Avoid re-downloading same tracks
- **Statistics** - Monitor bot usage and performance
- **VIP features** - Implement premium user tiers

### Install MongoDB

#### Ubuntu/Debian:
```bash
# Import MongoDB public key
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -

# Create MongoDB list file
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list

# Install MongoDB
sudo apt update
sudo apt install -y mongodb-org

# Start MongoDB
sudo systemctl enable mongod
sudo systemctl start mongod
```

#### macOS:
```bash
brew tap mongodb/brew
brew install mongodb-community
brew services start mongodb-community
```

#### Docker (Easiest):
```bash
docker run --name mongodb -d -p 27017:27017 mongo:latest
```

### Test MongoDB Connection
```bash
# Test connection
mongosh --eval "db.runCommand({connectionStatus: 1})"

# Should return: "ok": 1
```

## ✅ Verify Installation

### Test 1: Package Import
```bash
python -c "from tortrack import TelegramBot; print('✅ TorTrack imported successfully')"
```

### Test 2: CLI Command
```bash
tortrack --help
# Should show help message
```

### Test 3: Bot Creation
```bash
python -c "
from tortrack import TelegramBot
bot = TelegramBot('test_token', use_tor=False)
print('✅ Bot created successfully')
"
```

### Test 4: Full System Test
```bash
python -c "
import os
from tortrack import TelegramBot

# Check environment variables
spotify_id = os.getenv('SPOTIFY_CLIENT_ID')
if spotify_id:
    print('✅ Spotify credentials found')
else:
    print('⚠️  Spotify credentials not set (optional)')

# Test bot creation
try:
    bot = TelegramBot('test_token', use_tor=False)
    print('✅ All components working')
except Exception as e:
    print(f'❌ Error: {e}')
"
```

## 🚀 First Run

### Basic Usage:
```bash
tortrack YOUR_BOT_TOKEN_HERE
```

### With Custom MongoDB:
```bash
tortrack YOUR_BOT_TOKEN --mongo mongodb://localhost:27017/mybot
```

### Without Tor (for testing):
```bash
tortrack YOUR_BOT_TOKEN --no-tor
```

### Production Example:
```bash
# Set environment variables
export BOT_TOKEN="your_bot_token"
export SPOTIFY_CLIENT_ID="your_spotify_id"
export SPOTIFY_CLIENT_SECRET="your_spotify_secret"
export MONGO_URI="mongodb://localhost:27017/musicbot"

# Run bot
tortrack $BOT_TOKEN --mongo $MONGO_URI
```

## 🔧 Configuration Files

### Environment Variables (.env)
Create `.env` file in your project directory:
```bash
# Telegram Bot
BOT_TOKEN=123456789:ABCdefGHIjklMNOpqrsTUVwxyz

# Spotify API (optional)
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret

# Database (optional)
MONGO_URI=mongodb://localhost:27017/tortrack

# Tor Settings (optional)
TOR_SOCKS_PORT=9050
TOR_CONTROL_PORT=9051
```

### Python Configuration
```python
import os
from tortrack import TelegramBot

# Load from environment
TOKEN = os.getenv('BOT_TOKEN')
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/tortrack')

bot = TelegramBot(
    token=TOKEN,
    use_tor=True,
    mongo_uri=MONGO_URI
)

bot.run()
```

## 🐛 Troubleshooting Installation

### Common Issues & Solutions

#### Issue: `pip install tortrack` fails
```bash
# Try with --user flag
pip install --user tortrack

# Or upgrade pip first
pip install --upgrade pip
pip install tortrack

# Or use Python specific version
python3.10 -m pip install tortrack
```

#### Issue: Permission denied errors
```bash
# Don't use sudo with pip, use virtual environment instead
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows
pip install tortrack
```

#### Issue: Module not found after installation
```bash
# Check installation location
pip show tortrack

# Check Python path
python -c "import sys; print('\n'.join(sys.path))"

# Reinstall in current environment
pip uninstall tortrack
pip install tortrack
```

#### Issue: Tor connection fails
```bash
# Check if Tor is running
sudo systemctl status tor

# Test Tor proxy manually
curl --socks5 127.0.0.1:9050 https://httpbin.org/ip

# Start Tor manually if needed
sudo systemctl start tor
```

#### Issue: MongoDB connection fails
```bash
# Check if MongoDB is running
sudo systemctl status mongod

# Test connection
mongosh --eval "db.runCommand({ping: 1})"

# Start MongoDB if needed
sudo systemctl start mongod
```

## 🔄 Updating TorTrack

### Update from PyPI:
```bash
pip install --upgrade tortrack
```

### Update from Source:
```bash
cd tortrack
git pull origin main
pip install -e .
```

### Check Version:
```bash
pip show tortrack
```

## 🎯 Next Steps

After successful installation:

1. **[Quick Start Guide](Quick-Start)** - Get running in 60 seconds
2. **[Examples](Examples)** - See real usage patterns
3. **[API Reference](API-Reference)** - Advanced customization
4. **[Deployment](Deployment)** - Host on cloud platforms

---

**Installation complete!** 🎉 Ready to build your music bot? Start with the [Quick Start Guide](Quick-Start).