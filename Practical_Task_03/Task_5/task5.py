message = input("User Message: ").lower()

if "hello" in message or "hi" in message or "salam" in message:
    print("Intent: greeting")
    print("Response: Hello! How can I help you?")

elif "thank" in message:
    print("Intent: thanks")
    print("Response: You are welcome!")

elif "help" in message:
    print("Intent: help")
    print("Response: Sure! How can I help you?")

else:
    print("Intent: unknown")
    print("Response: Sorry, I did not understand your request.")