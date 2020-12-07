name = "a new student"
description = "A program that takes in a students name, age and nationality and outputs it to a text file and the console"

class student:
  def __init__(self, name, age, nationality):
    self.name = name
    self.age = age
    self.nationality = nationality
    self.content = [self.name, self.age, self.nationality]

def run_exercise():
  new_student = student(input("Name\n"),input("Age\n"),input("Nationality\n"))

  for item in new_student.content:
    print(item)

  file = open("file.txt", "a")
  for item in new_student.content:

    file.write(item)
    file.write("\n")
  file.write("\n")
  file.close()