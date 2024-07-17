import time
import datetime


filename=datetime.datetime.now()
#filename= str(filename)
filename= filename.strftime("%d-%b-%Y-%H-%M--%S")

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


"""Better code from instructor"""
# import glob2
# import datetime

# filenames=glob2.glob("*.txt")

# with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
# for filename in filenames:
# with open(filename,"r") as f:
# file.write(f.read()+"\n")

