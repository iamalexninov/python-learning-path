def centuries_to_minutes(century):
    years = century * 100
    days = int(round(years * 365.2422))
    hours = days * 24
    minutes = hours * 60
    
    print(f'{century} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')
    
centuries_to_minutes(1)
centuries_to_minutes(5)