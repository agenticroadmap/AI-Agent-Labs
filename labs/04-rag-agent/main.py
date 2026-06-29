from pathlib import Path
from openai import OpenAI

client = OpenAI()

KNOWLEDGE_FILE = Path("docs/knowledge.md")


def load_knowledge():
    if not KNOWLEDGE_FILE.exists():
        raise FileNotFoundError("فایل docs/knowledge.md پیدا نشد.")

    return KNOWLEDGE_FILE.read_text(encoding="utf-8")


def split_into_chunks(text):
    sections = text.split("## ")
    chunks = []

    for section in sections:
        section = section.strip()
        if section:
            chunks.append(section)

    return chunks


def retrieve_relevant_context(question, chunks):
    question_words = set(question.lower().split())

    scored_chunks = []

    for chunk in chunks:
        chunk_words = set(chunk.lower().split())
        score = len(question_words.intersection(chunk_words))
        scored_chunks.append((score, chunk))

    scored_chunks.sort(reverse=True, key=lambda item: item[0])

    top_chunks = [chunk for score, chunk in scored_chunks[:2] if score > 0]

    if not top_chunks:
        return chunks[0]

    return "\n\n---\n\n".join(top_chunks)


def generate_answer(question, context):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": """
تو یک RAG Agent فارسی هستی.

قوانین:
- فقط بر اساس Context پاسخ بده.
- اگر جواب در Context نبود، صادقانه بگو در فایل دانش موجود نیست.
- پاسخ کوتاه، روشن و کاربردی باشد.
- از حدس زدن خودداری کن.
"""
            },
            {
                "role": "user",
                "content": f"""
سؤال کاربر:
{question}

Context:
{context}
"""
            }
        ]
    )

    return response.output_text


def run_agent():
    knowledge = load_knowledge()
    chunks = split_into_chunks(knowledge)

    question = input("سؤال خود را بنویسید: ")

    context = retrieve_relevant_context(question, chunks)
    answer = generate_answer(question, context)

    print("\nContext استفاده‌شده:\n")
    print(context)

    print("\nپاسخ Agent:\n")
    print(answer)


if __name__ == "__main__":
    run_agent()
