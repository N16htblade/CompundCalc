import os
import sys
import datetime
import csv

#User register section:
user = input("Please enter Username: ")
if os.path.exists(os.path.join(sys.path[0], '%s.csv') %user):
    print (f"Welcome back {user}, here is a new calculator:")
    breakpoint
else:
    usernamecheck = input("This username does not exist, would you like to create it? (Yes/No): ")
    if usernamecheck == ("Yes"):
         with open(os.path.join(sys.path[0], '%s.csv') %user, 'w', newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(["date", "currentAccount", "anualContribution", "finalAccount", "year"])
    else:
        quit()

# Calculator section:
def CheckInput (testInput):
    x = input(f"Please enter your {testInput} value: ")
    while True:
        try:
            x = int(x)
        except ValueError:
            x = input("This is not a valid number, please try again: ")
        else:
            return x

currentAccount = CheckInput("Current Account")
anualContribution = CheckInput("Anual Contribution")
finalAccount = CheckInput("Final Account")
estimatedGrowth = 1.07
year = 1
investmentAccount = currentAccount
while investmentAccount < finalAccount:
    investmentAccount += anualContribution
    investmentAccount *= estimatedGrowth
    investmentAccount = round (investmentAccount)
    year += 1
x = datetime.datetime.now()
xtime = x.strftime("%c")

print (f"We estimate you will reach a value of {investmentAccount} in {year} Years")

#User history section:
with open(os.path.join(sys.path[0], '%s.csv') %user, 'a', newline="") as csv_file:
    writer = csv.writer(csv_file, delimiter=",")
    writer.writerow([xtime, currentAccount, anualContribution, finalAccount, year])