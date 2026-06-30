# GitHub Repo Analyzer Agent

اولین Business Agent در AgenticRoadmap Labs.

## هدف

این Agent یک لینک GitHub دریافت می‌کند و درباره آن Repository یک گزارش فارسی، ساختاریافته و کاربردی تولید می‌کند.

## این Agent چه کار می‌کند؟

```text
GitHub Repository URL
↓
Read Repository Data
↓
Analyze README and Metadata
↓
AI Agent
↓
Persian Repository Report
```

## نمونه ورودی

```text
https://github.com/langchain-ai/langgraph
```

## خروجی مورد انتظار

Agent گزارشی تولید می‌کند شامل:

* این پروژه چیست؟
* برای چه کاری مناسب است؟
* سطح سختی یادگیری چقدر است؟
* نقاط قوت چیست؟
* محدودیت‌ها چیست؟
* آیا برای AgenticRoadmap ارزش بررسی دارد؟
* پیشنهاد استفاده عملی چیست؟

## چرا این Agent مهم است؟

این پروژه فقط یک تمرین نیست.
این Agent می‌تواند به مرور برای تحلیل ابزارها، فریم‌ورک‌ها و پروژه‌های متن‌باز حوزه AI Agent استفاده شود.

## کاربردهای آینده

* تحلیل GitHub پروژه‌های AI Agent
* تولید گزارش اولیه برای سایت AgenticRoadmap
* بررسی ابزارهای جدید
* کمک به تولید محتوای X
* ساخت نمونه‌کار فنی برای خدمات آینده

## فایل‌های این پروژه

```text
main.py
requirements.txt
.env.example
reports/
demo/sample-output.md
```

## اجرا روی سیستم شخصی

این پروژه روی خود GitHub اجرا نمی‌شود.
برای اجرا باید ریپو را روی سیستم خود Clone کنید:

```bash
git clone https://github.com/agenticroadmap/AI-Agent-Labs.git
cd AI-Agent-Labs/projects/github-repo-analyzer-agent
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
## Demo

نمونه خروجی این Agent را می‌توانید اینجا ببینید:

```text
demo/sample-output.md.
