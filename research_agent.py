"""
research_agent.py
Handles research logic + history save/load
"""

import json

# global history list
history = []

def load_history():
    """Load history from file if it exists"""
    global history
    try:
        with open("history.json", "r", encoding="utf-8") as f:
            history = json.load(f)
        print(f"[Debug] History loaded with {len(history)} entries")
    except FileNotFoundError:
        history = []
        print("[Debug] No history.json found, starting fresh")
    return history   # 👈 return it

def save_history():
    """Save history to JSON file"""
    global history
    with open("history.json", "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4)
    print(f"[Debug] History saved with {len(history)} entries")

def research_agent(query: str) -> str:
    """Simulates Tavily + Groq research (stub version)"""
    global history
    groq_answer = f"[Groq says] I looked at your question: '{query}'"
    tavily_answer = f"[Tavily says] I found some info for: '{query}'"
    answer = f"{tavily_answer}\n{groq_answer}"

    # update history
    history.append({"question": query, "answer": answer})
    save_history()
    return answer





