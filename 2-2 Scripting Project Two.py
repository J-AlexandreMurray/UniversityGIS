
# Python 2-2 Scripting Project Two
# This code is meant as an exercise to expand on the previous scripting project,
# where it allows the user to enter data for as many individuals as they would like
# as well as provide the user with a functional way to exit the program interface
# The information must now print the number of males and females as well as the average age of both males and females

def main():

countMale=0

countFemale = 0



while True:  # infinite loop

  name = input("Enter the User Name : ")

	Gender = input("Enter the User gender : ")

	Age = (int(input("Enter the User Age")))

	if Gender == "Male" || Gender =="male" :

		countMale++

	elif Gender == "Female" || Gender =="female" :

		countFemale++



  n = raw_input("\n\nWant to Enter again individuals data Press Y/y: ")

  if n == "Y" || n == "y":

    break # stops the loop

  elif n == "True":





main():
