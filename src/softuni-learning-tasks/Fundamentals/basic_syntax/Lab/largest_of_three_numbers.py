def largest_of_three_numbers(number1, number2, number3):
    if number1 > number2 and number1 > number3:
        return number1
    if number2 > number1 and number2 > number3:
        return number2
    return number3
    
test1 = largest_of_three_numbers(3, -1, 5)
test2 = largest_of_three_numbers(0, -1, -2)
print(test1)
print(test2)