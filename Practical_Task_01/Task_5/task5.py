prompt = input("Enter your prompt: ")

action_words = [
    "explain",
    "summarize",
    "classify",
    "generate",
    "rewrite",
    "compare"
]

prompt = prompt.lower()

if any(word in prompt for word in action_words):
    print("Clear Prompt")
else:
    print("Unclear Prompt")