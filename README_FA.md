# 🎵 TorTrack

**ربات تلگرام ساده برای دانلود ناشناس موزیک**

TorTrack یک پکیج Python هست که بهت اجازه میده ربات تلگرام دانلود موزیک خودت رو با قابلیت ناشناس‌سازی Tor راه‌اندازی کنی. فقط توکن ربات بده و آماده!

## ⚡ شروع سریع

### نصب
```bash
pip install tortrack
```

### استفاده ساده
```python
from tortrack import TelegramBot

# همین! فقط توکن ربات رو بده
bot = TelegramBot("توکن_ربات_شما")
bot.run()
```

### خط فرمان
```bash
# شروع با ناشناس‌سازی Tor
tortrack توکن_ربات_شما

# شروع بدون Tor (توصیه نمیشه)
tortrack توکن_ربات_شما --no-tor
```

## 🚀 قابلیت‌ها

- **راه‌اندازی یک خطی** - فقط توکن ربات بده
- **ناشناس‌سازی Tor** - پروکسی Tor داخلی برای دانلود ناشناس
- **منابع متعدد** - دانلود از یوتیوب، ساندکلاود و بقیه
- **آرشیو هوشمند** - از دانلود مجدد همون آهنگ‌ها جلوگیری میکنه
- **محدودیت کاربر** - محدودیت نرخ داخلی (۵ دانلود/روز برای کاربران معمولی)
- **کیفیت بالا** - دانلود MP3 با کیفیت ۱۹۲kbps
- **پشتیبانی پلی‌لیست** - کار با آهنگ، آلبوم و پلی‌لیست‌های اسپاتیفای

## 📋 نیازمندی‌ها

