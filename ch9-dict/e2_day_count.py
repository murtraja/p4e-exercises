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
    day = words[2]
    if day not in count:
        count[day] = 0
    count[day] += 1

print(count)
