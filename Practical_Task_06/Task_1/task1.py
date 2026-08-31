request = input("User Request: ").lower()

if "weather" in request:
    print("Selected Tool: Weather Tool")
elif "calculate" in request:
    print("Selected Tool: Calculator Tool")
else:
    print("Selected Tool: General Chat Tool")