#Define a function called `greet` that takes a name as an argument and prints a greeting message like:
#  "Hello, [name]!"
"""def greet(name):
    print("hello",name)

greet("siva")
greet("samba")"""

#Write a function `add_numbers` that takes two numbers as arguments and returns their sum. Test the function by 
#passing different numbers.
"""def add(x,y):
    print(x+y)

add(10,20)
add(345,678)"""

#Create a function `is_even` that takes a number as an argument and returns `True` if
#the number is even, and `False` otherwise.
"""def is_even(i):
    if i%2==0:
        return True
    else:
        return False
    
print(is_even(8))
print(is_even(5))"""

#Write a function `factorial` that takes a positive integer as input and returns the factorial of that number.
#Remember, `factorial(5)` should return \(5 \times 4 \times 3 \times 2 \times 1 = 120\).
"""def factorial(s):
    if s==0:
        return 1
    else:
        return(s*factorial(s-1))

print(factorial(5))"""

#Define a function `find_max` that takes three numbers as input and returns
#the largest of the three. Test the function with various sets of numbers.

def find_max(a,b,c):
    return max(a,b,c)

print(find_max(10,20,30))
print(find_max(56,97,98))
print(find_max(34,57,43))

