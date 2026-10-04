def even_numbers(number:int):
    is_odd = False
    for i in range(0, number, 1):
        current_number = int(input("Enter a number: "))
        if(current_number % 2 == 1):
            isOdd = True
            print(current_number + " is odd!")
            break
            
    if(is_odd is not True):
        print("All numbers are even.")
            
even_numbers(3)
