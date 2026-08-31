memory_input = input("Memory: ")
requested_key = input("Requested Key: ").strip()

memory = {}
for item in memory_input.split(','):
    k, v = item.split('=')
    memory[k.strip()] = v.strip()

if requested_key in memory:
    print(f"{requested_key}: {memory[requested_key]}")
else:
    print("Memory Not Found")