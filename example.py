#!/usr/bin/env python3
"""
Simple example showing how easy it is to use TorTrack
"""

from tortrack import TelegramBot

# This is all you need!
if __name__ == "__main__":
    # Replace with your actual bot token from @BotFather
    BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
    
    # Create and run bot with one line!
    bot = TelegramBot(BOT_TOKEN)
    bot.run()
    
    # That's it! Your music download bot is running with:
    # ✅ Tor anonymity
    # ✅ User limits  
    # ✅ Smart archiving
    # ✅ Multiple formats support