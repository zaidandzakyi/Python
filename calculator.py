#CALCULATOR

print("\n===== CALCULATOR =====\n")

options = ['+','-','*','/']
loop = True
while loop:
    try :
        data = float(input("Input First Number : "))
    except ValueError:
        print("Data Invalid...")
        break
    data2 = input("(+ | - | * | / ) : ")
    if data2 not in options :
        print("Invalid syntax...")
        break
    try:
        data3 = float(input("Input second Number : "))
    except ValueError:
        print("Data Invalid...")
        break
    if data2 == "+":
        value = data + data3
        print("Value : ",value)
        user_input = input("\nwanna try again ? yes/no : ")
        if user_input == "yes":
            continue
        else :
            break
    elif data2 == "-":
        value = data - data3
        print("Value : ",value)
        user_input = input("\nwanna try again ? yes/no : ")
        if user_input == "yes":
            continue
        else :
            break
    elif data2 == "*":
        value = data * data3
        print("Value : ",value)
        user_input = input("\nwanna try again ? yes/no : ")
        if user_input == "yes":
            continue
        else :
            break
    elif data2 == "/":
        try:
            value = data / data3
            print("Value : ",value)
            user_input = input("\nwanna try again ? yes/no : ")
            if user_input == "yes":
                continue
            else :
                break
        except ZeroDivisionError:
            print("Data invalid")
            break
print("\nCalculator End...")
