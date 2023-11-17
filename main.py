import string
import time

uppercase_alphabets = list(string.ascii_uppercase)
lowercase_alphabets = list(string.ascii_lowercase)

alphabet_list = uppercase_alphabets + lowercase_alphabets
alphabet_list.append(' ')

temp = []

finalstring = "Hello World"

for index, element in enumerate(finalstring):
    temp.append('')
    for item in alphabet_list:
        temp[index] = item
        time.sleep(0.009)
        print("".join(temp))
        if item == element:
            break
print(":)")        
x = input()