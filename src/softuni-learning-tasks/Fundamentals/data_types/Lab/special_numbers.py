# import math


def special_numbers(number):
    for i in range(1, number + 1, 1):
        first_num = i // 10
        second_num = i % 10
        sum = first_num + second_num
        if (sum == 5 or sum == 7 or sum == 11):
            print(f'{i} -> True')
        else:
            print(f'{i} -> False')


special_numbers(15)
special_numbers(6)

# What learning from this example:
# 14 / 10    # 1.4  → / always gives a float
# 14 // 10   # 1    → // gives integer (floor) division
