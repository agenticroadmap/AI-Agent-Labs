# 02 — Tool Calling Agent

دومین Agent عملی در AgenticRoadmap Labs.

## هدف

در این Lab یک Agent می‌سازیم که فقط پاسخ متنی نمی‌دهد؛ بلکه می‌تواند بر اساس سؤال کاربر، ابزار مناسب را انتخاب و اجرا کند.

## این Agent چه کار می‌کند؟

```text
User Question
↓
AI Agent
↓
Tool Selection
↓
Tool Execution
↓
Final Persian Answer
```

## ابزارهای Agent

این Agent سه ابزار دارد:

* `learning_difficulty` — بررسی سختی یادگیری یک موضوع
* `topic_summary` — تولید خلاصه کوتاه درباره یک موضوع
* `topic_type` — تشخیص نوع موضوع

## نمونه سؤال‌ها

```text
سختی یادگیری LangGraph چقدر است؟
```

```text
یک خلاصه کوتاه درباره RAG بده
```

```text
نوع CrewAI چیست؟
```

## اجرا روی سیستم شخصی

این پروژه روی خود GitHub اجرا نمی‌شود.
برای اجرا باید ریپو را روی سیستم خود Clone کنید:

```bash
git clone https://github.com/agenticroadmap/AI-Agent-Labs.git
cd AI-Agent-Labs/labs/02-tool-calling
pip install -r requirements.txt
```

سپس کلید API را در سیستم تنظیم کنید:

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

* Tool Calling
* Function Calling
* Agent Decision
* Tool Execution
* Final Response

## نکته

این Agent یک نمونه ساده اما واقعی از Tool Calling است.
در اینجا مدل زبانی تصمیم می‌گیرد کدام ابزار باید اجرا شود.
