"""Count words in file."""

#  fname = input ("Enter filename: ")

infile = open("test.txt")
word_dic = {}
for line in infile:
    line = line.rstrip()
    words = line.split(' ') # words is list of elements
    for word_index in words:
        word_dic[word_index] = word_dic.get(word_index,0) + 1

for word_index, count in word_dic.items():
    print(word_index, count)

