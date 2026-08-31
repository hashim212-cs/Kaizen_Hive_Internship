facts_input = input("Facts: ")
facts = [f.strip() for f in facts_input.split(',')]

f1 = facts[0]
f2 = facts[1].replace("User ", "").replace("user ", "")
f3 = facts[2].replace("User ", "").replace("user ", "")

print(f"Memory Summary: {f1}, {f2}, and {f3}.")