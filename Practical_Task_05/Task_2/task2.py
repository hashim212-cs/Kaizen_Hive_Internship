context = input("Context: ")
question = input("Question: ")

prompt = (
    f"Context: {context}\n"
    f"Question: {question}\n"
    "Answer using only the given context."
)

print(prompt)