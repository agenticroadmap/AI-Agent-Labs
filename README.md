# AI Agent Labs

آزمایشگاه عملی ساخت AI Agentها به زبان فارسی.

این ریپو بازوی فنی AgenticRoadmap است؛ جایی برای ساخت، تست و نمایش Agentهای واقعی.

## هدف

در سایت AgenticRoadmap مفاهیم را یاد می‌گیریم.
در اینجا همان مفاهیم را به Agentهای قابل اجرا تبدیل می‌کنیم.

## Labs

| شماره | Agent                                        | وضعیت   | هدف                                            |
| ----- | -------------------------------------------- | ------- | ---------------------------------------------- |
| 01    | [First Agent](./labs/01-first-agent)         | آماده   | اولین ارتباط ساده با مدل زبانی                 |
| 02    | [Tool Calling Agent](./labs/02-tool-calling) | آماده   | انتخاب و اجرای ابزار توسط Agent                |
| 03    | [Memory Agent](./labs/03-memory-agent)       | آماده   | ذخیره اطلاعات کاربر و استفاده در پاسخ‌های بعدی |
| 04    | [RAG Agent](./labs/04-rag-agent)             | آماده   | پاسخ‌دهی بر اساس فایل‌ها و منابع اختصاصی       |
| 05    | [Web Research Agent](./labs/05-web-research-agent) | آماده | تحقیق وبی و تولید گزارش ساختاریافته |

## Business Agents

| شماره | Agent | وضعیت | هدف |
|---|---|---|---|
| 01 | [GitHub Repo Analyzer Agent](./projects/github-repo-analyzer-agent) | آماده | تحلیل Repositoryهای GitHub و تولید گزارش فارسی |

## استاندارد هر Agent

هر Agent در این ریپو شامل این بخش‌هاست:

* README فارسی
* کد قابل اجرا
* نمونه خروجی
* فایل تنظیمات محیطی
* توضیح اجرای محلی

## اجرای پروژه‌ها

هر Agent به‌صورت جداگانه اجرا می‌شود.
برای نمونه:

```bash
git clone https://github.com/agenticroadmap/AI-Agent-Labs.git
cd AI-Agent-Labs/labs/02-tool-calling
pip install -r requirements.txt
python main.py
```

## لینک‌ها

* Website: https://agenticroadmap.ir
* X: https://x.com/agenticroadmap
* Telegram: https://t.me/agenticroadmap
