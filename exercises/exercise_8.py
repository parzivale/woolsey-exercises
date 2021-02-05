import re

name = "Ticket booker"
description = "A program that prints the amount of tickets you want"

def run_exercise():
  amount = input("How many tickets would you like?\n")

  while not re.match("^[0-9]+$", amount) or int(amount) == 0:
       amount = input("That's not a vaild number of tickets! try again\n")
  

  for number in range(1,int(amount) + 1):
    print("Ticket number " + str(number) + " booked\n")