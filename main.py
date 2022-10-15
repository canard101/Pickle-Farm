from replit import db
from time import sleep as s
import os
from random import randint

def w():
    s(0.1)

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

sellPrice = {
    "basic": randint(5,15),
    "festival": randint(10,20),
}

class planted:
    phase1 = 0
    phase2 = 0
    phase3 = 0
    phase4 = 0
    phase5 = 0
    phase6 = 0
    phase7 = 0
    
    growing = phase1+phase2+phase3+phase4+phase5+phase6

class events:
    def storm():
        print("Oh no !\n", G, "50%", END, "of your pickles got destroyed because of a storm")
        planted.phase1 

    def festival():
        player.festNbr 
        print("\nYay ! ")
        print("Today")

def save(name):
    
  from replit import db
  
  db["PCK_"+name] = player.pickles
  db["MNY_"+name] = player.money
  db["SDS_"+name] = player.seeds

  print("\nYou've saved the game to the name ", G, name, END, " !")

def load(name):

    from replit import db

    player.money = db["MNY_"+name]
    player.pickles = db["PCK_"+name]
    player.seeds = db["SDS_"+name]

    print("\nYou've loaded the game with the name ", G, name, END, " !")
    
def crops():
    print("\n• Tommorow's crop : ", G, planted.phase6, END)
    print("• Recolt in 2 days : ", G, planted.phase5, END)
    print("• Recolt in 3 days : ", G, planted.phase4, END)
    print("• Recolt in 4 days : ", G, planted.phase3, END)
    print("• Recolt in 5 days : ", G, planted.phase2, END)
    print("• Recolt in 6 days : ", G, planted.phase1, END)
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
            print("You now have ", G, planted.phase1+planted.phase2+planted.phase3+planted.phase4+planted.phase5+planted.phase6, END, " pickles growing.")
            player.seeds = 0

        if player.seeds < int(amount):
            print("You don't have that much of seeds ! You can only plant ", G, player.seeds, END, " seeds!")
            pass
        
        else:
            player.seeds -= int(amount)
            planted.phase1 += int(amount)
            print("\nYou planted ", G, amount, END, " pickles !")  
            print("You now have ", planted.phase1+planted.phase2+planted.phase3+planted.phase4+planted.phase5+planted.phase6, " pickles growing.")

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
    salePrice = randint(5,15)
    if player.pickles == 0:
        print("\nYou don't have any pickles to sell !\n")
        pass

    if player.pickles != 0:    
        if amount == "all":
            print("\nThe sale price of pickles is at ", G, salePrice, END, " $ today!")
            ch = input("\nAre you sure you want to sell your pickles? > ")
            
            if ch == "yes":
                player.money += (player.pickles*salePrice)
                print("\nYou sold ", G, player.pickles, END, " pickle(s) !")
                player.pickles = 0
                print("You now have ", G, player.money, END, " $ and ", G, player.pickles, END, " pickle(s).")
                
            elif ch == "no":
                print("\nOk, maybe another day!")
                pass
            else:
                print("\nAnswer by yes or no!")
            
        if player.pickles < int(amount):
            print("You don't have that much pickles to harvest ! You can only harvest ", G, planted.phase7, END, " pickle(s)!")
            pass

        
    
def newDay():
    """
    Create a new day
    """
    event = random.randint(1, 10)
    
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
    a = player.day
    print("\nDay : ", G, a, END)       
    print("="*len("Day : "+str(a)))
    s(0.5)
    print(G, player.money, END, "$")
    s(0.5)
    print("Pickles : ", G, f"{player.pickles} ", END)  
    s(0.5)
    print("Seeds : ", G, f"{player.seeds}", END)     
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

print("Pickle")
w()
print("Farm")
print("====")
w()
print("\n© jujubier\n")

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