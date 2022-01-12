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

reciept = [""]

A,B,C,D = False,False,False,False
zakelijk1 = False
particulier = False
smaakLiter = 0

toppingPrice = 0
bakjePrijs = 0.75
cone = 0
cup = 0
bolletjesPrijs = 0.95
horrentjesPrijs = 1.25
literLijst = []
x = 1
reciept = f'--------[Papi Gelato]--------\n'
total = 0
                                           
def iceCream():
    choice = ""
    coneOrCup = ""
    global cone
    global amount
    global cup
    global toppingPrice
    global toppings

    clearScreen(0)
    print_slow("Welcome in Papi Gelato.\n")
    zakelijk = input("What do you need it for?:\n 1. Private\n 2. For business\n")
    clearScreen(1)
    if zakelijk == "1":
        zakelijk1 = True
        amount = int(input("How many ice cream balls would you like?\n"))
        clearScreen(1)
        if amount <= 8:
            i = 1
            while i <= amount: 
                flavour = input("What ice cream taste would je like for the " + str(i) + "\n 1. Strawberry.\n 2. Chocolate.\n 3. Vanille.\n")
                clearScreen(1)
                if int(flavour) >= 1 and int(flavour) <= 3:
                    i += 1
                else:
                    print_slow("Sorry we dont have that.")
                    i += 0
                    clearScreen(2)
                    iceCream()   
        else:
            print_slow("Sorry, we dont have bigger cups.\n") 
            clearScreen(1)
            iceCream() 
        if amount <= 3:
            coneOrCup = input(f"What would you like your ice cream ball(s) in? A cup or a cone?\n")
        elif amount <= 8:
            print_slow(f"You will get a cup with {amount} ice cream balls inside.\n")
            cup = 1
        elif amount > 8:
            print_slow("Sorry, we dont have bigger cups.\n") 
            clearScreen(1)
            iceCream()
        else:
            print("Sorry, thats not a option that we have.")
            clearScreen(2)
            iceCream()           
        clearScreen(1)
        clearScreen(1)
        bolletjesKosten = round(amount * bolletjesPrijs,2)
        if coneOrCup == "cone":
            cone = 1
        elif coneOrCup == "cup":
            cup = 1
        bakjeKosten = bakjePrijs * cup
        horrentjesKosten = horrentjesPrijs * cone
        toppings = input("What kind of toppings would you like?\n A. Nothing\n B. Cream\n C. Sprinkels\n D. Carmel\n").lower()
        if toppings == "a":
            A = True
        elif toppings == "b":
            B = True
        elif toppings == "c":
            C = True
        elif toppings == "d":
            D = True    
        if toppings == "a":
            toppingPrice = 0
        elif toppings == "b":
            toppingPrice = 0.50
        elif toppings == "c":
            toppingPrice = 0.30 * amount
        elif toppings == "d":
            if cone == 1:
                toppingPrice = 0.60
            else:
                toppingPrice = 0.90
        else:
            print("Sorry i didnt quite get that\n")
            clearScreen(2)
            iceCream()
        clearScreen(1)
        choice = input(f"Here is your order with {amount} ice cream balls. Do you want to order again? (Y/N)\n").lower()
        global reciept,x
        reciept += f"ijsje {x}\nBalls   {amount} X {format(bolletjesPrijs,'.2f')} = {format(bolletjesKosten,'.2f')}\n {'Cones   '+cone+' X '+str(format(horrentjesPrijs,'.2f'))+' = '+str(format(horrentjesKosten,'.2f')) if cone > 0 else ''} Cup     {cup} X {format(bakjePrijs,'.2f')} = {format(bakjeKosten,'.2f')}\n Topping 1 X {format(toppingPrice,'.2f')} = {format(toppingPrice,'.2f')}\n-----------------------------\n"
        if choice == "y":
            global total
            x+=1
            total += horrentjesKosten + bakjeKosten + bolletjesKosten + toppingPrice
            clearScreen(1)
            iceCream()
        elif choice == "n":
            print_slow("Thank you and see you again! Here is your reciept\n")
            total += horrentjesKosten + bakjeKosten + bolletjesKosten + toppingPrice
            print(f'{reciept} \n total {total}')
            #clearScreen(5)
        else:
            print_slow("Sorry i didnt understand that.\n")
    elif zakelijk == "2":
        liters = int(input("How many liters of ice cream do you need?\n"))
        clearScreen(1)
        i = 1
        while i <= liters:
            literSmaak = input("What ice cream taste would je like for the " + str(i) + "\n 1. Strawberry.\n 2. Chocolate.\n 3. Vanille.\n")
            clearScreen(2)
            if int(literSmaak) >= 1 and int(literSmaak) <= 3:
                i += 1
            else:
                print_slow("Sorry we dont have that.")
                i += 0
                clearScreen(2)
                iceCream()
        clearScreen(1)
        literKosten = liters * 9.80
        btw = (literKosten / 106) * 6 
        print(f"--------[Papi Gelato]--------\n\nLiter  {liters} X €9,80 = {format(literKosten,'.2f')}\n                -------\nTotale           = {format(literKosten,'.2f')}(9%) BTW         = {format(btw,'.2f')} \n\n----------------------------- ")
        choice = input(f"Here is your order with {liters} liters of ice cream. Do you want to order again? (Y/N)\n").lower()
        if choice == "y":
            clearScreen(1)
        elif choice == "n":
            print_slow("Thank you and see you again!\n")
            clearScreen(2)
        else:
            print_slow("Sorry i didnt understand that.\n")
    else:
        print("Sorry, thats not a option that we have.")
        clearScreen(2)
        iceCream()


iceCream()