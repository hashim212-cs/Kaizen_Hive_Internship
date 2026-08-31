actions = input("Actions: ").split(",")

for number, action in enumerate(actions, start=1):
    print(f"{number}. {action.strip()}")