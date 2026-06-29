# 05 — Web Research Agent

پنجمین Agent عملی در AgenticRoadmap Labs.

## هدف

در این Lab یک Agent می‌سازیم که می‌تواند درباره یک موضوع در وب تحقیق کند و یک گزارش فارسی، خلاصه و ساختاریافته تولید کند.

## این Agent چه کار می‌کند؟

```text
User Topic
↓
Web Search
↓
Source Review
↓
AI Agent
↓
Structured Persian Report
```

## مثال

کاربر می‌پرسد:

```text
آخرین وضعیت LangGraph چیست؟
```

Agent در وب جستجو می‌کند و گزارشی شبیه این تولید می‌کند:

```text
خلاصه:
LangGraph یکی از فریم‌ورک‌های مهم برای ساخت Agentهای stateful و workflow-based است.

نکات مهم:
- مناسب برای workflowهای چندمرحله‌ای
- قابل استفاده در پروژه‌های Multi-Agent
- نیازمند درک بهتر از state و graph

جمع‌بندی:
برای پروژه‌های جدی Agent، گزینه قدرتمندی است؛ اما برای شروع ساده‌ترین انتخاب نیست.
```

## خروجی این Lab

این Agent یک گزارش ساختاریافته تولید می‌کند شامل:

* خلاصه موضوع
* نکات مهم
* کاربردها
* محدودیت‌ها
* جمع‌بندی نهایی

## اجرا روی سیستم شخصی

این پروژه روی خود GitHub اجرا نمی‌شود.
برای اجرا باید ریپو را روی سیستم خود Clone کنید:

```bash
git clone https://github.com/agenticroadmap/AI-Agent-Labs.git
cd AI-Agent-Labs/labs/05-web-research-agent
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

* Web Research
* Source Review
* Report Generation
* Research Agent
* Structured Output

## نکته

این Agent پایه ساخت پروژه‌های جدی‌تر مثل GitHub Repo Analyzer، News Agent و Market Research Agent است.
