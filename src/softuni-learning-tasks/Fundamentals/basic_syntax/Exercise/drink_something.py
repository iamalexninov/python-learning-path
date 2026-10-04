def drink_something(age):
    kids_drinking = "toddy"
    teens_drinking = "coke"
    youngs_drinking = "beer"
    adults_drinking = "whisky"

    if (age <= 14):
        print(f'drink {kids_drinking}')
    elif (age > 14 and age < 18):
        print(f'drink {teens_drinking}')
    elif (age >= 18 and age <= 21):
        print(f'drink {youngs_drinking}')
    else:
        print(f'drink {adults_drinking}')


drink_something(13)
drink_something(17)
drink_something(21)
drink_something(30)
