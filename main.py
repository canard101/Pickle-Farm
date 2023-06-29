try:
    from replit import db
except:
    pass
from time import sleep as s
import platform
import os
from os import system as cmd
from random import randint, choice

def clear(): # Cross-platform console clearer
  ostype = platform.system()
  if ostype == "Linux" or ostype == "Darwin":
    cmd("clear")
  else:
    cmd("cls")

def w():
    s(0.2)

""" ANSI color codes """
BLACK = "\033[0;30m"
RED = "\033[0;31m"
G = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"


class player:
    money = 10
    inv = []
    name = ""
    pickles = 0
    seeds = 0
    day = 0
    picklesType = "basic"
    festNbr = 0

    a = 5
    b = 15


class planted:
    phase1 = 0
    phase2 = 0
    phase3 = 0
    phase4 = 0
    phase5 = 0
    phase6 = 0
    phase7 = 0
    
    growing = phase1+phase2+phase3+phase4+phase5+phase6

sellPrice = 0

def choose():
    cities = ["Montgomery", "Juneau", "Phoenix", "Little Rock", "Sacramento", "Denver", "Hartford", "Dover", "Tallahassee", "Atlanta", "Honolulu", "Boise", "Springfield", "Indianapolis", "Des Moines", "Topeka", "Frankfort", "Baton Rouge", "Augusta"]
    x = choice(cities)

    return x

class events:
    events = ["events.disease()" "events.extraSeeds()", "events.storm()", "events.festival()", "events.stocksMarketUp()", "events.stocksMarketDown()"]
    
    def disease():
        print("Oh no!\n It looks like your growing pickles have all been infected by a disease.\nIt would be illegal to not destroy your pickles, but the government might not find out about it.\nYou've gotta choose :")
        ch = input("1 : Keep my infected pickles\n2 : Ask the government for help to destroy them\n> ")
        if ch == "1":
            print("You chose to keep your pickles.")
            if randint(0, 1) == 1:
                print("And you got away with it!\nNow, try not thinking too much about the diarrhea people will get by eating your pickles.")
                input("\nPress enter to continue./")
            else:
                print("But the government found out!\nYou've got to pay a fine of $5")
                player.money -= 5
                input("\nPress enter to continue./")
        else:
            print("You chose to destroy your pickles with the help of the government\nThey gave you $10 so you can buy seeds again")
            planted.phase1 = 0
            planted.phase2 = 0
            planted.phase3 = 0
            planted.phase4 = 0
            planted.phase5 = 0
            planted.phase6 = 0
            planted.phase7 = 0
            player.money += 10
            input("\nPress enter to continue./")
    
    def storm():
        print("\nOh no !\n", G, "50%", END, "of your growing pickles got destroyed because of a storm")
        planted.phase1 = int(planted.phase1 / 2)
        planted.phase2 = int(planted.phase2 / 2)
        planted.phase3 = int(planted.phase3 / 2)
        planted.phase4 = int(planted.phase4 / 2)
        planted.phase5 = int(planted.phase5 / 2)
        planted.phase6 = int(planted.phase6 / 2)
        planted.phase7 = int(planted.phase7 / 2)
        left_pickles = planted.phase1+planted.phase2+planted.phase3+planted.phase4+planted.phase5+planted.phase6+planted.phase7
        print("You now have", G, left_pickles, END, "left pickles...")
        print("\nBUT !  The government is ready to help you !\nSo they gave you", G, "$5.",  END)
        player.money += 5
        del left_pickles
        input("\nPress enter to continue./")
        
    def festival():
        player.festNbr += 1
        wage = randint(20, 60)
        print("\nYay ! ")
        print("Today is the", player.festNbr, "th Pickles Festival of ", choose(), " !")
        print("They invited you to hold a booth for", G, "$" + str(wage), END, " !")
        player.money += wage
        input("\nPress enter to continue./")

    def stocksMarketUp():
        #global player
        add = randint(1, 15)
        player.a += add
        player.b += add
        print("\nThe pickles stocks market went up !\nYou can now sell your pickles in a range from", G, "$" + str(player.a), END, "to", G,  "$" + str(player.b), END, "!")
        input("\nPress enter to continue./")

    def stocksMarketDown():
        #global player
        sub = randint(1, 15)
        player.a -= sub
        player.b -= sub
        print("\nOh no !\nThe pickles stocks market went down...\nNo one wants to buy pickles for more than",G, "$" + str(player.b), END, "now.\nYou can now sell your pickles in a range from", G, "$" + str(player.a), END, "to", G,  "$" + str(player.b), END)
        input("\nPress enter to continue./")
        
    def extraSeeds():
        print("\nYour seeds supplier has extra seeds and decides to give it to you !\nYou got", G, "5", END, "seeds !")
        player.seeds += 5
        input("\nPress enter to continue./")

    def taxes():
        if player.money == 0:
            pass
        else:
            toPay = player.money/5
            print("\nHey hey hey !\nIt's taxes time !\nYou owe ", G, "$", toPay, END, "to the government\nAnd you're gonna pay it because you're a good citizen !")
            input("\nPress enter to pay./")
            player.money -= toPay
        
