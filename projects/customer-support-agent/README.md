# Customer Support Agent

ششمین Business Agent در AgenticRoadmap Labs.

## هدف

این Agent سؤال یا پیام مشتری را دریافت می‌کند و با کمک یک فایل دانش پشتیبانی، پاسخ فارسی، دقیق و کاربردی تولید می‌کند.

## این Agent چه کار می‌کند؟

```text
Customer Message
↓
Support Knowledge Base
↓
AI Agent
↓
Persian Support Reply
```

## نمونه ورودی

```text
چطور می‌توانم اشتراکم را لغو کنم؟
```

## خروجی مورد انتظار

Agent پاسخی تولید می‌کند شامل:

* پاسخ مستقیم به سؤال مشتری
* لحن محترمانه و حرفه‌ای
* راهنمایی مرحله‌به‌مرحله
* هشدار در صورت نیاز به بررسی انسانی
* متن آماده ارسال برای پشتیبانی

## چرا این Agent مهم است؟

پشتیبانی مشتری یکی از واضح‌ترین کاربردهای AI Agent در کسب‌وکارهاست.
این Agent می‌تواند پایه یک سرویس واقعی برای پاسخ‌گویی، دسته‌بندی درخواست‌ها و کاهش فشار تیم پشتیبانی باشد.

## کاربردهای آینده

* پاسخ‌گویی اولیه به مشتریان
* ساخت Helpdesk Agent
* تحلیل پیام‌های پشتیبانی
* اتصال به FAQ یا مستندات داخلی
* آماده‌سازی پاسخ برای تیم Support

## فایل‌های این پروژه

```text
main.py
requirements.txt
.env.example
knowledge/support.md
demo/sample-output.md
```

## اجرا روی سیستم شخصی

این پروژه روی خود GitHub اجرا نمی‌شود.
برای اجرا باید ریپو را روی سیستم خود Clone کنید:

```bash
git clone https://github.com/agenticroadmap/AI-Agent-Labs.git
cd AI-Agent-Labs/projects/customer-support-agent
pip install -r requirements.txt
```

سپس کلید API را تنظیم کنید:

```bash
export OPENAI_API_KEY="your_api_key_here"
```

در ویندوز:

```bash
set OPENAI_API_KEY=your_api_key_here
```

بعد اجرا کنید:

```bash
python main.py
```

## وضعیت

در حال ساخت...
