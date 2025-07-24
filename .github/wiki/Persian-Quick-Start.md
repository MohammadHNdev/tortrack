# 🚀 راهنمای شروع سریع

ربات موزیک TorTrack خودت رو در کمتر از ۶۰ ثانیه اجرا کن!

## ⚡ راه‌اندازی فوق سریع

### ۱. نصب TorTrack
```bash
pip install tortrack
```

### ۲. گرفتن توکن ربات
به [@BotFather](https://t.me/BotFather) تو تلگرام پیام بده:
```
/newbot
اسم_ربات_شما
نام_کاربری_ربات_bot
```
توکن رو کپی کن (شبیه این: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

### ۳. اجرای ربات
```bash
tortrack توکن_ربات_شما_اینجا
```

**همین!** ربات شما الان در حال اجرا هست با:
- ✅ ناشناس‌سازی Tor فعال
- ✅ محدودیت کاربر (۵ دانلود روزانه)
- ✅ آرشیو هوشمند
- ✅ پشتیبانی چند فرمت

## 📱 تست ربات

1. تلگرام باز کن و ربات رو پیدا کن
2. `/start` بفرست تا پیام خوش‌آمدگویی رو ببینی
3. یه لینک اسپاتیفای بفرست مثل: `https://open.spotify.com/track/4iV5W9uYEdYUVa79Axb7Rh`
4. منتظر دانلود موزیک باش! 🎵

## 🐍 روش Python

Python رو ترجیح میدی؟ از این استفاده کن:

```python
from tortrack import TelegramBot

# با توکن واقعی خودت جایگزین کن
bot = TelegramBot("123456789:ABCdefGHIjklMNOpqrsTUVwxyz")
bot.run()
```

## 🔧 اختیاری: راه‌اندازی Spotify API

برای metadata بهتر و جستجوی سریع‌تر:

1. برو به [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. اپ جدید بساز
3. Client ID و Secret رو بگیر
4. متغیرهای محیطی تنظیم کن:

```bash
export SPOTIFY_CLIENT_ID="آیدی_کلاینت_شما"
export SPOTIFY_CLIENT_SECRET="سکرت_کلاینت_شما"
```

## 🧅 اختیاری: راه‌اندازی Tor

TorTrack با یا بدون Tor کار میکنه، ولی برای حداکثر ناشناس‌سازی:

```bash
# Ubuntu/Debian
sudo apt install tor

# macOS
brew install tor

# بعد ربات رو دوباره شروع کن
tortrack توکن_ربات_شما
```

## 🗄️ اختیاری: راه‌اندازی دیتابیس

برای محدودیت کاربر و آرشیو، MongoDB نصب کن:

```bash
# Ubuntu/Debian
sudo apt install mongodb

# macOS
brew install mongodb-community

# استفاده از دیتابیس دلخواه
tortrack توکن_شما --mongo mongodb://localhost:27017/ربات_من
```

## 🎯 کاربران چی میبینن

وقتی کسی از ربات شما استفاده میکنه:

1. **ارسال `/start`**:
```
🎵 ربات موزیک TorTrack

خوش اومدی! یه لینک اسپاتیفای بفرست تا برات دانلودش کنم.

لینک‌های پشتیبانی شده:
• آهنگ‌های اسپاتیفای
• آلبوم‌های اسپاتیفای
• پلی‌لیست‌های اسپاتیفای

ویژگی‌ها:
• دانلود ناشناس از طریق Tor
• کیفیت بالا MP3 (192kbps)
• سریع و قابل اعتماد

فقط لینک بفرست تا شروع کنیم! 🚀
```

2. **ارسال لینک اسپاتیفای**:
```
⏳ در حال پردازش درخواست شما...
🎵 دانلود: نام آهنگ - نام خواننده
📤 در حال آپلود...
```

3. **دریافت فایل موزیک** با metadata و کاور آرت!

## 🔍 راه‌حل‌های سریع عیب‌یابی

### ربات جواب نمیده؟
- چک کن توکن درست باشه
- مطمئن شو ربات در حال اجرا هست
- اول دستور `/start` رو امتحان کن

### دانلود شکست میخوره؟
- اتصال اینترنت چک کن
- لینک‌های اسپاتیفای معتبر باشن
- بدون Tor امتحان کن: `tortrack توکن_شما --no-tor`

### خطای مجوز؟
- از virtual environment استفاده کن
- به عنوان root/administrator اجرا نکن
- نسخه Python چک کن (3.8+ لازم)

## ⚙️ راه‌اندازی پیشرفته سریع

### استقرار تولید:
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

### شروع سریع Docker:
```dockerfile
FROM python:3.11-slim
RUN apt-get update && apt-get install -y tor
RUN pip install tortrack
ENV BOT_TOKEN=""
CMD ["sh", "-c", "tortrack $BOT_TOKEN"]
```

## 🎉 مراحل بعدی

حالا که ربات اجرا شده:

- **[مستندات کامل بخون](Persian-Installation)** - راهنمای کامل راه‌اندازی
- **[مثال‌ها چک کن](Persian-Examples)** - الگوهای استفاده واقعی
- **[تو کلاود استقرار کن](Persian-Deployment)** - میزبانی در پلتفرم‌های مختلف
- **[مرجع API](Persian-API-Reference)** - سفارشی‌سازی پیشرفته
- **[راهنمای انگلیسی](Quick-Start)** - English guide

## 💡 نکات حرفه‌ای

- **اول محلی تست کن**: از `--no-tor` برای تست محلی سریع‌تر استفاده کن
- **لاگ‌ها رو مانیتور کن**: حالت verbose فعال کن تا ببینی چه اتفاقی میافته
- **محدودیت تنظیم کن**: پیش‌فرض ۵ دانلود روزانه هر کاربر (قابل تنظیم)
- **از متغیرهای محیطی استفاده کن**: توکن‌ها رو با فایل‌های `.env` امن نگه دار

---

**🎵 از ربات موزیک جدیدت لذت ببر!** کمک لازم داری؟ [عیب‌یابی](Persian-Troubleshooting) چک کن یا [issue باز کن](https://github.com/MohammadHNdev/tortrack/issues).