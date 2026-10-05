def string_pureness(number):
    is_pure = True
    for i in range(number):
        str = input("Enter a string: ")
        for j in range(len(str)):
            if (str[j] == "," or str[j] == "." or str[j] == "_"):
                is_pure = False
        if (is_pure is not True):
            print(f'{str} is not pure!')
            break
        else:
            print(f'{str} is pure.')


string_pureness(2)
string_pureness(3)
