```python
from pathlib import Path
from openai import OpenAI

client = OpenAI()

BRIEFS_DIR = Path("briefs")
BRIEF_FILE = BRIEFS_DIR / "latest-content-brief.md"


def generate_content_brief(topic: str) -> str:
    prompt = f"""
تو یک Content Research Agent فارسی هستی.

وظیفه:
درباره موضوع زیر تحقیق کن و یک brief فارسی برای تولید محتوا بساز.

موضوع:
{topic}

قالب خروجی:

# Content Brief

## خلاصه موضوع
موضوع را ساده و دقیق توضیح بده.

## مخاطب هدف
بگو این محتوا برای چه کسانی مناسب است.

## زاویه‌های محتوایی پیشنهادی
- زاویه ۱
- زاویه ۲
- زاویه ۳

## ایده‌های مقاله
- ایده مقاله ۱
- ایده مقاله ۲
- ایده مقاله ۳

## ایده‌های پست X
- پست ۱
- پست ۲
- پست ۳

## نکات کلیدی
- نکته ۱
- نکته ۲
- نکته ۳

## ساختار پیشنهادی محتوا
یک ساختار ساده برای مقاله یا پست بلند پیشنهاد بده.

## جمع‌بندی کاربردی
یک جمع‌بندی کوتاه و قابل استفاده بنویس.

قوانین:
- فارسی روان بنویس.
- برای مخاطب AgenticRoadmap بنویس.
- تبلیغاتی و اغراق‌آمیز ننویس.
- خروجی باید برای تولید مقاله، X thread یا ویدئوی کوتاه قابل استفاده باشد.
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        tools=[
            {
                "type": "web_search",
                "search_context_size": "low"
            }
        ],
        input=prompt,
    )

    return response.output_text


def save_brief(brief: str):
    BRIEFS_DIR.mkdir(exist_ok=True)
    BRIEF_FILE.write_text(brief, encoding="utf-8")


def run_agent():
    topic = input("موضوع محتوا را وارد کنید: ")

    print("\nدر حال تحقیق و ساخت Content Brief...\n")

    brief = generate_content_brief(topic)
    save_brief(brief)

    print("\nContent Brief تولید شد:\n")
    print(brief)

    print(f"\nفایل Brief ذخیره شد در: {BRIEF_FILE}")


if __name__ == "__main__":
    run_agent()
```
