#Create two variables num_1 as 7, num_2 as 3.5 and:
#Display their data types
#Display their sum
#Display their difference
#Display their product
#Display their division
num_1 = 7
num_2 = 3.5
print (type(num_1), type(num_2))
print (num_1+num_2)
print (num_1-num_2)
print (num_1*num_2)
print (num_1/num_2)
#Convert both num_1 and num_2 into string and display sum again
num_1_int = str(num_1)
num_2_int = str(num_2)
print(str(num_1)+str(num_2))

#Create variable num_3 as 15 and num_4 as 4. Swap their values and display the result
num_3 = 15
num_4 = 4

num_3, num_4 = num_4, num_3
print(num_3)