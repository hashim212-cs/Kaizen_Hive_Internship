question = input("Question: ")

passages = input("Passages separated by |: ").split("|")

question_words = question.lower().split()

retrieved_context = "No relevant context found."

for passage in passages:
    passage_lower = passage.lower()

    for word in question_words:
        if word in passage_lower and len(word) > 3:
            retrieved_context = passage.strip()
            break

    if retrieved_context != "No relevant context found.":
        break

print("Retrieved Context:", retrieved_context)