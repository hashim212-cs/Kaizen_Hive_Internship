action = input("Action: ").lower()

if action == "send_email" or action == "delete_file":
    print("Confirmation Required")
else:
    print("Safe to Execute")