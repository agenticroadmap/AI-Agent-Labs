# 03 — Memory Agent

سومین Agent عملی در AgenticRoadmap Labs.

## هدف

در این Lab یک Agent می‌سازیم که می‌تواند اطلاعات مهم کاربر را ذخیره کند و در پاسخ‌های بعدی از آن استفاده کند.

## این Agent چه کار می‌کند؟

```text
User Message
↓
Memory Extraction
↓
Local Memory Update
↓
Personalized AI Response
```

## مثال

کاربر ابتدا می‌گوید:

```text
من Python را در سطح متوسط بلدم و می‌خواهم ساخت AI Agent را یاد بگیرم.
```

Agent این اطلاعات را در حافظه ذخیره می‌کند:

```json
{
  "python_level": "متوسط",
  "learning_goal": "یادگیری ساخت AI Agent"
}
```

بعد کاربر می‌پرسد:

```text
برای یادگیری LangGraph از کجا شروع کنم؟
```

Agent پاسخ را با توجه به حافظه قبلی شخصی‌سازی می‌کند.

## حافظه در این Lab

در این نسخه، حافظه در یک فایل محلی ذخیره می‌شود:

```text
memory.json
```

این فایل نباید وارد GitHub شود و در `.gitignore` قرار گرفته است.

## اجرا روی سیستم شخصی

این پروژه روی خود GitHub اجرا نمی‌شود.
برای اجرا باید ریپو را روی سیستم خود Clone کنید:

```bash
git clone https://github.com/agenticroadmap/AI-Agent-Labs.git
cd AI-Agent-Labs/labs/03-memory-agent
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

## فایل‌ها

```text
main.py
requirements.txt
.env.example
demo/sample-output.md
```

## مفاهیم این Lab

* Memory
* User Profile
* Context
* Personalization
* Local JSON Storage

## نکته

این Agent یک نمونه ساده اما واقعی از حافظه در Agentهاست.
هدف آن نشان دادن این است که Agent چگونه می‌تواند از اطلاعات قبلی برای پاسخ بهتر استفاده کند.
