# Website Analyzer Agent

دومین Business Agent در AgenticRoadmap Labs.

## هدف

این Agent یک آدرس وب‌سایت دریافت می‌کند و یک گزارش فارسی، ساختاریافته و کاربردی درباره وضعیت کلی سایت تولید می‌کند.

## این Agent چه کار می‌کند؟

```text
Website URL
↓
Read Page Content
↓
Analyze Structure and Messaging
↓
AI Agent
↓
Persian Website Report
```

## نمونه ورودی

```text
https://agenticroadmap.ir
```

## خروجی مورد انتظار

Agent گزارشی تولید می‌کند شامل:

* سایت درباره چیست؟
* پیام اصلی سایت چقدر واضح است؟
* مخاطب هدف چه کسی است؟
* نقاط قوت سایت چیست؟
* ضعف‌های احتمالی چیست؟
* پیشنهادهای بهبود محتوا و ساختار چیست؟
* آیا سایت برای تبدیل کاربر به مشتری/عضو/خواننده آماده است؟

## چرا این Agent مهم است؟

این Agent می‌تواند پایه یک سرویس واقعی برای تحلیل سایت شرکت‌ها باشد؛ مخصوصاً برای کسب‌وکارهایی که می‌خواهند سایت‌شان واضح‌تر، قابل‌اعتمادتر و تبدیل‌محورتر شود.

## کاربردهای آینده

* تحلیل سایت شرکت‌ها
* بررسی صفحه اصلی کسب‌وکارها
* پیشنهاد بهبود UX و پیام برند
* کمک به تولید گزارش مشاوره‌ای
* تبدیل شدن به سرویس B2B آینده

## فایل‌های این پروژه

```text
main.py
requirements.txt
.env.example
demo/sample-output.md
```

## اجرا روی سیستم شخصی

این پروژه روی خود GitHub اجرا نمی‌شود.
برای اجرا باید ریپو را روی سیستم خود Clone کنید:

```bash
git clone https://github.com/agenticroadmap/AI-Agent-Labs.git
cd AI-Agent-Labs/projects/website-analyzer-agent
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
