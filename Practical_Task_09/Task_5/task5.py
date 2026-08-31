actions_input = input("Actions enter karein: ")
actions = [a.strip() for a in actions_input.split(',')]

for action in actions:
    if action.lower() == "finish":
        print(f"Stopped at: {action}")
        break