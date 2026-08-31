messages_input = input("Messages: ")
messages = [m.strip() for m in messages_input.split('|')]

user_count = sum(1 for msg in messages if msg.lower().startswith("user:"))
print(f"User Turns: {user_count}")