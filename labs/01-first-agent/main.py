from openai import OpenAI

client = OpenAI()

question = input("سؤال خود را بنویسید: ")

response = client.responses.create(
    model="gpt-4.1-mini",
    input=f"به زبان فارسی، ساده و کاربردی پاسخ بده:\n\n{question}"
)

print("\nپاسخ ایجنت:\n")
print(response.output_text)
