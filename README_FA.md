# ربات قیمت بیت‌کوین

این یک ربات تلگرام است که قیمت بیت‌کوین را با استفاده از API بایننس مانیتور کرده و تغییرات قیمت و الگوهای شمعی را در یک چت تلگرام گزارش می‌دهد.

## ویژگی‌ها

- **مانیتورینگ قیمت**: به طور مداوم قیمت بیت‌کوین را مانیتور کرده و تغییرات درصدی آن را محاسبه می‌کند.
- **گزارش شدت تغییرات**: شدت تغییرات قیمت را بر اساس آستانه‌های تعریف‌شده گزارش می‌دهد.
- **الگوهای شمعی**: الگوهای شمعی را از داده‌های اخیر شناسایی کرده و گزارش می‌دهد.

## نصب

1. مخزن را کلون کنید:

    ```bash
    git clone https://github.com/yourusername/bitcoin-price-bot.git
    ```

2. پکیج‌های مورد نیاز پایتون را نصب کنید:

    ```bash
    pip install pyTelegramBotAPI requests pandas ta
    ```

3. توکن API ربات تلگرام خود را با `YOUR_TELEGRAM_API_TOKEN` در اسکریپت جایگزین کنید.

## استفاده

1. اسکریپت ربات را اجرا کنید:

    ```bash
    python bot.py
    ```

2. با ارسال دستور `/start` در چت تلگرام خود، ربات را شروع کنید.

## پیکربندی

- **TELEGRAM_API_TOKEN**: توکن ربات تلگرام شما.
- **BINANCE_API_URL**: URL API برای دریافت قیمت بیت‌کوین.
- **BINANCE_CANDLESTICK_API_URL**: URL API برای دریافت داده‌های شمعی.

## مجوز

این پروژه تحت مجوز MIT منتشر شده است - جزئیات در فایل [LICENSE](LICENSE) آمده است.

## تشکر و قدردانی

- [Telebot](https://github.com/eternnoir/pyTelegramBotAPI)
- [Requests](https://requests.readthedocs.io/en/latest/)
- [Pandas](https://pandas.pydata.org/)
- [کتابخانه تحلیل تکنیکال (TA)](https://technical-analysis-library-in-python.readthedocs.io/en/latest/)
