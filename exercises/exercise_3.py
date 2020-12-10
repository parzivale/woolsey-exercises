import re

name = "Celsius to fahrenheit"
description = "Converts celsius to farenheight or vice versa"

def run_exercise():
  while(True):
    print("convert from celsius(c) or fahrenheit(f), type c or f below")

    choice = input()

    valid_options = [("c","f"), ("y","n")]

    while choice.lower() not in valid_options[0]:
      choice = input()
    
    temp = input("whats the temperature\n")

    while not(re.match("^[0-9]+\.+[0-9]+$|^[0-9]+$", temp)):
      temp = input("that doesnt seem right try again\n")

    if choice.lower() == "c":
      print(float(temp)/5*9+32)
    
    if choice.lower() == "f":
      print((float(temp)-32)*5/9)
    
    while choice not in valid_options[1]:
        choice = input("would you like to convert another temperature\n")
    if choice.lower() == "n":
      break
    

