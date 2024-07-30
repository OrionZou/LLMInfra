from openai import OpenAI


client = OpenAI(
    base_url="http://localhost:15000/v1",
    api_key="token-abc123",
)

completion = client.chat.completions.create(
  model="/models/openbuddy",
  messages=[
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)