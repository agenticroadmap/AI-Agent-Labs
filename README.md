# AI Agent Labs

![Status](https://img.shields.io/badge/status-active-brightgreen)
![Language](https://img.shields.io/badge/language-Persian-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-yellow)
![Focus](https://img.shields.io/badge/focus-AI%20Agents-purple)

آزمایشگاه عملی ساخت AI Agentها به زبان فارسی.

این ریپو بازوی فنی AgenticRoadmap است؛ جایی برای ساخت، تست و نمایش Agentهای واقعی و قابل اجرا.

---

## AgenticRoadmap چیست؟

AgenticRoadmap یک پروژه فارسی برای یادگیری، ساخت و کاربردی‌کردن AI Agentهاست.

در سایت، مفاهیم را یاد می‌گیریم.
در GitHub، همان مفاهیم را به پروژه‌های عملی تبدیل می‌کنیم.

```text
Website
↓
یادگیری مفاهیم

GitHub Labs
↓
ساخت Agentهای عملی

Business Agents
↓
نمونه‌کارهای قابل تبدیل به خدمات شرکتی
```

---

## Roadmap

مسیر توسعه این پروژه در فایل زیر قابل مشاهده است:

[مشاهده Roadmap پروژه](./ROADMAP.md)

---

## Core Labs

این بخش پایه‌های اصلی ساخت AI Agent را به‌صورت عملی نشان می‌دهد.

| شماره | Agent                                              | وضعیت | هدف                                            |
| ----- | -------------------------------------------------- | ----- | ---------------------------------------------- |
| 01    | [First Agent](./labs/01-first-agent)               | آماده | اولین ارتباط ساده با مدل زبانی                 |
| 02    | [Tool Calling Agent](./labs/02-tool-calling)       | آماده | انتخاب و اجرای ابزار توسط Agent                |
| 03    | [Memory Agent](./labs/03-memory-agent)             | آماده | ذخیره اطلاعات کاربر و استفاده در پاسخ‌های بعدی |
| 04    | [RAG Agent](./labs/04-rag-agent)                   | آماده | پاسخ‌دهی بر اساس فایل‌ها و منابع اختصاصی       |
| 05    | [Web Research Agent](./labs/05-web-research-agent) | آماده | تحقیق وبی و تولید گزارش ساختاریافته            |

---

## Business Agents

این بخش شامل Agentهایی است که می‌توانند در آینده به نمونه‌کار، سرویس یا ابزار قابل ارائه به کسب‌وکارها تبدیل شوند.

| شماره | Agent | وضعیت | هدف |
|---|---|---|---|
| 01 | [GitHub Repo Analyzer Agent](./projects/github-repo-analyzer-agent) | آماده | تحلیل Repositoryهای GitHub و تولید گزارش فارسی |
| 02 | [Website Analyzer Agent](./projects/website-analyzer-agent) | آماده | تحلیل وب‌سایت و تولید گزارش فارسی کاربردی |
| 03 | [Document Analyzer Agent](./projects/document-analyzer-agent) | آماده | تحلیل سندهای متنی و تولید گزارش فارسی |
| 04 | [News Research Agent](./projects/news-research-agent) | آماده | تحقیق خبری و تولید گزارش فارسی ساختاریافته |
| 05 | [Content Research Agent](./projects/content-research-agent) | آماده | تحقیق موضوعی و ساخت Brief فارسی برای تولید محتوا |
---

## استاندارد هر Agent

هر Agent در این ریپو تا حد امکان شامل این بخش‌هاست:

* `README.md` — توضیح فارسی پروژه
* `main.py` — کد اصلی Agent
* `requirements.txt` — وابستگی‌های پروژه
* `.env.example` — نمونه تنظیمات محیطی
* `demo/sample-output.md` — نمونه خروجی قابل مشاهده
* خروجی محلی مثل `reports/` یا `memory.json` در GitHub ذخیره نمی‌شود

---

## اجرای پروژه‌ها

هر Agent به‌صورت جداگانه اجرا می‌شود.

ابتدا ریپو را Clone کنید:

```bash
git clone https://github.com/agenticroadmap/AI-Agent-Labs.git
```

بعد وارد پوشه Agent مورد نظر شوید.
مثلاً برای GitHub Repo Analyzer:

```bash
cd AI-Agent-Labs/projects/github-repo-analyzer-agent
pip install -r requirements.txt
python main.py
```

بعضی Agentها برای اجرا به API Key نیاز دارند.
نمونه تنظیمات در فایل `.env.example` هر پروژه قرار دارد.

---

## نکته امنیتی

هیچ‌وقت فایل‌های زیر را وارد GitHub نکنید:

```text
.env
memory.json
reports/
```

این فایل‌ها ممکن است شامل اطلاعات شخصی، API Key یا خروجی‌های محلی باشند.

---

## مسیر آینده

این ریپو به‌مرور تبدیل می‌شود به مجموعه‌ای از Agentهای عملی برای:

* یادگیری AI Agentها
* ساخت نمونه‌کار فنی
* تحلیل ابزارها و وب‌سایت‌ها
* تحقیق وبی و تولید گزارش
* آماده‌سازی خدمات آینده برای کسب‌وکارها

---

## لینک‌ها

* Website: https://agenticroadmap.ir
* X: https://x.com/agenticroadmap
* Telegram: https://t.me/agenticroadmap
* GitHub: https://github.com/agenticroadmap
  
