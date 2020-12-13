from exercises import *
import exercises
import sys




while(True):
  names = []
  print("Welcome to Zeus's coding exercises which would you like to view(type the exercise number)")
  for item in exercises.modules:
    if not item.endswith("__init__.py"):
        names.append(item[43:-3] + " " + getattr(sys.modules["exercises.exercise_" + item[-4:-3]], "name"))

  names.sort()
  for item in names:
    print(item)

  selection = input()

  while (selection not in [str(a) for a in range(1,len(exercises.modules))]):
    selection = input("please select a number between 1 and" + " "+ str(len(exercises.modules)-1) + "\n")

  print("\n" + getattr(sys.modules["exercises.exercise_" + selection], "name") + ":" + "\n",getattr(sys.modules["exercises.exercise_" + selection], "description"))
    
  print("\nWould you like to execute " + getattr(sys.modules["exercises.exercise_" + selection], "name") + "?" + "\nY/N")

  choice = input()

  vaild_options = ("y","n")

  while choice.lower() not in vaild_options:
    choice = input()

  if (choice == "y" or choice == "Y"):
    while(True):
      print("\n") 
      getattr(sys.modules["exercises.exercise_" + selection], "run_exercise")()
      print("\nWould you like to run this again?Y/N")

      valid_inputs = ("y","n")

      choice = input()

      while choice.lower() not in valid_inputs:
        choice = input()
    
      if (choice.lower() == "n"):
        break

  print("\nWould you like to exit Y/N")

  exit = input()

  while exit.lower() not in vaild_options:
    exit = input()

  if (exit == "y" or exit == "Y"):
    break
