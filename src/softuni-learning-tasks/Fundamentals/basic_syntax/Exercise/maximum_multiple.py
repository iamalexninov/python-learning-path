def maximum_multiple(divisor, boundary):
    biggest_division = 0
    for i in range(boundary):
        current_biggest_division = round(i / divisor) * divisor
        biggest_division = max(biggest_division, current_biggest_division)

    print(biggest_division)

maximum_multiple(2, 7)
maximum_multiple(10, 50)
maximum_multiple(37, 200)
