sum = count = 0
while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break
    try:
        no = float(user_input)
    except ValueError as e:
        print("Invalid input")
        continue
    sum += no
    count += 1

if count != 0:
    print(f'{sum:g} {count} {sum/count}')
