pref_input = input("Preference: ")
key, value = [x.strip() for x in pref_input.split('=')]
memory = {key: value}

print(f"Saved Preference: {key} = {memory[key]}")