#Store student info as: [[name_1, age_1], [name_2, age_2], ...]. Display 2nd student's age.
students = [["Ram", 16], ["Sita", 15], ["Hari", 17]]
print(students[1][1])

#Assign marks in five subjects to mark_list and subject names in subject_list. Display:
mark_list=[90,82,85,60,50]
subject_list=["English","Science","Maths","Computer","Social"]

#total, average, highest and lowest marks obtained by student
total = sum(mark_list)
average=total/len(mark_list)
highest=max(mark_list)
lowest=min(mark_list)
print(total)
print(average)
print(highest)
print(lowest)

#Change name of 2nd subject (1st index) to Python and display updated list
subject_list[1] = "Python"
print(subject_list)

#Marks obtained in subject at 3rd position (2nd index) as Mark obtained in English is 89
subject_list[2]=mark_list

#Marks obtained in subject at second last position with similar format as above.
second_last_subject_name = subject_list[-2]
second_last_mark_value = mark_list[-2]
print(f"Marks obtained in {second_last_subject_name} is {second_last_mark_value}")

#Marks obtained in last two subjects
print(mark_list[-2:])

#Marks in first three subjects
print(mark_list[:3])

#Name of subject in which student scored highest marks
max_mark = max(mark_list)
print(max_mark)

#Name of subject in which student scored lowest marks
min_marks=min(mark_list)
print(min_marks)

#Number of subjects in which student scored 80
count_students=mark_list.count(80)
print(count_students)