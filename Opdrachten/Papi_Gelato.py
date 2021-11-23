# 99058235 Mert Erciyas
import time,os,sys

def clearScreen(sleepTime):
    time.sleep(sleepTime)
    os.system("cls")

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        #time.sleep(0.05)

def iceCream():
    choice = ""
    print_slow("Welcome in Papi Gelato you can choose any taste of ice cream but it has to be vanille ice cream.\n")
    amount = int(input("How many ice cream balls would you like?\n"))
    if amount <= 3:
        coneOrCup = input(f"Do you want your {amount} ice cream in a cone or cup?\n")
    elif amount <= 8:
        print_slow(f"You will get a cup with {amount} ice cream balls inside.\n")
    elif amount > 8:
        print_slow("Sorry, we dont have bigger cups.\n") 
        clearScreen(1)
        iceCream()
    choice = input(f"Here is your {coneOrCup} with {amount} ice cream balls. Do you want to order again? (Y/N)\n").lower()
    if choice == "y":
        clearScreen(1)
        iceCream()
    elif choice == "n":
        print_slow("Thank you and see you again!\n")
    else:
        print_slow("Sorry i didnt understand that.\n")

iceCream()