def save(name):
    
    try:
        from replit import db
    except:
        pass
    
    db["PCK_"+name] = player.pickles
    db["MNY_"+name] = player.money
    db["SDS_"+name] = player.seeds

    print("\nYou've saved the game to the name ", G, name, END, " !")

def load(name):

    try:
        from replit import db
    except:
        pass
    player.money = db["MNY_"+name]
    player.pickles = db["PCK_"+name]
    player.seeds = db["SDS_"+name]

    del db["MNY_"+name]
    del db["PCK_"+name]
    del db["SDS_"+name]

    print("\nYou've loaded the game with the name ", G, name, END, " !")
    
def crops():
    print("\n• Tomorrow's crop : ", G, planted.phase6, END)
    print("• Crops in 2 days : ", G, planted.phase5, END)
    print("• Crops in 3 days : ", G, planted.phase4, END)
    print("• Crops in 4 days : ", G, planted.phase3, END)
    print("• Crops in 5 days : ", G, planted.phase2, END)
    print("• Crops in 6 days : ", G, planted.phase1, END)
    print("\nTOTAL OF GROWING PICKLES : ", G, planted.phase1+planted.phase2+planted.phase3+planted.phase4+planted.phase5+planted.phase6, END)

def buySeeds(amount, seedPrice):
    if player.money < amount*seedPrice:
        print("\nYou don't have the money to do that! You can only buy ", G, int(player.money/seedPrice), END, " seeds!\n")
        pass
    else:
        player.money -= amount*seedPrice
        player.seeds += amount
        print("\nYou bought ", G, amount, END, " seeds !\nYou now have ", G, player.seeds, END, "seed(s) and ", G, player.money, END, "$.")

def plant(amount):
    if player.seeds == 0:
        print("\nYou don't have any seeds!\n")
        pass

    if player.seeds != 0:    
        if amount == "all":
            planted.phase1 += player.seeds
            print("\nYou planted ", G, player.seeds, END, " pickle(s) !")
            print("You now have ", G, str(planted.phase1+planted.phase2+planted.phase3+planted.phase4+planted.phase5+planted.phase6), END, " pickles growing.")
            player.seeds = 0

        if player.seeds < int(amount):
            print("You don't have that much of seeds ! You can only plant ", G, player.seeds, END, " seeds!")
            pass
        
        else:
            player.seeds -= int(amount)
            planted.phase1 += int(amount)
            print("\nYou planted ", G, amount, END, " pickles !")  
            print("You now have ", G, planted.phase1+planted.phase2+planted.phase3+planted.phase4+planted.phase5+planted.phase6, END, " pickles growing.")

