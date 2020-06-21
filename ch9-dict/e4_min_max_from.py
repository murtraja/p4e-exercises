# file_name = input("Enter a file name: ")
file_name = "mbox-short.txt"
file_name = "mbox.txt"
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

dict_list = [[k,v] for k,v in count.items()]
value_list = [v for k,v in dict_list]
max_value = max(value_list)
index_max_value = value_list.index(max_value)
max_sender, max_value = dict_list[index_max_value]
print(max_sender, max_value)
