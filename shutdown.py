import os

shutdown = input("Do you want to shutdown your computer? Please enter Yes or No: ")

if shutdown == "no" or shutdown == "No":
    exit()
else:
    os.system("shutdown /s /t 1")