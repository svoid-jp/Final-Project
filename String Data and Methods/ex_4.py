#Assign str_1 as "Hello", str_2 as "12345", str_3 as "##abc123##" and str_4 as " "
str_1="Hello"
str_2="12345"
str_3="##abc123##"
str_4=" "
#Check and display if str_1 has alphabetic characters only.
is_alpha = str_1.isalpha()
print(is_alpha)
#Check and display if str_1 has numeric characters only.
is_numeric = str_1.isnumeric()
print(is_numeric)
#Check and display if str_2 has alphanumeric characters only.
is_alnum = str_2.isalnum()
print(is_alnum)
#Check and display if str_4 is empty.
is_empty = (str_4 == "")
print(is_empty)
#Check and display if str_3 starts with abc
starts_abc = str_3.startswith("abc")
print(starts_abc)
#Check and display if str_3 ends with 3
ends_3 = str_3.endswith("3")
print(ends_3)
#Check and display if str_1 starts with He and ends with lo
check_both = str_1.startswith("He") and str_1.endswith("lo")
print(check_both)
#Remove leading and trailing # from str_3 and display the result
removed_both = str_3.strip("#")
print(removed_both)

#Remove leading # from str_3 and display the result
removed_left = str_3.lstrip("#")
print(removed_left)