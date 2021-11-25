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

bakjePrijs = 0.75
cone = 0
cup = 0

bolletjesPrijs = 1.10
horrentjesPrijs = 1.25
                                           
def iceCream():
    choice = ""
    coneOrCup = ""
    global cone
    global amount
    global cup
    print_slow("Welcome in Papi Gelato.\n")
    flavour = input("What flavour would you like with that?\n ⚫ Strawberry.\n ⚫ Chocolate.\n ⚫ Mint.\n ⚫ Vanille.\n").lower()
    amount = int(input("How many ice cream balls would you like?\n"))
    if amount <= 3:
        coneOrCup = input(f"Do you want your {amount} {flavour} ice cream balls in a cone or cup?\n")
    elif amount <= 8:
        print_slow(f"You will get a cup with {amount} {flavour} ice cream balls inside.\n")
        cup = 1
    elif amount > 8:
        print_slow("Sorry, we dont have bigger cups.\n") 
        clearScreen(1)
        iceCream()
    bolletjesKosten = amount * bolletjesPrijs
    if coneOrCup == "cone":
        cone = 1
    elif coneOrCup == "cup":
        cup = 1
    bakjeKosten = bakjePrijs * cup
    horrentjesKosten = horrentjesPrijs * cone
    total = horrentjesKosten + bakjeKosten + bolletjesKosten
    print(f"\n  --------[Papi Gelato]-------- \n\n Balls   {amount} X {bolletjesPrijs} = {bolletjesKosten}\n Cones   {cone} X {horrentjesPrijs} = {horrentjesKosten}\n Cup     {cup} X {bakjePrijs} = {bakjeKosten}\n-----------------------------\n Total              {total}\n")
    choice = input(f"Here is your {coneOrCup} with {amount} {flavour} ice cream balls. Do you want to order again? (Y/N)\n").lower()
    if choice == "y":
        clearScreen(1)
        iceCream()
    elif choice == "n":
        print_slow("Thank you and see you again!\n")
        clearScreen(2)
    else:
        print_slow("Sorry i didnt understand that.\n")

iceCream()