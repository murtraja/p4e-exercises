# file_name = input("Enter a file name: ")
file_name = "mbox-short.txt"
# file_name = "mbox.txt"
f = open(file_name)
try:
    f = open(file_name)
except FileNotFoundError as e:
    print('File can\'t be opened: '+file_name)
    exit(0)

count = {}
for line in f.readlines():
    words = line.split()
    if len(words) < 3 or words[0] != "From" or words[1].find('@') == -1:
        continue
    sender = words[1]
    domain = sender[sender.find('@')+1:]
    if domain not in count:
        count[domain] = 0
    count[domain] += 1

print(count)
