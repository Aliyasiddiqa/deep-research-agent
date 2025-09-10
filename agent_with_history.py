from research_agent import research_agent, load_history

def main():
    history = load_history()  # 👈 store the returned history
    print(f"[Debug] Loaded {len(history)} past entries from history.json (inside agent_with_history.py)")

    print("Hello! I am your Deep Research Robot 🤖")
    print("Type '/exit' to quit.")
    print("Type '/history' to see past questions.")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == "/exit":
            print("Robot: Goodbye!")
            break
        elif user_input.lower() == "/history":
            if not history:
                print("Robot: No history yet.")
            else:
                print("Robot: Here is your past history:")
                for i, item in enumerate(history, 1):
                    print(f"{i}. Q: {item['question']} | A: {item['answer']}")
        else:
            reply = research_agent(user_input)
            print("Robot:", reply)
            history = load_history()  # 👈 reload after every new question

if __name__ == "__main__":
    main()