- Python 3.8+
- توکن ربات تلگرام (از [@BotFather](https://t.me/BotFather) بگیر)
- MongoDB (اختیاری، برای محدودیت کاربر و آرشیو)
- Tor (اختیاری، برای ناشناس‌سازی)

## 🔧 راه‌اندازی

### ۱. گرفتن توکن ربات
به [@BotFather](https://t.me/BotFather) تو تلگرام پیام بده:
```
/newbot
اسم_ربات_شما
نام_کاربری_ربات_bot
```

### ۲. گرفتن اطلاعات اسپاتیفای (اختیاری)
1. برو به [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. اپ جدید بساز
3. Client ID و Secret رو بگیر

```bash
export SPOTIFY_CLIENT_ID="آیدی_کلاینت_شما"
export SPOTIFY_CLIENT_SECRET="سکرت_کلاینت_شما"
```

### ۳. نصب Tor (برای ناشناس‌سازی)
```bash
# Ubuntu/Debian
sudo apt install tor

# macOS
brew install tor

# Windows
# از https://www.torproject.org/ دانلود کن
```

### ۴. شروع ربات
```bash
tortrack توکن_ربات_تو_اینجا
```

## 💻 استفاده پیشرفته

### تنظیمات دلخواه
```python
from tortrack import TelegramBot

bot = TelegramBot(
    token="توکن_ربات_شما",
    use_tor=True,  # فعال کردن ناشناس‌سازی Tor
    mongo_uri="mongodb://localhost:27017/ربات_من"
)

bot.run()
```

### استفاده کتابخانه‌ای
```python
from tortrack import TelegramBot, TorManager

# راه‌اندازی پیشرفته با تنظیمات Tor دلخواه
tor_manager = TorManager(socks_port=9050, control_port=9051)
await tor_manager.start()

bot = TelegramBot("توکن_شما", use_tor=False)
# از tor_manager دلخواه خودت استفاده کن
```

### متغیرهای محیطی
```bash
# API اسپاتیفای (اختیاری ولی توصیه میشه)
export SPOTIFY_CLIENT_ID="آیدی_کلاینت_اسپاتیفای_شما"
export SPOTIFY_CLIENT_SECRET="سکرت_کلاینت_اسپاتیفای_شما"

# MongoDB (اختیاری)
export MONGO_URI="mongodb://localhost:27017/tortrack"
```

## 🎯 لینک‌های پشتیبانی شده

ربات شما این لینک‌های اسپاتیفای رو پردازش میکنه:
- `https://open.spotify.com/track/...` - آهنگ‌های تکی
- `https://open.spotify.com/album/...` - آلبوم‌های کامل
- `https://open.spotify.com/playlist/...` - پلی‌لیست‌ها

## 🛡️ امنیت و ناشناس‌سازی

TorTrack از Tor برای این کارها استفاده میکنه:
- مخفی کردن IP آدرس سرور شما
- جلوگیری از محدودیت نرخ و مسدود شدن IP
- محافظت در برابر محدودیت‌های جغرافیایی
- حفظ ناشناس‌سازی هنگام دانلود

**بدون Tor:** IP سرور شما برای منابع دانلود قابل مشاهده هست و ممکنه مسدود بشه.

**با Tor:** تمام ترافیک از شبکه Tor رد میشه برای ناشناس‌سازی کامل.

## 📊 دستورات ربات

کاربران میتونن با ربات شما اینطوری کار کنن:
- `/start` - پیام خوش‌آمدگویی
- `/help` - راهنمای استفاده
- `/stats` - آمار دانلود
- هر لینک اسپاتیفای رو بفرست تا دانلود کنه

## 🔧 استقرار

### توسعه محلی
```bash
git clone https://github.com/MohammadHNdev/tortrack.git
cd tortrack
pip install -e .
python -m tortrack توکن_شما
```

### Docker (به زودی)
```bash
docker run -e BOT_TOKEN=توکن_شما tortrack/tortrack
```

### استقرار ابری
روی هر پلتفرم هاستینگ Python کار میکنه:
- Railway
- Heroku
- DigitalOcean
- AWS Lambda
- Google Cloud Run

## 🚨 نکات مهم

1. **قانونی:** فقط موزیک‌هایی دانلود کن که حق استفاده ازشون رو داری
2. **محدودیت نرخ:** محدودیت‌های داخلی از سوء استفاده جلوگیری میکنه
3. **منابع:** دانلودها از فضای ذخیره‌سازی موقت استفاده میکنن
4. **راه‌اندازی Tor:** برای ویژگی‌های ناشناس‌سازی باید Tor نصب باشه

## 📝 مجوز

مجوز MIT - هرطوری خواستی استفاده کن!

## 🤝 مشارکت

باگ پیدا کردی؟ ویژگی می‌خوای؟ Issue یا PR باز کن!

## 📞 پشتیبانی

- 🐛 [گزارش مشکلات](https://github.com/MohammadHNdev/tortrack/issues)
- 💬 [بحث‌ها](https://github.com/MohammadHNdev/tortrack/discussions)
- 📧 ایمیل: hosein.norozi434@gmail.com

---

## 🎯 مثال‌های کاربردی

### مثال ۱: ربات ساده
```python
from tortrack import TelegramBot

# فقط همین!
bot = TelegramBot("توکن_ربات_از_BotFather")
bot.run()
```

### مثال ۲: ربات بدون دیتابیس
```python
from tortrack import TelegramBot

# بدون MongoDB - فقط دانلود
bot = TelegramBot(
    token="توکن_شما",
    mongo_uri=None  # غیرفعال کردن دیتابیس
)
bot.run()
```

### مثال ۳: ربات تست (بدون Tor)
```python
from tortrack import TelegramBot

# برای تست محلی
bot = TelegramBot(
    token="توکن_شما",
    use_tor=False  # غیرفعال کردن Tor
)
bot.run()
```

### مثال ۴: راه‌اندازی در سرور
```python
import os
from tortrack import TelegramBot

# خوندن تنظیمات از متغیرهای محیطی
TOKEN = os.getenv('BOT_TOKEN')
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/music_bot')

if not TOKEN:
    print("❌ BOT_TOKEN تنظیم نشده!")
    exit(1)

bot = TelegramBot(
    token=TOKEN,
    use_tor=True,
    mongo_uri=MONGO_URI
)

print("🚀 ربات موزیک شروع شد...")
bot.run()
```

## 🔧 تنظیمات پیشرفته

### تنظیم پورت‌های Tor
```python
from tortrack import TorManager, TelegramBot

# تنظیم پورت‌های دلخواه برای Tor
tor_manager = TorManager(
    socks_port=9150,    # پورت SOCKS5
    control_port=9151   # پورت کنترل
)

# استفاده در ربات
bot = TelegramBot("توکن_شما")
# تنظیمات Tor دستی...
```

### مدیریت خطا
```python
from tortrack import TelegramBot
import logging

# فعال کردن لاگ‌های تفصیلی
logging.basicConfig(level=logging.DEBUG)

try:
    bot = TelegramBot("توکن_شما")
    bot.run()
except KeyboardInterrupt:
    print("ربات توسط کاربر متوقف شد")
except Exception as e:
    print(f"خطا: {e}")
```

## 📱 نصب در سرورهای مختلف

### Railway
```bash
# railway.json
{
  "build": {
    "command": "pip install tortrack"
  },
  "start": {
    "command": "tortrack $BOT_TOKEN"
  }
}
```

### Heroku
```bash
# Procfile
worker: tortrack $BOT_TOKEN

# requirements.txt
tortrack
```

### Docker
```dockerfile
FROM python:3.11-slim

RUN apt-get update && apt-get install -y tor
RUN pip install tortrack

ENV BOT_TOKEN=""
CMD ["sh", "-c", "tortrack $BOT_TOKEN"]
```

---

**ساخته شده با ❤️ توسط [محمدحسین نوروزی](https://github.com/MohammadHNdev)**

*نسخه فارسی - Iranian Developer Community*