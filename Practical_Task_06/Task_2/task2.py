import json

a = int(input("a: "))
b = int(input("b: "))

function_call = {
    "function": "add_numbers",
    "arguments": {
        "a": a,
        "b": b
    }
}

print(json.dumps(function_call))