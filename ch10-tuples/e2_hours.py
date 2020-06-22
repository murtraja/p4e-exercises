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
    if len(words) < 6 or words[0] != "From":
        continue
    time_components = words[5].split(':')
    if len(time_components) == 0:
        continue
    hour = time_components[0]
    if hour not in count:
        count[hour] = 0
    count[hour] += 1

dict_list = [(k,v) for k,v in count.items()]
reverse_sorted = sorted(dict_list)

[print(hour, count) for hour, count in reverse_sorted]
