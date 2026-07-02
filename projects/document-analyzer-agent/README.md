# Document Analyzer Agent

سومین Business Agent در AgenticRoadmap Labs.

## هدف

این Agent یک فایل متنی یا سند ساده دریافت می‌کند و یک گزارش فارسی، ساختاریافته و کاربردی از محتوای آن تولید می‌کند.

## این Agent چه کار می‌کند؟

```text
Document File
↓
Extract Text
↓
Analyze Content
↓
AI Agent
↓
Persian Document Report
```

## نوع فایل‌های پشتیبانی‌شده

در نسخه اولیه:

* `.txt`
* `.md`

در نسخه‌های بعدی:

* `.pdf`
* `.docx`

## خروجی مورد انتظار

Agent گزارشی تولید می‌کند شامل:

* خلاصه سند
* موضوع اصلی
* نکات کلیدی
* ریسک‌ها یا ابهام‌ها
* پیشنهادهای عملی
* جمع‌بندی تصمیم‌محور

## چرا این Agent مهم است؟

بسیاری از شرکت‌ها با فایل‌ها و مستندات زیادی کار می‌کنند.
این Agent می‌تواند پایه یک سرویس واقعی برای تحلیل قراردادها، گزارش‌ها، پروپوزال‌ها، مستندات داخلی و فایل‌های آموزشی باشد.

## کاربردهای آینده

* تحلیل قرارداد
* تحلیل پروپوزال
* خلاصه‌سازی گزارش‌های طولانی
* استخراج نکات مهم از مستندات شرکت
* آماده‌سازی سرویس Document Intelligence

## فایل‌های این پروژه

```text
main.py
requirements.txt
.env.example
documents/sample.md
demo/sample-output.md
```

## اجرا روی سیستم شخصی

این پروژه روی خود GitHub اجرا نمی‌شود.
برای اجرا باید ریپو را روی سیستم خود Clone کنید:

```bash
git clone https://github.com/agenticroadmap/AI-Agent-Labs.git
cd AI-Agent-Labs/projects/document-analyzer-agent
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
