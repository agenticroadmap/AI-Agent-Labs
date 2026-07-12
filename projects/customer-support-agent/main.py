```python
from pathlib import Path
from openai import OpenAI

client = OpenAI()

KNOWLEDGE_FILE = Path("knowledge/support.md")
REPLIES_DIR = Path("replies")
REPLY_FILE = REPLIES_DIR / "latest-reply.md"


def load_knowledge() -> str:
    if not KNOWLEDGE_FILE.exists():
        raise FileNotFoundError("فایل knowledge/support.md پیدا نشد.")

    return KNOWLEDGE_FILE.read_text(encoding="utf-8")


def split_knowledge(text: str):
    sections = text.split("## ")
    chunks = []

    for section in sections:
        section = section.strip()
        if section:
            chunks.append(section)

    return chunks


def retrieve_context(customer_message: str, chunks):
    message_words = set(customer_message.lower().split())
    scored_chunks = []

    for chunk in chunks:
        chunk_words = set(chunk.lower().split())
        score = len(message_words.intersection(chunk_words))
        scored_chunks.append((score, chunk))

    scored_chunks.sort(reverse=True, key=lambda item: item[0])

    top_chunks = [chunk for score, chunk in scored_chunks[:2] if score > 0]

    if not top_chunks:
        return "اطلاعات مرتبطی در فایل دانش پشتیبانی پیدا نشد."

    return "\n\n---\n\n".join(top_chunks)


def generate_support_reply(customer_message: str, context: str) -> str:
    prompt = f"""
تو یک Customer Support Agent فارسی هستی.

وظیفه:
بر اساس پیام مشتری و فایل دانش پشتیبانی، یک پاسخ فارسی، محترمانه و قابل ارسال تولید کن.

پیام مشتری:
{customer_message}

دانش پشتیبانی مرتبط:
{context}

قالب خروجی:

# پاسخ پیشنهادی پشتیبانی

## پاسخ به مشتری
متن آماده ارسال به مشتری را بنویس.

## مراحل پیشنهادی
اگر لازم است، مراحل را کوتاه و روشن بنویس.

## نیاز به بررسی انسانی
اگر موضوع نیاز به بررسی تیم انسانی دارد، واضح بگو.

قوانین:
- فارسی روان و محترمانه بنویس.
- فقط بر اساس دانش پشتیبانی پاسخ بده.
- اگر اطلاعات کافی نیست، حدس نزن.
- اگر نیاز به بررسی انسانی است، شفاف اعلام کن.
- پاسخ را کوتاه، کاربردی و آماده ارسال بنویس.
"""

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
    )

    return response.output_text


def save_reply(reply: str):
    REPLIES_DIR.mkdir(exist_ok=True)
    REPLY_FILE.write_text(reply, encoding="utf-8")


def run_agent():
    customer_message = input("پیام مشتری را وارد کنید: ")

    print("\nدر حال خواندن دانش پشتیبانی...\n")
    knowledge = load_knowledge()

    print("در حال پیدا کردن بخش مرتبط...\n")
    chunks = split_knowledge(knowledge)
    context = retrieve_context(customer_message, chunks)

    print("در حال تولید پاسخ پشتیبانی...\n")
    reply = generate_support_reply(customer_message, context)

    save_reply(reply)

    print("\nپاسخ پیشنهادی تولید شد:\n")
    print(reply)

    print(f"\nفایل پاسخ ذخیره شد در: {REPLY_FILE}")


if __name__ == "__main__":
    run_agent()
```
