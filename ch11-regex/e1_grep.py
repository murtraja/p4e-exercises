import re

# file_name = input("Enter a file name: ")
# file_name = "mbox-short.txt"
file_name = "mbox.txt"
f = open(file_name)
try:
    f = open(file_name)
except FileNotFoundError as e:
    print('File can\'t be opened: '+file_name)
    exit(0)

# regex_string = input("Enter a regular expression: ")
regex_string = r'^Author'
regex_string = r'^X-'
regex_string = r'java$'
result = [re.search(regex_string, line) for line in f.readlines()]
count = sum([1 for r in result if r is not None])
print(f'{file_name} had {count} lines that matched {regex_string}')