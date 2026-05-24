#Ask user for his/her name and display: Hello, <name>!
user_name=input("Enter your name:")
print(f"Hello,{user_name}!")

#Ask user for his/her birth year. Calculate and display his/her age
birth_year=int(input("Enter your birth year:"))
current_year=int(input("Enter current year:"))
print(current_year-birth_year)

#Ask user for mass and length of a cube. Calculate and display its density (d = m/v)
mass_1=int(input("Enter mass of cube:"))
length_1=int(input("Enter length of cube"))
volume = length_1 ** 3
density = mass_1 / volume
print( density)

#Ask user for length in feet and convert and display its value in meter (1 ft = 0.3048 m)
length_feet = float(input("Enter length in feet: "))
length_meter = length_feet * 0.3048
print( length_meter)

#Ask user for a file name in format file.ext. Extract and display file extension from it
file_name = input("Enter full file name: ")
file_name_list = file_name.split(".")
extension_name = file_name_list[-1]
print(f"File Extension: {extension_name}")

#Ask user for a sentence and display number of words in it.
sentence = input("Enter a sentence: ")
words = sentence.split()
count = len(words)
print( count)
#Ask user for two numbers and display their sum, difference, product and quotient.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print("Sum =", num1 + num2)
print("Difference =", num1 - num2)
print("Product =", num1 * num2)
print("Quotient =", num1 / num2)