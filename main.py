from exercises import *
import exercises
import sys




while(True):
  print("Welcome to Zeus's coding exercises which would you like to view(type the exercise number)")
  for item in exercises.modules:
    if not item.endswith("__init__.py"):
      print(item[41:-3])

  selection = input()

  while (selection not in [str(a) for a in range(1,len(exercises.modules))]):
    selection = input()

  print(getattr(sys.modules["exercises.exercise_" + selection], "name"),getattr(sys.modules["exercises.exercise_" + selection], "description"))
    
  print("\nWould you like to execute " + getattr(sys.modules["exercises.exercise_" + selection], "name") + "?" + "\nY/N")

  choice = input()

  vaild_options = ("y","n")

  while choice.lower() not in vaild_options:
    choice = input()

  if (choice == "y" or choice == "Y"):
    getattr(sys.modules["exercises.exercise_" + selection], "run_exercise")()

  print("\nWould you like to exit y/n")

  exit = input()

  while exit.lower() not in vaild_options:
    exit = input()

  if (exit == "y" or exit == "Y"):
    break