def harvest(amount):
    if planted.phase7 == 0:
        print("\nYou don't have any pickle ready to be harvested!\n")
        pass

    if planted.phase7 != 0:    
        if amount == "all":
            player.pickles += planted.phase7
            print("\nYou harvested ", G, planted.phase7, END, " pickle(s) !")
            planted.phase7 = 0

        if planted.phase7 < int(amount):
            print("You don't have that much pickles to harvest ! You can only harvest ", G, planted.phase7, END, " pickle(s)!")
            pass

        else:
            planted.phase7 -= int(amount)
            player.pickles += int(amount)
            print("\nYou harvested ", G,  amount, END, " pickles !")  
            print("You now have ", G, player.pickles, END, " pickle(s) !")

def sell(amount):
    print("\nThe price of pickles is $", G, sellPrice, END, "today!")
    if player.pickles == 0:
        print("\nYou don't have any pickles to sell !\n")
        pass

    if player.pickles != 0:    
        if amount == "all":
            ch = input("\nAre you sure you want to sell your pickles? > ")
            
            if ch == "yes":
                player.money += (player.pickles*sellPrice)
                print("\nYou sold ", G, player.pickles, END, " pickle(s) !")
                player.pickles = 0
                print("You now have ", G, player.money, END, " $ and ", G, player.pickles, END, " pickle(s).")
                
            else:
                print("\nOk, maybe another day!")
                pass
            
        elif player.pickles < int(amount):
            print("You don't have that much pickles to sell ! You only have ", G, player.pickles, END, " pickle(s)!")
            pass
            
        else:
            ch = input(f"\nAre you sure you want to sell {amount} pickles? > ")
            
            if ch == "yes":
                player.money += (player.pickles*sellPrice)
                print("\nYou sold ", G, player.pickles, END, " pickle(s) !")
                player.pickles -= int(amount)
                print("You now have $", G, player.money, END, " and ", G, player.pickles, END, " pickle(s).")
                
            else:
                print("\nOk, maybe another day!")
                pass

def checkDebt():
    if player.money <= 0 and player.pickles == 0 and player.seeds == 0 and planted.phase1+planted.phase2+planted.phase3+planted.phase4+planted.phase5+planted.phase6+planted.phase7 == 0:
        print("Your pickle farm went bankrupt.\nYou don't have anymore money, or pickles, or seeds.\nYou will have to start a new career in another industry.")
        print("\nY O U     L O S T")
        input("\n\nPress enter to quit./")
        quit()
    elif player.money <= 0 and player.pickles == 0 and player.seeds > 0:
        print("Hey! You've got to plant your seeds RIGHT NOW if you don't wanna go bankrupt!")
    elif player.money <= 0 and player.pickles > 0:
        print("Hey: You've got to sell your pickles RIGHT NOW if you don't wanna go brankrupt!")
    else:
        pass
                
    
