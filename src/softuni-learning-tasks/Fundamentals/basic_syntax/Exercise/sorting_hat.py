def sorting_hat():
    command = input("Enter command: ")
    is_voldemort_received = False
    while (command != "Welcome!"):

        if (command != "Voldemort"):
            if (len(command) < 5):
                print(f'{command} goes to Gryffindor.')
            elif (len(command) == 5):
                print(f'{command} goes to Slytherin.')
            elif (len(command) == 6):
                print(f'{command} goes to Ravenclaw.')
            elif (len(command) > 6):
                print(f'{command} goes to Hufflepuff.')

            command = input("Enter command: ")
        else:
            print("You must not speak of that name!")
            is_voldemort_received = True
            break

    if (is_voldemort_received is not True):
        print("Welcome to Hogwarts.")


sorting_hat()
#sorting_hat()
