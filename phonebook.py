"""
names= ["Berra","Behnan","Enes"]
name= input("Name: ")
""
for n in names:
    if n == name:
        print("Found")
        break
else: #the indentation here is so important
    print("Not found")
""
if name in names:
    print("Found")
else:
    print("Not found")
"""
