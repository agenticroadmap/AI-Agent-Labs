import json
from pathlib import Path
from openai import OpenAI

client = OpenAI()

MEMORY_FILE = Path("memory.json")


def load_memory():
    if not MEMORY_FILE.exists():
        return {}

    with open(MEMORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as file:
        json.dump(memory, file, ensure_ascii=False, indent=2)


def extract_memory_updates(user_message):
    prompt = f"""
از پیام کاربر فقط اطلاعات پایدار و مفید برای پاسخ‌های بعدی را استخراج کن.

قوانین:
- فقط اگر کاربر خودش چیزی درباره مهارت، هدف، ترجیح یا پروژه‌اش گفت ذخیره کن.
- اطلاعات کوتاه‌مدت یا بی‌ارزش را ذخیره نکن.
- اگر چیزی برای ذخیره نبود، خروجی خالی بده.
- فقط JSON معتبر برگردان.

فرمت خروجی:
{{
  "memory_updates": {{
    "python_level": "",
    "learning_goal": "",
    "project_goal": "",
    "preferred_language": ""
  }}
}}

پیام کاربر:
{user_message}
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt
    )

    text = response.output_text.strip()
    text = text.replace("```json", "").replace("```", "").strip()

    try:
        data = json.loads(text)
        updates = data.get("memory_updates", {})
        return {key: value for key, value in updates.items() if value}
    except json.JSONDecodeError:
        return {}


def generate_answer(user_message, memory):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": f"""
تو یک Memory Agent فارسی هستی.

وظیفه تو:
- پاسخ ساده، کاربردی و فارسی بده.
- اگر حافظه کاربر اطلاعات مفیدی دارد، از آن برای شخصی‌سازی پاسخ استفاده کن.
- چیزی را از خودت به حافظه نسبت نده.
- اگر حافظه خالی بود، عادی پاسخ بده.

حافظه فعلی کاربر:
{json.dumps(memory, ensure_ascii=False, indent=2)}
"""
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    return response.output_text


def run_agent():
    memory = load_memory()

    print("Memory Agent فعال شد.")
    print("برای خروج بنویسید: exit")

    while True:
        user_message = input("\nپیام شما: ")

        if user_message.lower() in ["exit", "quit"]:
            break

        updates = extract_memory_updates(user_message)

        if updates:
            memory.update(updates)
            save_memory(memory)
            print("\nحافظه به‌روزرسانی شد:")
            print(json.dumps(updates, ensure_ascii=False, indent=2))

        answer = generate_answer(user_message, memory)

        print("\nپاسخ Agent:\n")
        print(answer)


if __name__ == "__main__":
    run_agent()
