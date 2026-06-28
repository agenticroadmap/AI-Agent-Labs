import json
from openai import OpenAI

client = OpenAI()


def learning_difficulty(topic: str) -> str:
    scores = {
        "LangGraph": 8,
        "CrewAI": 6,
        "AutoGen": 7,
        "RAG": 6,
        "Tool Calling": 5,
        "Memory": 5,
    }

    for name, score in scores.items():
        if name.lower() in topic.lower():
            return f"سطح سختی یادگیری {name} حدود {score} از 10 است."

    return f"برای {topic} هنوز امتیاز مشخصی ثبت نشده است."


def topic_summary(topic: str) -> str:
    return f"{topic} یکی از مفاهیم یا ابزارهای مهم در مسیر ساخت AI Agent است و باید با مثال عملی یاد گرفته شود."


def topic_type(topic: str) -> str:
    framework_keywords = ["langgraph", "crewai", "autogen"]
    concept_keywords = ["rag", "memory", "tool calling"]

    key = topic.lower()

    if any(word in key for word in framework_keywords):
        return "Framework"

    if any(word in key for word in concept_keywords):
        return "Agent Concept"

    return "General AI Agent Topic"


tools = [
    {
        "type": "function",
        "name": "learning_difficulty",
        "description": "بررسی سطح سختی یادگیری یک موضوع یا ابزار AI Agent.",
        "parameters": {
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "نام موضوع یا ابزار، مثل LangGraph یا RAG"
                }
            },
            "required": ["topic"],
            "additionalProperties": False
        },
        "strict": True
    },
    {
        "type": "function",
        "name": "topic_summary",
        "description": "تولید خلاصه کوتاه درباره یک موضوع AI Agent.",
        "parameters": {
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "نام موضوع یا ابزار"
                }
            },
            "required": ["topic"],
            "additionalProperties": False
        },
        "strict": True
    },
    {
        "type": "function",
        "name": "topic_type",
        "description": "تشخیص نوع موضوع: Framework، مفهوم ایجنتی یا موضوع عمومی.",
        "parameters": {
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "نام موضوع یا ابزار"
                }
            },
            "required": ["topic"],
            "additionalProperties": False
        },
        "strict": True
    }
]


available_tools = {
    "learning_difficulty": learning_difficulty,
    "topic_summary": topic_summary,
    "topic_type": topic_type,
}


def run_agent(question: str) -> str:
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=[
            {
                "role": "system",
                "content": "تو یک Agent فارسی برای آموزش عملی AI Agentها هستی. اگر برای پاسخ بهتر نیاز بود، از ابزارهای موجود استفاده کن."
            },
            {
                "role": "user",
                "content": question
            }
        ],
        tools=tools
    )

    tool_outputs = []

    for item in response.output:
        if item.type == "function_call":
            function_name = item.name
            arguments = json.loads(item.arguments)

            tool_result = available_tools[function_name](**arguments)

            tool_outputs.append({
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": tool_result
            })

    if not tool_outputs:
        return response.output_text

    final_response = client.responses.create(
        model="gpt-4.1-mini",
        previous_response_id=response.id,
        input=tool_outputs
    )

    return final_response.output_text


if __name__ == "__main__":
    question = input("سؤال خود را بنویسید: ")
    answer = run_agent(question)

    print("\nپاسخ Agent:\n")
    print(answer)
