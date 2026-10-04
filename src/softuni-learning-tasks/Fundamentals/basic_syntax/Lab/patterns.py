def patterns(number):
    # from 0 to number
    for i in range(1, number + 1, 1):
        print("*" * i)

    # from number to 0
    for j in range(number - 1, -1, -1):
        print("*" * j)


patterns(3)
patterns(5)
