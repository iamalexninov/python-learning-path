def numbers_between_range():
    number = float(input("Enter a number: "))
    while number < 1 or number > 100:
        number = float(input())

    print(f'The number {number} is between 1 and 100')


numbers_between_range()
