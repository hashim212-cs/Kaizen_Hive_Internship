question = input("Question: ").lower()

if "price" in question:
    print("Pricing information is available.")
elif "support" in question:
    print("Support is available by email.")
else:
    print("Sorry, I do not have an answer for that question.")