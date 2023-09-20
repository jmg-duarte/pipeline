import os

import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")


def summarize_news_item(news: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            # For this simple use case, this prompt is optional
            {
                "role": "system",
                "content": "You are an assistant, tasked with summarizing information.",
            },
            {
                "role": "user",
                "content": f"Please summarize the following news item: ```\n{news}\n```",
            },
        ],
    )
    return response["choices"][0]["message"]["content"]
