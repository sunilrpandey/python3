import time
import webbrowser
from datetime import datetime

def CreateTimerApp():
    print("Enter number of mins : ")
    min_c = int(input())
    seconds_c = min_c * 60
    print("Your time start now : ")
    for i in range(seconds_c,1,-1):
        time.sleep(1)
        print("Time remaining : %3d" % i, end = "\r")
    webbrowser.open("https://www.youtube.com/watch?v=ADYP32VV-ak&t=1781s")
    

currentDateAndTime = datetime.now()
print("The current date and time is", currentDateAndTime)
currentTime = currentDateAndTime.strftime("%H:%M:%S")
print("Time Now : ", currentTime)
print(datetime.today().strftime("%I:%M %p"))
#CreateTimerApp()