def newDay():
    """
    Create a new day
    """
    global sellPrice
    event = randint(1, 6)
    sellPrice = randint(player.a, player.b)
    #print(event) #
    if event == 3 and player.day > 0:
        eval(choice(events.events))
    print("\n\n")
    dayEnded = False
    player.day += 1
    # Growing pickles
    planted.phase7 += planted.phase6
    planted.phase6 = 0
    planted.phase6 += planted.phase5
    planted.phase5 = 0
    planted.phase5 += planted.phase4
    planted.phase4 = 0
    planted.phase4 += planted.phase3
    planted.phase3 = 0
    planted.phase3 += planted.phase2
    planted.phase2 = 0
    planted.phase2 += planted.phase1
    planted.phase1 = 0
    c = player.day
    print("\nDay : ", G, c, END)       
    print("="*len("Day : "+str(c)))
    s(0.3)
    print(G, player.money, END, "$")
    s(0.3)
    print("Pickles : ", G, f"{player.pickles} ", END)  
    s(0.3)
    print("Seeds : ", G, f"{player.seeds}", END)   
    checkDebt()  
    if planted.phase7 != 0:
        s(0.5)
        print("\nYou have ", G, planted.phase7, END, " pickles ready to be harvested !\nAnd you have currently ", G, planted.phase1+planted.phase2+planted.phase3+planted.phase4+planted.phase5+planted.phase6, END, "pickles growing.")

        if planted.phase6 != 0:
            print("TOMORROW'S HARVEST : ", G, planted.phase6, END, " pickles.")
    else:
        s(0.5)
        
        print("\nYou have currently ", G, planted.phase1+planted.phase2+planted.phase3+planted.phase4+planted.phase5+planted.phase6, END, "pickles growing.")

        if planted.phase6 != 0:
            print("\nTOMORROW'S HARVEST : ", G, planted.phase6, END, " pickle(s).")
    
    if player.day == 1:
        print("\nType 'help' to see what you can do.")
    while dayEnded is False:
        ch = input("\n\n> ")
        if len(ch) == 0 or len(ch.strip()) == 0:
            print("\nType a command!")
        if "help" in ch.lower():
            print("\n\n")
            print("COMMANDS")
            print("\n- inventory : Check your inventory")
            print("- buy seeds [amount]: Buy pickle seeds (5$ each).")
            print("- plant [amount] : Plant pickles seeds")
            print("- sell [amount] : Sell pickles.")
            print("- end : End the day.")
            print("- help : Show the help menu.")
            print("- crops : to see the prediction of your future crops !")
            print("(replace the word [amount] by a number or 'all')")
            
        if "buy seeds" in ch.lower():
            try:
                buySeeds(int(ch[10:]), 5)
            except ValueError:
                if ch[10:] == "":
                    print("\nPlease enter a valid amount!")
                    print("\nYou can buy ", G, int(player.money/5), END, " seeds.")
                    
        if ch == "inventory":
                print("\n")
                if player.inv == []:
                    print("\nYou don't have anything in your inventory.")
                else:
                    for a in player.inv:
                        print(a, ", ")
                        
        if ch.startswith("plant"):
            try:
                if ch[6:] == "all":
                    plant("all")
                    
                plant(int(ch[6:]))
                
            except ValueError:
                if ch[6:] != "all":
                    print("\nPlease enter a valid amount!")
        if ch.lower() == "end day" or ch.lower() == "end":
            newDay()

        if ch.startswith("harvest"):
            try:
                if ch[8:] == "all":
                    harvest("all")
                    
                harvest(int(ch[8:]))

            except ValueError:
                if ch[8:] == "all":
                    pass
                else:
                    print("\nPlease enter a valid amount!")

        if ch.lower() == "save":
            print("\nSAVE")
            print("====")
            print("Saving your game will permit you to resume it whenever you want ! ")
            x = input("\nOn what name do you want to save the game ? > ")
            save(x)

        if ch.lower() == "load":
            print("\nLOAD")
            print("====")
            print("Load a game you've saved before ! ")
            x = input("\nWhich game do you want to load ? > ")
            load(x)

        if ch.lower() == "qtoub":
            quit()
                    
        if ch.startswith("sell"):
            try:
                if ch[5:] == "all":
                    sell("all")
                    
                sell(int(ch[5:]))

            except ValueError:
                if ch[5:] == "all":
                    pass
                else:
                    print("\nPlease enter a valid amount!")

        if ch.lower() == "crops":
            
                crops()

clear()

print("Pickle", end=" ")
w()
print("Farm")
print("=" * len("Pickle Farm"))
w()
print("\n© canard 2023\n")

s(1)

input("Press enter to continue./")

def game():
    print("\n\n")
    print("\nThe goal of this game is to farm a maximum of pickles thanks to pickle seeds and then resell them.")
    input("\nPress enter to continue./")
    inGame = True
    while inGame is True:
        newDay()
    
game()