def computepay(hours, rate):
    bonus_hours = 0 if hours <= 40 else hours-40
    normal_hours = hours - bonus_hours
    pay = (normal_hours + bonus_hours*1.5)*rate
    return pay

hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
print(f'Pay: {computepay(hours, rate)}')