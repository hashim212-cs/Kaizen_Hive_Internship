text = input("Enter text: ")

formal_words = {
    "good": "effective",
    "bad": "ineffective",
    "big": "significant"
}

for informal, formal in formal_words.items():
    text = text.replace(informal, formal)

print("Formal Text:", text)