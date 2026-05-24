#Write a function get_simple_interest(principal, rate, time) to calculate and return simple interest
#  based on given principal, rate and time.
def get_simple_interest(principal, rate, time):
    si = (principal * rate * time) / 100
    return si

si = get_simple_interest(5000, 10, 2)
print(f"Simple Interest={si}")

#Write a function get_rectangle_area_perimeter(length, width) to calculate and
#  return area and perimeter of a rectangle based on length and width.
def get_rectangle_area_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

area, perimeter = get_rectangle_area_perimeter(10, 5)
print(f"Area of rectangle={area}")
print(f"Perimeter of rectangle={perimeter}")

#Write a function is_palindrome(string) to check if a given string is palindrome or not. 
# Return True if it is palindrome else return False.
#Write a function count_vowels(string) return the number of vowels in a given string.
#Write a function  get_square_root(num) to return the square root of a given number.