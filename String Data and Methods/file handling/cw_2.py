#CSV File
import csv
file_path=r"C:\Users\Sujan Piya\Downloads\2022-01-03.csv"

with open(file_path,'r')as file_obj:
        reader=csv.reader(file_obj)
        data=list(reader)
for row in data:
        print(row)

student_info=[
        ['Name','Gender','Class'],
        ['Buddha','M','Python with DS'],
        ['Brisha','F','Python'],
        ['Suhasi','F','AI']

]

import csv
file_path=r"C:\Users\Sujan Piya\Downloads\info.csv"

with open(file_path,'w',encoding='utf-8',newline="")as file_obj:
        writer=csv.writer(file_obj)
        writer.writerows(student_info)

student_info_dict=[
        {'Name':'Buddha','Gender':'M','Class':'Python with DS'},
        {'Name':'Brisha','Gender':'F','Class':'Pyhton'},
        {'Name':'Suhasi','Gender':'F','Class':'Python'},
]
        
import csv
file_path=r'C:\Users\Sujan Piya\Downloads\first.csv'
header=student_info_dict[0].key()

with open(file_path,'w',encoding='utf-8,' newline="")
writer=csv.DictWriter(file_obj, filednames=header)
writer.writerheader
writer.writerows(student_info_dict)

        