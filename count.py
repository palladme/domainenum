
number_of_words = 0
 
with open(r'out2.txt','r') as file: 
    data = file.read()
    lines = data.split()
    number_of_words += len(lines)
 
print(number_of_words)