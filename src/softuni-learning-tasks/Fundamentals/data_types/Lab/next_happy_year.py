def next_happy_year(year):
    is_happy_year = False
    while True:
        year += 1
        digits = str(year)
        is_happy_year = True

        for i in range(len(digits)):
            for j in range(i + 1, len(digits)):
                if digits[i] == digits[j]:
                    is_happy_year = False
                    break
            if not is_happy_year:
                break

        if is_happy_year:
            print(year)
            break


next_happy_year(8989)
next_happy_year(1001)
