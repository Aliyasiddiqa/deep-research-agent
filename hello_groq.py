import os
from groq import Groq
from dotenv import load_dotenv

# Load API keys from .env
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

response = client.chat.completions.create(
    model="mixtral-8x7b-32768",
    messages=[{"role": "user", "content": "Hello Robot, who are you?"}]
)

print(response.choices[0].message.content)
