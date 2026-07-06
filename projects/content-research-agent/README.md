# Content Research Agent

پنجمین Business Agent در AgenticRoadmap Labs.

## هدف

این Agent یک موضوع دریافت می‌کند، درباره آن تحقیق می‌کند و یک گزارش فارسی برای تولید محتوا می‌سازد.

## این Agent چه کار می‌کند؟

```text
Content Topic
↓
Research
↓
Audience Analysis
↓
Content Angles
↓
AI Agent
↓
Persian Content Brief
```

## نمونه ورودی

```text
Tool Calling در AI Agentها
```

## خروجی مورد انتظار

Agent گزارشی تولید می‌کند شامل:

* خلاصه موضوع
* مخاطب هدف
* زاویه‌های مناسب برای محتوا
* ایده‌های مقاله
* ایده‌های پست X
* نکات کلیدی
* پیشنهاد ساختار محتوا
* جمع‌بندی کاربردی

## چرا این Agent مهم است؟

این Agent می‌تواند به تولید محتوای منظم برای AgenticRoadmap کمک کند؛ از مقاله سایت تا پست X و ایده‌های آموزشی.

## کاربردهای آینده

* تحقیق برای مقاله‌های سایت
* ایده‌سازی برای X
* ساخت brief محتوایی
* کمک به تولید تقویم محتوا
* تبدیل موضوعات فنی به محتوای قابل فهم

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
cd AI-Agent-Labs/projects/content-research-agent
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
