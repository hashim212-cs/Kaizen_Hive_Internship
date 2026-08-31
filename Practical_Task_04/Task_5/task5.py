keyword = input("Enter keyword: ")

documents = input("Enter documents separated by |: ").split("|")

retrieved_document = "No document found."

for document in documents:
    if keyword.lower() in document.lower():
        retrieved_document = document.strip()
        break

print("Retrieved Document:", retrieved_document)