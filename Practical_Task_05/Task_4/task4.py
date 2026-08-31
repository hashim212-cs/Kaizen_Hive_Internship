context = input("Context: ")

words = context.split()

limited_context = " ".join(words[:20])

print("Limited Context:", limited_context)