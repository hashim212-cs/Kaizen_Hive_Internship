prompt = input("Enter your prompt: ")

words = prompt.split()
word_count = len(words)

print("Word Count:", word_count)

if word_count > 30:
    print("Prompt Too Long")
else:
    print("Prompt Accepted")