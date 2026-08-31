query = input("Enter query: ")

candidates = input("Enter three candidates separated by |: ").split("|")

query_words = set(query.lower().split())

best_sentence = ""
highest_count = 0

for sentence in candidates:
    sentence_words = set(sentence.lower().split())
    common_words = query_words.intersection(sentence_words)
    count = len(common_words)

    if count > highest_count:
        highest_count = count
        best_sentence = sentence.strip()

print("Most Similar Sentence:", best_sentence)