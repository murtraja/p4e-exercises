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
    if len(words) < 2 or words[0] != "From":
        continue
    sender = words[1]
    if sender not in count:
        count[sender] = 0
    count[sender] += 1

dict_list = [(v,k) for k,v in count.items()]
reverse_sorted = sorted(dict_list, reverse=True)
max_count, max_email = reverse_sorted[0]
print(max_email, max_count)
