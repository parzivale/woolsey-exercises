import re

name = "Grade me"
description = "input a decimal score and it outputs a grade"

def run_exercise():

  grade = input("What grade did you get\n")
    
  while not re.match("^(100)$|^[0-9]{1,2}$|^[0-9]{1,2}\.+[0-9]+$",grade):
    grade = input("That doesn't seem like a vaild grade please try again\n")

  grade = float(grade)

  if (grade >= 80):
    print("You got an A\nExcellent result")
  elif(grade >= 70):
    print("You got a B\nVery good")
  elif(grade >= 60):
    print("You got a C\nGood effort")
  elif(grade >= 50):
    print("You got a D\nYou achieved a Pass")
  elif(grade <= 49):
    print("You got a U\nWould you like to book a retake?")
    valid_inputs = ("y","n")

    choice = input()

    while choice.lower() not in valid_inputs:
      choice = input("please enter \"Y\" or \"N\"")
    
    if (choice.lower() == "y"):
        print("Retake booked for tommorow at 2pm")
    if (choice.lower() == "n"):
      print("You will need to book again later")
    
