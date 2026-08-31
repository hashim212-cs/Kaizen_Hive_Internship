function_name = input("Function: ")
arguments = input("Arguments: ").split(",")

arguments = [argument.strip() for argument in arguments]

required_arguments = ["to", "subject", "body"]

if function_name == "send_email":
    for argument in required_arguments:
        if argument not in arguments:
            print("Missing Argument:", argument)
            break