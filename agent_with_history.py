# agent_with_history.py
from research_agent import research_agent

print("Hello! I am your Deep Research Robot 🤖")
print("Type '/exit' when you want to stop.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "/exit":
        print("Robot: Bye! See you next time! 👋")
        break
    reply = research_agent(user_input)
    print("Robot:", reply)
