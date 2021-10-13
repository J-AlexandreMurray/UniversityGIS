


age = int(input("Enter age: "))
gender = input("Enter gender (Male / Female)? ").lower()
if(age < 18 or age > 65):
    while(gender!="male" and gender!="female"):
        gender = input("Enter gender (Male / Female)? ")
print("Your age:",age,", and gender:",gender)