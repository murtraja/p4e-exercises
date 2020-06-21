# file_name = input("Enter a file name: ")
file_name = "mbox-short.txt"
f = open(file_name)
try:
    f = open(file_name)
except FileNotFoundError as e:
    print('File can\'t be opened: '+file_name)
    exit(0)

count = 0
for line in f.readlines():
    words = line.split()
    if len(words) < 2 or words[0] != "From":
        continue
    count += 1
    print(words[1])

print(f'There were {count} lines in the file with From as the first word')
