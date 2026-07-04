from pathlib import Path
from openai import OpenAI

client = OpenAI()

REPORTS_DIR = Path("reports")
REPORT_FILE = REPORTS_DIR / "latest-news-brief.md"


def generate_news_brief(topic: str) -> str:
    prompt = f"""
تو یک News Research Agent فارسی هستی.

وظیفه:
درباره موضوع خبری زیر در وب تحقیق کن و یک گزارش فارسی، خلاصه، دقیق و ساختاریافته تولید کن.

موضوع خبری:
{topic}

قالب خروجی:

# گزارش خبری

## خلاصه سریع
خبر یا موضوع اصلی چیست؟

## مهم‌ترین نکات
- نکته ۱
- نکته ۲
- نکته ۳

## چرا مهم است؟
توضیح بده این خبر برای صنعت، بازار، کاربران یا سازندگان چه اهمیتی دارد.

## اثر احتمالی
اثر احتمالی این خبر روی کسب‌وکارها، ابزارها، کاربران یا روند بازار را توضیح بده.

## ابهام‌ها یا موارد نیازمند بررسی
اگر اطلاعات هنوز قطعی نیست یا نیاز به بررسی بیشتر دارد، شفاف بگو.

## جمع‌بندی نهایی
یک جمع‌بندی کوتاه و تصمیم‌محور بنویس.

قوانین:
- فارسی روان بنویس.
- از اغراق و تیترسازی زرد پرهیز کن.
- اگر اطلاعات قطعی نیست، شفاف بگو.
- خروجی را شبیه یک brief آماده انتشار بنویس.
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


def save_report(report: str):
    REPORTS_DIR.mkdir(exist_ok=True)
    REPORT_FILE.write_text(report, encoding="utf-8")


def run_agent():
    topic = input("موضوع خبری را وارد کنید: ")

    print("\nدر حال تحقیق خبری در وب...\n")

    report = generate_news_brief(topic)
    save_report(report)

    print("\nگزارش خبری تولید شد:\n")
    print(report)

    print(f"\nفایل گزارش ذخیره شد در: {REPORT_FILE}")


if __name__ == "__main__":
    run_agent()
