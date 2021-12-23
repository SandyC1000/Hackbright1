"""Restaurant rating lister."""


# put your code here
rest_name = input("Enter Restaurant name: ")
rest_score = input("Enter Restaurant score: ")


infile = open("scores.txt")
restaurant_dic = {rest_name:rest_score}


for line in infile:
    line = line.rstrip()  #each line use func rstrip()
    words = line.split(':') # words is list of elements split()

    restaurant_dic[words[0]] = words[1] # make dic KEY=word[0] then VALUE=words[1]

sorted_items = sorted(restaurant_dic.items()) # sort Keys and Values

for restaurant_index, count in sorted_items:
   print(f"{restaurant_index} is rated at {count}.")

