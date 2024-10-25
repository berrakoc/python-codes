"""
from cs50 import get_int
x= get_int("x: ")  #1
y= get_int("y: ")  #1

print(x + y)  #2


x= input("x: ")  #1
y= input("y: ")  #1

print(x + y)  #11

x= int(input("x: "))  #1
y= int(input("y: "))  #1

print(x + y)  #2
"""
"""
x= int(input("x: "))
y= int(input("y: "))

z= x/y
print(f"{z:.50f}")
"""
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError: #you can try to type 'cat' as a input
            print("Not an integer") #pass

def main():
    x= get_int("x: ")
    y= get_int("y: ")
    print (x+y)

main() #need to call main func
