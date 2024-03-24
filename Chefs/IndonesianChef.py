from openai import OpenAI

api_key = " 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"

client = OpenAI(api_key=api_key)

messages = [
    {
        "role": "system",
        "content": "You are an experienced Indonesian chef who loves to cook Nasi Padang. You help people by suggesting detailed recipes for dishes they want to cook. You always provide pro-tips for cooking and food preparation - you got most of the pro-tips on cooking dishes from your Indonesian mother. You always try to be as clear as possible and provide the best possible recipes for the user’s needs. You’re an energetic person to be around and you would usually also give interesting facts about the dishes. You know a lot about different cuisines and cooking techniques.",
    }
]
messages.append(
    {
        "role": "system",
        "content": "Your client is going to ask for a recipe about a specific dish. If you do not recognize the dish, you should not try to generate a recipe for it. Do not answer a recipe if you do not understand the name of the dish. If you know the dish, you must answer directly with a detailed recipe for it. If you don't know the dish, you should answer that you don't know the dish and end the conversation.",
    }
)

dish = input("Type the name of the dish you want a recipe for:\n")
messages.append(
    {
        "role": "user",
        "content": f"Suggest me a detailed recipe and the preparation steps for making {dish}"
    }
)

model = "gpt-3.5-turbo"

stream = client.chat.completions.create(
    model=model,
    messages=messages,
    stream=True,
)

collected_messages = []
for chunk in stream:
    chunk_message = chunk.choices[0].delta.content or ""
    print(chunk_message, end="")
    collected_messages.append(chunk_message)

messages.append(
    {
        "role": "system",
        "content": "".join(collected_messages)
    }
)

while True:
    print("\n")
    user_input = input()
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )
    stream = client.chat.completions.create(
        model=model,
        messages=messages,
        stream=True,
    )
    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)

    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )