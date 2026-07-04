# News Research Agent

چهارمین Business Agent در AgenticRoadmap Labs.

## هدف

این Agent یک موضوع خبری دریافت می‌کند، درباره آن تحقیق می‌کند و یک گزارش فارسی، خلاصه، ساختاریافته و کاربردی تولید می‌کند.

## این Agent چه کار می‌کند؟

```text
News Topic
↓
Web Search
↓
Source Review
↓
AI Agent
↓
Persian News Brief
```

## نمونه ورودی

```text
آخرین اخبار OpenAI Agents چیست؟
```

## خروجی مورد انتظار

Agent گزارشی تولید می‌کند شامل:

* خلاصه سریع خبر
* مهم‌ترین نکات
* چرا این خبر مهم است؟
* اثر احتمالی روی بازار یا صنعت
* ابهام‌ها و موارد نیازمند بررسی
* جمع‌بندی نهایی

## چرا این Agent مهم است؟

این Agent می‌تواند پایه یک سرویس واقعی برای رصد اخبار، تحلیل تحولات بازار، بررسی رقبا و تولید گزارش‌های کوتاه روزانه باشد.

## کاربردهای آینده

* رصد اخبار AI
* مانیتورینگ رقبا
* تولید گزارش خبری برای سایت یا X
* تحلیل روندهای بازار
* ساخت خبرنامه تخصصی

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
cd AI-Agent-Labs/projects/news-research-agent
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
demo/sample-output.md
