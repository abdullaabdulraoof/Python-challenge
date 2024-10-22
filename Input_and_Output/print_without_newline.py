import sys
# in when we print two statement it will automatically go to newline
# example
print("Abdulla")
print("Abdul Raoof")# here this will pront in new line
# now use end
print("Abdulla",end = " ")
print("Abdul Raoof")

#NEXT WE CAN USE JOIN() METHOD
words = ["Abdulla","Abdul Raoof"]
print(" ".join(words))

# we can print array using *
l = [1,2,3,4]
print(*l)

sys.stdout.write("hello world ")
sys.stdout.write("hello world")