# today i am going to start challenge to learn python programming (date 20-10-24 Sunday)
#1.here first program to print hello world.
print("hello world")
#2. variable - it is like container that store values.
nam = "Abdulla" # string
print(nam)
num = 10 # integer
rs = 10.1# float
print(num,rs)
""" we use these triple quote to comment multiple line of words.
    3.Data Types
    Python supports various data types, including integers, floats, strings, lists, tuples, dictionaries, and more.
    Integers: Whole numbers without decimals.
    Floats: Numbers with decimals.
    Strings: Text enclosed in single or double quotes.
    Lists: Ordered collections of items.
    Tuples: Immutable collections of items.
    Dictionaries: Key-value pairs.
"""
#4. Operators
"""
    Arithmetic operators: +, -, *, /, %, ** (exponentiation), // (floor division).
    Comparison operators: ==, !=, <, >, <=, >=.
    Logical operators: and, or, not.
    Assignment operators: =, +=, -=, *=, /=, %=, **=, //=.
    Bitwise operators: &, |, ^, ~, <<, >>.
    Strings: Strings can be enclosed in single or double quotes. You can use the + operator to concatenate strings.
"""
# FOR EXAMPLE here we use + to concatinate
first_name = "Abdulla"
last_name = "Abdul Raoof"
full_name = first_name+" "+last_name
print(full_name)
#5. control flow which means when we encounter an condition(true or false) we use control flow.
"""
    1. if else
    2. For loops
    3. While loops
"""
# for example
num =  10
if num>=10:
    print(f"{num}, is larger") # use f{} to access var in print
else:
    print(f"{num} is not larger")
#6. Function it make repeaten block of code into single
def name(name): # here i need to call function whenever i need to print the nmae don't need to write bloack of code
    print(f"{name}")

name("Abdulla")

"""
Summary
    1.hello world
    2.variable
    3.operations
    4.control flow
    5.function
"""