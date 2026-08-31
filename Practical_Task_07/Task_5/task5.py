plan_step = input("Plan Step: ")

tools_map = {
    "search": "Search Tool",
    "calculate": "Calculator Tool",
    "write": "Writing Tool"
}

required_tool = "Unknown Tool"
for keyword, tool in tools_map.items():
    if keyword in plan_step.lower():
        required_tool = tool
        break

print(f"Required Tool: {required_tool}")