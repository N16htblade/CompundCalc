from os import path
import datetime

#User register section:
user = input("Please enter Username: ")
x = datetime.datetime.now()
xtime = x.strftime("%c")

if path.exists('%s.txt' %user):
    with open('%s.txt' %user, 'a+') as a:
        a.write("%s logged in: %s\r" %(user, xtime) )
else:
    usernamecheck = input("This username does not exist, would you like to create it? (Yes/No): ")
    if usernamecheck == ("Yes"):
         with open('%s.txt' %user, 'w+') as a:
            a.write("%s's account created: %s\r" %(user, xtime))
    else:
        quit()

# Calculator section:
def CheckInput (testInput):
    x = input(f"Please enter your current {testInput} value: ")
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

print (f"We estimate you will reach a value of {investmentAccount} in {year} Years")

#User history section:
with open('%s.txt' %user, 'a+') as a:
        a.write("Current Account %d\r" %currentAccount)
        a.write("Anual Contribution %d\r" %anualContribution)
        a.write("Final account %d\r" %finalAccount)
        a.write("Estimated time %d\r\n" %year)
