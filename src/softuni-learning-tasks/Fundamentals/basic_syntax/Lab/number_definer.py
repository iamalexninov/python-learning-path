def number_definer(number):
    number = float(number)
    if number == 0:
        return "zero"
    elif number > 0:
        if(abs(number) < 1 and abs(number) > 0):
            return "small positive"
        elif(abs(number) > 1000000):
            return "large positive"
        else:
            return "positive"
    elif number < 0:
        if(abs(number) < 1 and abs(number) > 0):
            return "small negative"
        elif(abs(number) > 1000000):
            return "large negative"
        else:
            return "negative"

print(number_definer(25))
print(number_definer(0.7))
print(number_definer(435247392.921))
print(number_definer(-0.005))
print(number_definer(-103.21))
print(number_definer(-358583355123.001))