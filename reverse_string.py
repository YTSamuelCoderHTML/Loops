string = input("Enter a random string so it can be reversed:")

string2 = ('')

for i in string:
    string2 = i + string2

print("\n The real string was:", string)
print("The reversed string is:", string2)