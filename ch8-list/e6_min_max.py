nos = []
while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break
    try:
        no = float(user_input)
    except ValueError as e:
        print("Invalid input")
        continue
    nos.append(no)

if len(nos) > 0:
    min_no = min(nos)
    max_no = max(nos)
    print(f'Maximum: {max_no}\nMinimum: {min_no}')
