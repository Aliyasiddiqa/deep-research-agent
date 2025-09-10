# research_agent.py

# pretend we have keys for Groq / Tavily (you can ignore money!)
GROQ_API_KEY = "free_stub"
TAVILY_API_KEY = "free_stub"

# where we save questions and answers
history = []

# pretend Groq answers
def query_groq(question):
    return f"[Groq says] I looked at your question: '{question}'"

# pretend Tavily gives info
def query_tavily(question):
    return f"[Tavily says] I found some info for: '{question}'"

# the robot brain that combines both
def research_agent(question):
    groq_answer = query_groq(question)
    tavily_answer = query_tavily(question)
    
    # combine answers
    answer = f"{tavily_answer}\n{groq_answer}"
    
    # remember history
    history.append({"question": question, "answer": answer})
    
    return answer
