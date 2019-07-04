# This is a calender keeping track of events and setting reminders for the user in an interactive way
from time import sleep,strftime
your_name = raw_input("Please enter your name: ")
calender = {}
def welcome():
  print "Welcome " + your_name
  print "Calender is opening"
  print strftime("%A, %B, %d, %Y")
  print strftime("%H:%M:%S")
  sleep(1)
  print "What would you like to do?"

def start_calender():
  welcome()
  start = True
  while start == True:
    user_choice = raw_input("Please enter A to Add, U to Update, V to View , D to Delete and X to Exit")
    user_choice = user_choice.upper()  
    if user_choice =="V":
      if len(calender.keys()) < 1:
        print "Calender is empty"
      else:
        print calender
    elif user_choice == "U":
      date = raw_input("What date? ")
      update = raw_input("Enter the update: ")
      calender[date] = update
      print "Update successful!"
      print calender
    elif user_choice == "A":
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY)")
      if len(date) > 10 or len(date) < 10 or int(date[6:]) < int(strftime("%Y")):
        print "Invalid date was entered"
        try_again = raw_input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == "Y":
          continue
        else:
          start = False
      else:
        calender[date] = event
        print "Event was successfully added."
    elif user_choice == "D":
      if len(calender.keys()) < 1:
        print "Calender is empty"
      else:
        event = raw_input("What event? ")
        for date in calender.keys():
          if event == calender[date]:
            del calender[date]
            print "Event was successfully deleted"
          else:
            print "Incorrect event was specified"
    elif user_choice == "X":
      start = False
    else:
      print "Invalid command was entered"
      exit()

start_calender()      
          