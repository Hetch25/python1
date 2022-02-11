"""#first way to read a file
file = open('Clase 21/my_file.txt')
content = file.read()
print(content)
file.close()"""

#second way to open a file
with open('Clase 21/my_file.txt') as file:
    content = file.read()
    print(content)

with open('Clase 21/my_file.txt',mode='a') as file:
    #mode 'a' = append
    #mode 'w' = write
    #mode 'r' = read
    file.write("This is new text to test my write mode\n")