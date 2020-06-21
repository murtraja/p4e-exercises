min_no = 2**32
max_no = -min_no
while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break
    try:
        no = float(user_input)
    except ValueError as e:
        print("Invalid input")
        continue
    if no>max_no:
        max_no = no
    if no<min_no:
        min_no = no

if min_no != 2**32:
    print(f'{min_no:g} {max_no:g}')
