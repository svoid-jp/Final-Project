#Ask user for marks and display grade in format: Your grade is A.
# (Rule: 90+ => A, 80-90 => B, 70-80 => C, 60-70 => D, below 60 F)
marks=int(input("Enter your marks: "))
if marks>=90:
 print("Grade A")
elif marks<90 and marks>=80:
 print("Grade B")
elif marks<80 and marks>=70:
 print("Grade C")
elif marks<70 and marks>=60:
 print("Grade D")
else:
 print("Grade F")


#Ask user for birth year and display life stage in format: You are a teenager.
# (Rule: 0-12 => Child, 13-19 => Teenager, 20-59 => Adult, 60+ => Senior)

#Auser_name = input("Enter your name: ")age = int(input("Enter your age: "))if age <= 0:    age_group = "Invalid age"elif age <= 12:    age_group = "Children"elif age <= 19:    age_group = "Teenager"elif age <= 59:    age_group = "Adult"else:    age_group = "Senior"print(f"{user_name}, You belong to {age_group} category")

 
#This is an isosceles triangle. 
#(Rule: All sides equal => Equilateral, Two sides equal => Isosceles, No sides equal => Scalene)
#Ask user for two numbers and display the largest in format: The largest number is 5
#Ask user for hour of the day (0-23) and display appropriate greeting in format:
# Good Morning. 
#(Rule: 5-12 => Good Morning, 12-17 => Good Afternoon, 17-21 => Good Evening, 21-5 => Good Night, 
# else invalid time)