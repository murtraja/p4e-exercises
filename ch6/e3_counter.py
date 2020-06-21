def count_char(string, ch):
    count = 0
    for char in string:
        if char == ch:
            count += 1
    return count

print(count_char('banana', 'a'))