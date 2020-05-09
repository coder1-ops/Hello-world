#file handling
# r : read    w : write    a : append      r+ : read write


with open('C:/Users/Nishat/Desktop/file1.txt','r+') as file1:
    file1.write("i am fine")
    print(file1.read())
file1.close()
