def chat_codes(number: int):
    for i in range(number):
        received_number = int(input("Enter a number: "))
        if (received_number == 88):
            print("Hello")
        elif (received_number == 86):
            print("How are you?")
        elif ((received_number != 88 or received_number != 86) and received_number < 88):
            print("GREAT!")
        elif (received_number > 88):
            print("Bye.")


chat_codes(4)
chat_codes(3)
