import re

# file_name = input("Enter a file name: ")
file_name = "mbox-short.txt"
# file_name = "mbox.txt"
f = open(file_name)
try:
    f = open(file_name)
except FileNotFoundError as e:
    print('File can\'t be opened: '+file_name)
    exit(0)

# regex_string = input("Enter a regular expression: ")
regex_string = r'New Revision: (\d+)'
m = re.findall(regex_string, f.read(), re.M)
m = [int(x) for x in m]
mean = sum(m)//len(m)
print(mean)