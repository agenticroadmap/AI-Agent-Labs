```python
from pathlib import Path
from openai import OpenAI

client = OpenAI()

REPORTS_DIR = Path("reports")
REPORT_FILE = REPORTS_DIR / "latest-report.md"


def read_document(file_path: str) -> str:
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError("فایل مورد نظر پیدا نشد.")

    if path.suffix.lower() not in [".txt", ".md"]:
        raise ValueError("در نسخه اولیه فقط فایل‌های .txt و .md پشتیبانی می‌شوند.")

    return path.read_text(encoding="utf-8")


def generate_report(document_text: str, file_path: str) -> str:
    prompt = f"""
تو یک Document Analyzer Agent فارسی هستی.

وظیفه:
متن سند زیر را تحلیل کن و یک گزارش فارسی، خلاصه، دقیق و کاربردی تولید کن.

نام فایل:
{file_path}

متن سند:
{document_text[:12000]}

قالب خروجی:

# گزارش تحلیل سند

## خلاصه سریع
سند درباره چیست؟

## موضوع اصلی
موضوع یا مسئله اصلی سند را توضیح بده.

## نکات کلیدی
- نکته ۱
- نکته ۲
- نکته ۳

## ریسک‌ها یا ابهام‌ها
اگر سند ریسک، ضعف، ابهام یا نکته حساس دارد، توضیح بده.

## پیشنهادهای عملی
چند پیشنهاد کاربردی بر اساس محتوای سند بده.

## ارزش کسب‌وکاری
توضیح بده این سند چه ارزشی برای یک کسب‌وکار یا تیم دارد.

## جمع‌بندی نهایی
یک جمع‌بندی کوتاه و تصمیم‌محور بنویس.

قوانین:
- فارسی روان بنویس.
- فقط بر اساس متن سند تحلیل کن.
- اگر اطلاعات کافی نبود، شفاف بگو.
- از اغراق و حدس قطعی پرهیز کن.
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
    )

    return response.output_text


def save_report(report: str):
    REPORTS_DIR.mkdir(exist_ok=True)
    REPORT_FILE.write_text(report, encoding="utf-8")


def run_agent():
    file_path = input("مسیر فایل سند را وارد کنید یا Enter بزنید برای نمونه پیش‌فرض: ").strip()

    if not file_path:
        file_path = "documents/sample.md"

    print("\nدر حال خواندن سند...\n")
    document_text = read_document(file_path)

    print("در حال تحلیل سند...\n")
    report = generate_report(document_text, file_path)

    save_report(report)

    print("\nگزارش تولید شد:\n")
    print(report)

    print(f"\nفایل گزارش ذخیره شد در: {REPORT_FILE}")


if __name__ == "__main__":
    run_agent()
```
