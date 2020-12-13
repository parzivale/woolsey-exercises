name = "Hooray for weekend"
description = "Type in the day of the week and if its the weekend print \"Hooray\"" 

def run_exercise():
  day = input("What day of the week is it(in three letter format i.e(mon, tue, etc)\n")

  valid_options = ("mon","tue", "wed","thu","fri","sat","sun")

  while day.lower() not in valid_options:
    day = input("Thats not a day of the week try again(use the three letter format)\n")

  if(day.lower() == valid_options[5] or day.lower() == valid_options[6]):
    print("Hooray - it's the weekend\n")
  else:
    print("Bad luck back to your studies\n")