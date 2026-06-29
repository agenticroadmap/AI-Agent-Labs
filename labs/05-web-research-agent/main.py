```python
from pathlib import Path
from openai import OpenAI

client = OpenAI()

REPORTS_DIR = Path("reports")
REPORT_FILE = REPORTS_DIR / "latest-report.md"


def generate_research_report(topic: str) -> str:
    prompt = f"""
تو یک Web Research Agent فارسی هستی.

وظیفه:
درباره موضوع زیر در وب تحقیق کن و یک گزارش فارسی، خلاصه، دقیق و ساختاریافته تولید کن.

موضوع:
{topic}

قالب خروجی:

# گزارش تحقیق وبی

## خلاصه سریع
در چند خط توضیح بده موضوع چیست و چرا مهم است.

## نکات مهم
- نکته ۱
- نکته ۲
- نکته ۳

## کاربردها
توضیح بده این موضوع در چه پروژه‌هایی کاربرد دارد.

## محدودیت‌ها یا ریسک‌ها
اگر محدودیت، ابهام یا ریسک مهمی وجود دارد، توضیح بده.

## جمع‌بندی
یک جمع‌بندی کوتاه و کاربردی بنویس.

قوانین:
- فارسی روان بنویس.
- از اغراق پرهیز کن.
- اگر اطلاعات قطعی نیست، شفاف بگو.
- خروجی را شبیه گزارش آماده انتشار بنویس.
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        tools=[
            {
                "type": "web_search",
                "search_context_size": "low"
            }
        ],
        input=prompt
    )

    return response.output_text


def save_report(report: str):
    REPORTS_DIR.mkdir(exist_ok=True)
    REPORT_FILE.write_text(report, encoding="utf-8")


def run_agent():
    topic = input("موضوع تحقیق را بنویسید: ")

    print("\nدر حال تحقیق در وب...\n")

    report = generate_research_report(topic)
    save_report(report)

    print("گزارش تولید شد:\n")
    print(report)

    print(f"\nفایل گزارش ذخیره شد در: {REPORT_FILE}")


if __name__ == "__main__":
    run_agent()
```
