import re

name = "Cash register simulated"
description = "A virual cash register"




def run_exercise():
  while(True):

    price = input("price of the item\n")

    while not re.match("^[0-9]+\.+[0-9]$|^[0-9]+\.+[0-9][0-9]$|^[0-9]+$",price):
      price = input("that doesn't seem like a vaild price please try again\n")

    cash_given = input("payment\n")
    
    while not re.match("^[0-9]+\.+[0-9]$|^[0-9]+\.+[0-9][0-9]$|^[0-9]+$",cash_given):
      cash_given = input("that doesn't seem like a vaild input please try again\n")
    
    while float(cash_given) < float(price):
      cash_given = input("thats not enough for this item please insert more money\n")

    if float(cash_given) >= float(price):
      print("transaction completed thank you for shopping with us\n")
      if (float(cash_given) > float(price)):
        print("here is your change " + str(round(float(cash_given) - float(price),2)))

