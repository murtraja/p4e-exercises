file_name = input("Enter a file name: ")
# file_name = "mbox-short.txt"
f = open(file_name)
try:
    f = open(file_name)
except FileNotFoundError as e:
    print('File can\'t be opened: '+file_name)
    exit(0)
for line in f.readlines():
    print(line.upper())