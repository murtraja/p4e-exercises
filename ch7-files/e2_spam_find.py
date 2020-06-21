# file_name = input("Enter a file name: ")
file_name = "mbox-short.txt"
file_name = "mbox.txt"
f = open(file_name)
try:
    f = open(file_name)
except FileNotFoundError as e:
    print('File can\'t be opened: '+file_name)
    exit(0)

total_spam = count = 0
for line in f.readlines():
    if line.startswith("X-DSPAM-Confidence:"):
        total_spam += float(line[line.find(":")+1:])
        count += 1

if count != 0:
    print(f'avg spam: {(total_spam/count)}')