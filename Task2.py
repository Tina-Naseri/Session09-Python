def add_time(t1, t2):
    result = {}
    result["h"] = t1["h"] + t2["h"]
    result["m"] = t1["m"] + t2["m"]
    result["s"] = t1["s"] + t2["s"]
    if result["s"] >= 60:
        result["s"] -= 60
        result["m"] += 1
    if result["m"] >= 60:
        result["m"] -= 60
        result["h"] += 1
    print(f"Your result is    ---> {result['h']} : {result['m']} : {result['s']}")
    return result


def subtract_time(t1, t2):
    result = {}
    result["h"] = t1["h"] - t2["h"]
    result["m"] = t1["m"] - t2["m"]
    result["s"] = t1["s"] - t2["s"]
    if t1["s"] < t2["s"]:
        t1["m"] -= 1
        t1["s"] += 60
    if t1["m"] < t2["m"]:
        t1["h"] -= 1
        t1["m"] += 60
    result["h"] = t1["h"] - t2["h"]
    result["m"] = t1["m"] - t2["m"]
    result["s"] = t1["s"] - t2["s"]
    print(f"Your result is    ---> {result['h']} : {result['m']} : {result['s']}")
    return result


while True:
    user_choice = input("Enter 's' to start the program or 'e' to exit: ")

    if user_choice == "s":
        t1 = {"h": int(input("Please enter the hour of time1: ")),
              "m": int(input("Please enter the minute of time1: ")),
              "s": int(input("Please enter the second of time1: "))}
        print(f"Your time1 is: {t1['h']} : {t1['m']} : {t1['s']}")
        print("-------------------------------")
        t2 = {"h": int(input("Please enter the hour of time2: ")),
              "m": int(input("Please enter the minute of time2: ")),
              "s": int(input("Please enter the second of time2: "))}
        print(f"Your time2 is: {t2['h']} : {t2['m']} : {t2['s']}")
        print("-------------------------------")
        operation_choice = int(input(
            "Enter the number of the operation you want to perform:\n1. Addition\n2. Subtraction\n---------------\nYour operation is ---> number "))
        if operation_choice == 1:
            add_time(t1, t2)
        elif operation_choice == 2:
            subtract_time(t1, t2)
    elif user_choice == "e":
        break
    else:
        print("Invalid input!")
