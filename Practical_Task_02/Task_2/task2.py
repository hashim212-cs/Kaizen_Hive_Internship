text = input("Enter text: ")
keyword = input("Enter keyword: ")

sentences = text.split(".")

for sentence in sentences:
    if keyword.lower() in sentence.lower():
        print(sentence.strip() + ".")