try:
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
except ValueError as e:
    print('Error, please enter numeric input')
    exit(0)
bonus_hours = 0 if hours <= 40 else hours-40
normal_hours = hours - bonus_hours
pay = (normal_hours + bonus_hours*1.5)*rate
print(f'Pay: {pay}')