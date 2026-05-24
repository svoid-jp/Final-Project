#Ask user for name and price of a pen. display in format: Ram bought a pen for $ 10.56
name=input("Enter your name:")
price=float(input("Enter price of the pen:"))
print(f"{name} bought a pen for ${price}")
#Ask user for name, price of three product. Display it in format as:
#Item        Price
#--------------------
#Apple       Rs.   3
#Banana      Rs.  10
#Orange      Rs. 200
#Note: Item is left aligned with width of 12 and price is right aligned with width of 3
item1 = input("Enter first item: ")
price1 = int(input("Enter price: "))

item2 = input("Enter second item: ")
price2 = int(input("Enter price: "))

item3 = input("Enter third item: ")
price3 = int(input("Enter price: "))

print(f"{'Item':<12}Price")
print("-" * 20)

print(f"{item1:<12}Rs. {price1:>3}")
print(f"{item2:<12}Rs. {price2:>3}")
print(f"{item3:<12}Rs. {price3:>3}")

#Ask user for current year, month and day. Display it in format: Today's Date: 2023-03-12
current_year=input("Enter current year:")
current_month=input("Enter current month:")
current_day=input("Enter current day:")
print(f"{current_year:-<5}{current_month}{current_day:->3}")

#Ask user for name and marks in 3 subject. Display result as: Hari scored 85.5% in exam.
user_name=input("Enter your name")
m1 = int(input("Enter marks of subject 1: "))
m2 = int(input("Enter marks of subject 2: "))
m3 = int(input("Enter marks of subject 3: "))
print(f"{user_name}scored {(m1+m2+m3/300)*100}")