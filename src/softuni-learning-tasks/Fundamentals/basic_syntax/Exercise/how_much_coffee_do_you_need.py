def how_much_coffee_do_you_need():
    count = 0
    inputValue = input("Enter a string value: ")
    while inputValue != "END":
        if (inputValue == "coding" or inputValue == "CODING"):
            count += check_case_sensitivity(inputValue)
        elif (inputValue == "dog" or inputValue == "DOG"):
            count += check_case_sensitivity(inputValue)
        elif (inputValue == "cat" or inputValue == "CAT"):
            count += check_case_sensitivity(inputValue)
        elif (inputValue == "movie" or inputValue == "MOVIE"):
            count += check_case_sensitivity(inputValue)

        inputValue = input("Enter a string value: ")

    if (count > 5):
        print("You need extra sleep")
    else:
        print(f'{count}')


def check_case_sensitivity(word):
    if (word.islower()):
        return 1
    return 2


how_much_coffee_do_you_need()
