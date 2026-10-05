def double_char():
    result = ""
    str = input("Enter a string value: ")
    while str != "End":
        for i in range(len(str)):
            result += str[i] + str[i]

        if (str != "SoftUni"):
            print(result)
        result = ""
        str = input("Enter a string value: ")


double_char()
