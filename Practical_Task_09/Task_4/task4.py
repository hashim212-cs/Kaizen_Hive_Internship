actions_input = input("Actions enter karein: ")
actions = [a.strip() for a in actions_input.split(',')]

for action in actions:
    print(f"{action}: Done")