current_state = input("Current State: ")
tool_result = input("Tool Result: ")

if tool_result.strip().lower() == "success":
    current_state = "completed"

print(f"Updated State: {current_state}")