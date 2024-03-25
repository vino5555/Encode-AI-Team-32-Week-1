from openai import OpenAI
import os

class Chef:
  def __init__(self, firstPrompt, secondPrompt):
    self.messages = [
        {
            "role": "system",
            "content": firstPrompt,
        }
    ]

    self.messages.append(
        {
            "role": "system",
            "content": secondPrompt,
        }
    )

  def listen(self):
    api_key = os.environ.get('OPENAI_API_KEY')
    client = OpenAI(api_key=api_key)

    dish = input("Type in a few ingredients, the name of a dish, or your own recipe:\n")
    self.messages.append(
        {
            "role": "user",
            "content": f"If {dish} is a list of ingredients, suggest me 3 to 5 dishes that I can create without any instructions or recipes. If {dish} is a specific dish, suggest me a detailed recipe and the preparation steps for making {dish}. If {dish} is a recipe, criticize my recipe and suggest changes. "
        }
    )

    model = "gpt-3.5-turbo"

    stream = client.chat.completions.create(
        model=model,
        messages=self.messages,
        stream=True,
    )

    collected_messages = []
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)

    self.messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )

    while True:
        print("\n")
        user_input = input()
        self.messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )
        stream = client.chat.completions.create(
            model=model,
            messages=self.messages,
            stream=True,
        )
        collected_messages = []
        for chunk in stream:
            chunk_message = chunk.choices[0].delta.content or ""
            print(chunk_message, end="")
            collected_messages.append(chunk_message)

        self.messages.append(
            {
                "role": "system",
                "content": "".join(collected_messages)
            }
        )