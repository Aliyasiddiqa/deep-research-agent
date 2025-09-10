"""
Deep_Research_Agent
Simple skeleton with input loop + placeholders
"""

from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def research_agent(query: str) -> str:
    """
    Placeholder for research logic.
    On Day 1, just echo back.
    """
    return f"[Stub Response] You asked: {query}"

def main():
    print("Welcome to Deep Research Agent (Day 1)!")
    print("Type '/exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "/exit":
            print("Agent: Goodbye!")
            break
        print("Agent:", research_agent(user_input))

if __name__ == "__main__":
    main()
