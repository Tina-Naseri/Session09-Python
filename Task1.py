def separator():
    print()
    print("------------------------------------------")


def sum(f1, f2):
    result = {}
    result["s"] = (f1["s"] * f2["m"]) + (f2["s"] * f1["m"])
    result["m"] = f1["m"] * f2["m"]
    print(f"                 {f1['s']}     {f2['s']}     {result['s']}")
    print(" ---> Addition: ___ + ___ = _____")
    print(f"                 {f1['m']}     {f2['m']}     {result['m']}")
    if result['s'] == result['m']:
        print(" = 1")
    elif result['s'] == 0:
        print(' = 0')
    separator()
    return result


def difference(f1, f2):
    result = {}
    result["s"] = (f1["s"] * f2["m"]) - (f2["s"] * f1["m"])
    result["m"] = f1["m"] * f2["m"]
    print(f"                    {f1['s']}     {f2['s']}     {result['s']}")
    print(" ---> Subtraction: ___ - ___ = _____")
    print(f"                    {f1['m']}     {f2['m']}     {result['m']}")
    if result['s'] == result['m']:
        print(" = 1")
    elif result['s'] == 0:
        print(' = 0')
    separator()
    return result


def product(f1, f2):
    result = {}
    result["s"] = f1["s"] * f2["s"]
    result["m"] = f1["m"] * f2["m"]
    print(f"                       {f1['s']}     {f2['s']}     {result['s']}")
    print(" ---> Multiplication: ___ × ___ = _____")
    print(f"                       {f1['m']}     {f2['m']}     {result['m']}")
    if result['s'] == result['m']:
        print(" = 1")
    elif result['s'] == 0:
        print(' = 0')
    separator()
    return result


def quotient(f1, f2):
    result = {}
    result["s"] = f1["s"] * f2["m"]
    result["m"] = f1["m"] * f2["s"]
    print(f"                 {f1['s']}     {f2['s']}     {result['s']}")
    print(" ---> Division: ___ ÷ ___ = _____")
    print(f"                 {f1['m']}     {f2['m']}     {result['m']}")
    if result['s'] == result['m']:
        print(" = 1")
    elif result['s'] == 0:
        print(' = 0')
    separator()
    return result


while True:
    user_choice = input("Enter 's' to start the program or 'e' to exit: ")
    if user_choice == "s":
        f1 = {"s": int(input("Please enter the numerator of fraction1: ")),
              "m": int(input("Please enter the denominator of fraction1: "))}
        print(f"Your fraction1 is: {f1['s']} / {f1['m']}")
        f2 = {"s": int(input("Please enter the numerator of fraction2: ")),
              "m": int(input("Please enter the denominator of fraction2: "))}
        print(f"Your fraction2 is: {f2['s']} / {f2['m']}")
        print("-------------------------------")
        operation_choice = int(input(
            "Enter the number of the operation you want to perform:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n---> "))
        separator()
        if operation_choice == 1:
            sum(f1, f2)
        elif operation_choice == 2:
            difference(f1, f2)
        elif operation_choice == 3:
            product(f1, f2)
        elif operation_choice == 4:
            quotient(f1, f2)
    elif user_choice == "e":
        break
    else:
        print("Invalid input!")
