#Reading text file
#file_path=r'c:\user\desktop\notebel.txt'
file_path=r"C:\Users\Sujan Piya\Downloads\nobel_prize_speech.txt"
with open(file_path, 'r',encoding='utf-8') as file_obj:
    content=file_obj.read()
    print(content)
    repetition_of_the=content.count("the")
    print(repetition_of_the)

my_content='''We are reading File Handling.We are going to write on file 

the course is nearly completed.
'''

file_path=r"C:\Users\Sujan Piya\Downloads\progress.txt"
with open (file_path, 'w',encoding='utf-8') as file_obj:
            file_obj.write(my_content)


my_content="\nbye"
file_path=r'C:\Users\Sujan Piya\Downloads\progress.txt'

with open(file_path,'a',encoding='utf-8') as file_obj:
        file_obj.write(my_content)

#CSV File
import csv
file_path=r"C:\Users\Sujan Piya\Downloads\2022-01-03.csv"

with open(file_path,'r')as file_obj:
        reader=csv.reader(file_obj)
        data=list(reader)
