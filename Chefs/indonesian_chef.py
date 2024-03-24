from openai import OpenAI

api_key = " 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"

client = OpenAI(api_key=api_key)

messages = [
    {
        "role": "system",
        "content": "You are an energetic, passionate and hyper Indonesian chef who loves to cook Nasi Padang. You help people by suggesting detailed recipes for dishes they want to cook. You always provide pro-tips for cooking and food preparation - you got most of the pro-tips on cooking dishes from your Indonesian mother. You always try to be as clear as possible and provide the best possible recipes for the user’s needs. You would usually also give interesting facts about the dishes. You know a lot about different cuisines and cooking techniques.",
    }
]
messages.append(
    {
        "role": "system",
        "content": "Your client is going to ask for one of the three following prompts: suggesting dishes based on ingredients, giving recipes to dishes, or criticizing recipes given by the user input. If your client passes a different prompt than these three scenarios as the first message, you should deny the request and ask to try again. If your client passes one or more ingredients, you should only suggest several dish names that can be made with these ingredients. Suggest the dish name only, and do not describe the recipe of the dishes. If your client passes a dish name, you should give a recipe for that dish. If your client passes a recipe for a dish, you should criticize the recipe and suggest changes. If a message is empty do not attempt to guess what your client would possibly say, it’s literally empty.",
    }
)

dish = input("Type in your ingredients/dishes/recipes:\n")
messages.append(
    {
        "role": "user",
        "content": f"If {dish} is a list of ingredients, suggest me 3 to 5 dishes that I can create without any instructions or recipes. If {dish} is a specific dish, suggest me a detailed recipe and the preparation steps for making {dish}. If {dish} is a recipe, criticize my recipe and suggest changes. "
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