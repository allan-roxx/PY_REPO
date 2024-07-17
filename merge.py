import time
import datetime


filename=datetime.datetime.now()
#filename= str(filename)
filename= filename.strftime("%d-%b-%Y-%H-%M--%S")

    


filename
with open("file1.txt", 'r') as file:
    file.seek(0)
    content1= file.readlines()
print(content1)   
with open("file2.txt", 'r') as file:
     content2= file.readlines()
    

with open("file3.txt", 'r') as file:
    content3= file.readlines()   

content4= [i for i in content1]
content4.append(content2[0])
content4.append(content3[0])

print(content4)
def file_name():
    with open(filename +".txt", 'w+') as file:
        for i in content4:
            file.write(i)

file_name()

#with open(now, '+') as file: