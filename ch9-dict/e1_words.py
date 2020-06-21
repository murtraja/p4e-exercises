# file_name = input("Enter a file name: ")
file_name = "words.txt"
f = open(file_name)
try:
    f = open(file_name)
except FileNotFoundError as e:
    print('File can\'t be opened: '+file_name)
    exit(0)

# word_list = [word.strip() for line in f.readlines() for word in line.split(' ') if word.strip() != '']
word_list = {word.strip() for line in f.readlines() for word in line.split(' ') if word.strip() != ''}


# print(word_list)
print('one' in word_list)
print('once' in word_list)