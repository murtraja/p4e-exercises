import string

# file_name = input("Enter a file name: ")
file_name = "romeo-full.txt"
# file_name = "mbox.txt"
f = open(file_name)
try:
    f = open(file_name)
except FileNotFoundError as e:
    print('File can\'t be opened: '+file_name)
    exit(0)

letters = [l for l in f.read() if l in string.ascii_lowercase]
count = {}
total_count = 0
for l in letters:
    if l not in count:
        count[l] = 0
    count[l] += 1
    total_count += 1

# print(count)
frequencies = [(occurrences/total_count, letter) for letter, occurrences in count.items()]
frequencies.sort(reverse=True)
[print(letter, f'{freq*100:.2f}%') for freq, letter in frequencies]