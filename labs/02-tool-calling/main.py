def extract_topic(question):
    words_to_remove = [
        "سختی", "یادگیری", "چقدر", "است", "؟", "?",
        "خلاصه", "درباره", "بده", "نوع", "چیست"
    ]

    topic = question
    for word in words_to_remove:
        topic = topic.replace(word, "")

    return topic.strip()


def learning_difficulty_tool(topic):
    scores = {
        "langgraph": 8,
        "crewai": 6,
        "autogen": 7,
        "rag": 6,
        "tool calling": 5,
        "memory": 5,
    }

    topic_key = topic.lower()

    for key, score in scores.items():
        if key in topic_key:
            return f"سطح سختی یادگیری {topic}: حدود {score} از 10 است."

    return f"برای {topic} هنوز امتیاز مشخصی نداریم، اما می‌توان آن را بررسی کرد."


def short_summary_tool(topic):
    return f"{topic} یکی از مفاهیم مهم در ساخت AI Agentهاست و باید با مثال عملی یاد گرفته شود."


def detect_topic_type_tool(topic):
    topic_key = topic.lower()

    if "langgraph" in topic_key or "crewai" in topic_key or "autogen" in topic_key:
        return f"{topic}: Framework"

    if "rag" in topic_key or "memory" in topic_key or "tool calling" in topic_key:
        return f"{topic}: Agent Concept"

    return f"{topic}: General AI Agent Topic"


def run_agent(question):
    topic = extract_topic(question)

    if "سختی" in question or "difficulty" in question.lower():
        return learning_difficulty_tool(topic)

    if "خلاصه" in question or "summary" in question.lower():
        return short_summary_tool(topic)

    if "نوع" in question or "type" in question.lower():
        return detect_topic_type_tool(topic)

    return "این Agent فعلاً سه ابزار دارد: سختی یادگیری، خلاصه‌سازی کوتاه، و تشخیص نوع موضوع."


if __name__ == "__main__":
    question = input("سؤال خود را بنویسید: ")
    answer = run_agent(question)

    print("\nپاسخ Agent:\n")
    print(answer)
