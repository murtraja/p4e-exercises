# file_name = input("Enter a file name: ")
file_name = "romeo.txt"
f = open(file_name)
try:
    f = open(file_name)
except FileNotFoundError as e:
    print('File can\'t be opened: '+file_name)
    exit(0)

word_list = [word.strip() for line in f.readlines() for word in line.split(' ')]
word_set = set(word_list)
unique_word_list = list(word_set)
# print(len(word_list))
# print(len(unique_word_list))
print(sorted(unique_word_list))