name = "Help me print"
description = "Helps you print 3 numbers between 1 and 10 to the console"


def run_exercise():
  numbers = []
  for item in range (1,4):
    
    

    number = input("number please\n")
      
    while(number not in [str(a) for a in range(0,11)]):
      print("oop thats not a number between 1 and 10 try again :)")
      number = input()
    
    if(item < 3):
      print("thank you " + str(3 - item) + " more numbers to go")
    else:
      print("thats all the numbers I need")

    numbers.append(number)
  
  print("here are your numbers ")

  for item in numbers:
    print(item)
    
  file = open("file.txt", "a")
  for item in numbers:

    file.write(item)
    file.write("\n")
  file.write("\n")
  file.close()