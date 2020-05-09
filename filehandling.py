#file handling

with open('C:/Users/Nishat/Desktop/file1.txt','r+') as file1:
    file1.write("i am fine")
    print(file1.read())
file1.close()