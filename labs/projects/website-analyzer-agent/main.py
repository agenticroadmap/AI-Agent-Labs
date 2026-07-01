import re
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse

from openai import OpenAI

client = OpenAI()

REPORTS_DIR = Path("reports")
REPORT_FILE = REPORTS_DIR / "latest-report.md"


class WebsiteTextParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_script_or_style = False
        self.title = ""
        self.headings = []
        self.paragraphs = []
        self.current_tag = None
        self.current_text = []

    def handle_starttag(self, tag, attrs):
        if tag in ["script", "style", "noscript"]:
            self.in_script_or_style = True

        if tag in ["title", "h1", "h2", "h3", "p"]:
            self.current_tag = tag
            self.current_text = []

    def handle_endtag(self, tag):
        if tag in ["script", "style", "noscript"]:
            self.in_script_or_style = False

        if tag == self.current_tag:
            text = " ".join("".join(self.current_text).split())

            if text:
                if tag == "title":
                    self.title = text
                elif tag in ["h1", "h2", "h3"]:
                    self.headings.append(text)
                elif tag == "p":
                    self.paragraphs.append(text)

            self.current_tag = None
            self.current_text = []

    def handle_data(self, data):
        if not self.in_script_or_style and self.current_tag:
            self.current_text.append(data)


def validate_url(url: str) -> str:
    url = url.strip()

    if not url.startswith(("http://", "https://")):
        url = "https://" + url

    parsed = urlparse(url)

    if not parsed.netloc:
        raise ValueError("آدرس وب‌سایت معتبر نیست.")

    return url


def fetch_html(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 AgenticRoadmap-Website-Analyzer"
        },
    )

    with urllib.request.urlopen(request, timeout=15) as response:
        return response.read().decode("utf-8", errors="ignore")


def extract_website_content(html: str) -> dict:
    parser = WebsiteTextParser()
    parser.feed(html)

    text_blocks = parser.headings + parser.paragraphs
    page_text = "\n".join(text_blocks)

    page_text = re.sub(r"\n{3,}", "\n\n", page_text)
    page_text = page_text[:12000]

    return {
        "title": parser.title,
        "headings": parser.headings[:20],
        "paragraphs": parser.paragraphs[:30],
        "page_text": page_text,
    }


def generate_report(url: str, content: dict) -> str:
    prompt = f"""
تو یک Website Analyzer Agent فارسی هستی.

وظیفه:
یک وب‌سایت را بر اساس محتوای صفحه اصلی تحلیل کن و یک گزارش فارسی، خلاصه، کاربردی و تصمیم‌محور تولید کن.

Website URL:
{url}

Title:
{content["title"]}

Headings:
{content["headings"]}

Page Text:
{content["page_text"]}

قالب خروجی:

# گزارش تحلیل وب‌سایت

## خلاصه سریع
این سایت درباره چیست؟

## پیام اصلی سایت
پیام اصلی سایت چقدر واضح است؟

## مخاطب هدف
به نظر می‌رسد مخاطب اصلی سایت چه کسانی هستند؟

## نقاط قوت
چند نقطه قوت مهم سایت.

## ضعف‌ها یا ابهام‌ها
مواردی که ممکن است برای کاربر مبهم باشد.

## پیشنهادهای بهبود
پیشنهادهای عملی برای بهتر شدن محتوا، ساختار یا تبدیل کاربر.

## آمادگی برای تبدیل کاربر
آیا سایت کاربر را به اقدام مشخصی هدایت می‌کند؟

## جمع‌بندی
یک نتیجه کوتاه و کاربردی.

قوانین:
- فارسی روان بنویس.
- از اغراق پرهیز کن.
- اگر اطلاعات کافی نیست، شفاف بگو.
- فقط بر اساس محتوای استخراج‌شده تحلیل کن.
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
    website_url = input("آدرس وب‌سایت را وارد کنید: ")

    url = validate_url(website_url)

    print("\nدر حال خواندن صفحه اصلی سایت...\n")
    html = fetch_html(url)

    print("در حال استخراج محتوای سایت...\n")
    content = extract_website_content(html)

    print("در حال تولید گزارش فارسی...\n")
    report = generate_report(url, content)

    save_report(report)

    print("\nگزارش تولید شد:\n")
    print(report)

    print(f"\nفایل گزارش ذخیره شد در: {REPORT_FILE}")


if __name__ == "__main__":
    run_agent()
