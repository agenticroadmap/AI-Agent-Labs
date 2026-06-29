# 04 — RAG Agent

چهارمین Agent عملی در AgenticRoadmap Labs.

## هدف

در این Lab یک Agent می‌سازیم که به‌جای پاسخ دادن فقط بر اساس دانش مدل، از فایل‌های داخل پروژه استفاده می‌کند.

## این Agent چه کار می‌کند؟

```text
User Question
↓
Search Local Documents
↓
Find Relevant Context
↓
AI Agent
↓
Answer Based on Documents
```

## مثال

داخل پروژه یک فایل داریم:

```text
docs/knowledge.md
```

کاربر می‌پرسد:

```text
LangGraph برای چه پروژه‌هایی مناسب است؟
```

Agent ابتدا داخل فایل جستجو می‌کند، بخش مرتبط را پیدا می‌کند و بعد پاسخ فارسی می‌سازد.

## فایل‌های این Lab

```text
main.py
requirements.txt
.env.example
docs/knowledge.md
demo/sample-output.md
```

## اجرا روی سیستم شخصی

این پروژه روی خود GitHub اجرا نمی‌شود.
برای اجرا باید ریپو را روی سیستم خود Clone کنید:

```bash
git clone https://github.com/agenticroadmap/AI-Agent-Labs.git
cd AI-Agent-Labs/labs/04-rag-agent
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

## مفاهیم این Lab

* RAG
* Local Knowledge Base
* Document Search
* Context Injection
* Answer Based on Source

## نکته

این Agent یک نمونه ساده اما واقعی از RAG است.
هدف آن نشان دادن این است که Agent چگونه می‌تواند با کمک فایل‌های اختصاصی، پاسخ دقیق‌تر و قابل‌اعتمادتر تولید کند.
