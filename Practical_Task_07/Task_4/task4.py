steps = input("Steps: ").split(",")

steps = [step.strip() for step in steps]

if all(step == "completed" for step in steps):
    print("Goal Completed")
else:
    print("Goal In Progress")