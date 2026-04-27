from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
print("API KEY:", os.getenv("OPENAI_API_KEY"))
def generate():
    prompt = "Придумай 5 вирусных идей видео для товара: держатель для телефона в авто"

    response = client.chat.completions.create(
        model="gpt-5",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


while True:
    ideas = generate()
    print("=== ИДЕИ ===")
    print(ideas)

    with open("ideas.txt", "a") as f:
        f.write(ideas + "\n\n")

    time.sleep(3600)
