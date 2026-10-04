def orders(number_of_orders):
    total_price_of_orders = 0
    for i in range(number_of_orders):
        capsules_price = float(input("Enter a capsule price: "))
        days = int(input("Enter days: "))
        capsules = int(input("Enter capsules: "))

        current_total_price = (capsules * days) * capsules_price
        if (capsules > 0):
            print(f'The price of the coffee is: ${current_total_price:.2f}')
        total_price_of_orders += current_total_price

    print(f'Total: ${total_price_of_orders:.2f}')


# orders(1)
# orders(2)
orders(2)
