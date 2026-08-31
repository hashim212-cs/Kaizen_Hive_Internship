steps = [
    ("Step1", "completed"),
    ("Step2", "pending"),
    ("Step3", "pending")
]

for step, status in steps:
    if status == "pending":
        print("Next Action:", step)
        break