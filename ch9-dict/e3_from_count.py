# file_name = input("Enter a file name: ")
file_name = "mbox-short.txt"
f = open(file_name)
try:
    f = open(file_name)
except FileNotFoundError as e:
    print('File can\'t be opened: '+file_name)
    exit(0)

count = {}
for line in f.readlines():
    words = line.split()
    if len(words) < 3 or words[0] != "From":
        continue
    sender = words[1]
    if sender not in count:
        count[sender] = 0
    count[sender] += 1

print(count)
