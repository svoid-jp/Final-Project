#Ask user for name and birth year. Calculate and display if he/she can vote in format:
# Ram, You are [not] eligible for voting. (Note: 18+ people can vote)
name=input("Enter your name: ")
birth_date=int(input("Enter your birth date:"))
current_year=2026
birth_year_check=current_year-2026
if birth_year_check>=18:
    print(f"{name},You are eligible to vote")
else:
    print(f"{name},You are not eligible to vote")

#Ask user for num_1 and num_2. Display if num_1 is divisible by num_2 in format: 
#15 is [not] divisible by 3
num_1=int(input("Enter any number: "))
num_2=int(input("Enter any number: "))
if num_1%num_2==0:
    print("It is divisible: ")
else:
    print("It is not divisible:")
#Ask user for name, age and salary. Display if user is eligible for a loan in format: 
# Ram, You are [not] eligible for loan.
#  (Eligibility Rule: Age between 21 and 60, salary at least 30K)
name=input("Enter your name: ")
age=int(input("Enter your age: "))
salary=int(input("Enter your salary: "))
if age>20 and age<60 and salary>=30000:
    print(f"{name} is eligible for loan")
else:
    print(f"{name} is not eligible for loan")
#Ask user for string and check if it's palindrome in format: "madam" is [not] a palindrome
string=input("Enter string: ")
rev_string=string[::-1]
if rev_string==string:
 print("It is Palindrome: ")
else:
    print("It is not palindrome: ")


#Store customer balance in a variable. Ask user for amount to withdraw.
#  If desired amount is less than total balance display, 123 withdrawn successfully.
#  New Balance: 456 else display Insufficient balance. You only have 123 in your account
amount=float(input("Enter the amount to withdraw: "))
total_balance=10000000
if amount<=10000000:
    print(f"{amount} withdrawn sucessfully:")
else:
    print(f"You only have {total_balance} in your account ")


