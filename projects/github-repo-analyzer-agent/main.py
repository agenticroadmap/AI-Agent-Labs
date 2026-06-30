```python
import base64
import json
import re
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

from openai import OpenAI

client = OpenAI()

REPORTS_DIR = Path("reports")
REPORT_FILE = REPORTS_DIR / "latest-report.md"


def parse_github_url(url: str):
    parsed = urlparse(url.strip())
    parts = parsed.path.strip("/").replace(".git", "").split("/")

    if parsed.netloc != "github.com" or len(parts) < 2:
        raise ValueError("لینک GitHub معتبر نیست.")

    return parts[0], parts[1]


def github_api_get(path: str):
    request = urllib.request.Request(
        f"https://api.github.com{path}",
        headers={
            "Accept": "application/vnd.github+json",
            "User-Agent": "AgenticRoadmap-Repo-Analyzer",
        },
    )

    with urllib.request.urlopen(request) as response:
        return json.loads(response.read().decode("utf-8"))


def fetch_repo_metadata(owner: str, repo: str):
    data = github_api_get(f"/repos/{owner}/{repo}")

    return {
        "name": data.get("name"),
        "full_name": data.get("full_name"),
        "description": data.get("description"),
        "stars": data.get("stargazers_count"),
        "forks": data.get("forks_count"),
        "open_issues": data.get("open_issues_count"),
        "language": data.get("language"),
        "topics": data.get("topics", []),
        "license": data.get("license", {}).get("name") if data.get("license") else None,
        "homepage": data.get("homepage"),
        "created_at": data.get("created_at"),
        "updated_at": data.get("updated_at"),
    }


def fetch_readme(owner: str, repo: str):
    try:
        data = github_api_get(f"/repos/{owner}/{repo}/readme")
        content = base64.b64decode(data["content"]).decode("utf-8", errors="ignore")
        return content
    except Exception:
        return "README پیدا نشد."


def clean_text(text: str, max_chars: int = 12000):
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text[:max_chars]


def generate_report(repo_url: str, metadata: dict, readme: str):
    prompt = f"""
تو یک GitHub Repo Analyzer Agent فارسی هستی.

وظیفه:
یک Repository گیت‌هاب را برای مخاطب فارسی‌زبان تحلیل کن.
تحلیل باید کاربردی، خلاصه، دقیق و مناسب AgenticRoadmap باشد.

لینک Repository:
{repo_url}

Metadata:
{json.dumps(metadata, ensure_ascii=False, indent=2)}

README:
{clean_text(readme)}

قالب خروجی:

# گزارش تحلیل Repository

## خلاصه سریع
این پروژه چیست و در یک نگاه چه ارزشی دارد؟

## این پروژه چه کاری انجام می‌دهد؟
توضیح ساده و کاربردی.

## دسته‌بندی پروژه
مشخص کن این پروژه بیشتر به کدام دسته نزدیک است:
- Agent Framework
- Agent Tool
- AI Application
- RAG Tool
- Multi-Agent Framework
- Developer Tool
- Other

## سیگنال‌های GitHub
بر اساس metadata توضیح بده:
- Stars
- Forks
- زبان اصلی
- وضعیت به‌روزرسانی
- موضوعات/Topics

## نقاط قوت
چند مورد مهم.

## محدودیت‌ها یا ریسک‌ها
چند مورد واقعی و بدون اغراق.

## سطح سختی یادگیری
از 1 تا 10 امتیاز بده و دلیل کوتاه بنویس.

## مناسب چه کسانی است؟
برای چه نوع کاربر یا تیمی مناسب است؟

## ارزش بررسی برای AgenticRoadmap
بگو آیا ارزش دارد در AgenticRoadmap بررسی شود یا نه.

## جمع‌بندی نهایی
یک نتیجه کوتاه و تصمیم‌محور.

قوانین:
- فارسی روان بنویس.
- تبلیغاتی ننویس.
- اگر اطلاعات کافی نبود، شفاف بگو.
- از حدس‌های قطعی پرهیز کن.
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
    repo_url = input("لینک Repository گیت‌هاب را وارد کنید: ")

    owner, repo = parse_github_url(repo_url)

    print("\nدر حال خواندن اطلاعات Repository...\n")
    metadata = fetch_repo_metadata(owner, repo)

    print("در حال خواندن README...\n")
    readme = fetch_readme(owner, repo)

    print("در حال تولید گزارش فارسی...\n")
    report = generate_report(repo_url, metadata, readme)

    save_report(report)

    print("\nگزارش تولید شد:\n")
    print(report)

    print(f"\nفایل گزارش ذخیره شد در: {REPORT_FILE}")


if __name__ == "__main__":
    run_agent()
```
