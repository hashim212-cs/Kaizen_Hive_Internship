context = input("Context: ")
keyword = input("Question Keyword: ")

if keyword.lower() in context.lower():
    print("Answer:", context)
else:
    print("Not found in context.")