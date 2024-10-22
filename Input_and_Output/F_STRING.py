import datetime
#Today we are going to sudy about fstring simple way to to acces variables in print function
name = "Abdulla"
age = 10
print(f"{name} is human and his age is {age}")

# using dateandtime module
today = datetime.datetime.today()
print(f"{today:%B %d, %Y}")

# printing quotation mark in fstring
print(f"'GeeksforGeeks'")

print(f"""Geeks"for"Geeks""")

print(f'''Geeks'for'Geeks''')

# we can evaluate using an fstring
a = 10
b = 20
c = 100
print(f"Sum = {a+b+c} ")
# printing dictionary key values
student = {
    "Name": "Abdulla",
    "age": 19
}
print(f"Name is {student['Name']} and his age is {student['age']}")