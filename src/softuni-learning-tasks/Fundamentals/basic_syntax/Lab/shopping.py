def shopping(budget: int, ):
    productPrices = input("Enter price: ")
    is_overdraft = False
    while productPrices != "End":
        if (budget > int(productPrices)):
            budget -= int(productPrices)
        else:
            print("You went in overdraft")
            is_overdraft = True
            break

        productPrices = input("Enter price: ")

    if (is_overdraft is not True):
        print("You bought everything needed.")


shopping(100)
shopping(50)
