import math
import random
import os

shopLevel = 1

userName = str(input("What is your name?: "))

while True:

    genderChoice = eval(input("Do you wish to be a 1. Boy or 2. Girl?: "))

    if genderChoice == 1:
        pronounChoice = "He"
        pronounChoicePossession = "His"
        pronounChoiceTitle = "Him"
        break
    elif genderChoice == 2:
        pronounChoice = "She"
        pronounChoicePossession = "Hers"
        pronounChoiceTitle = "Her"
        break
    else:
        print("Please enter either 1 or 2.")

while True:
    wealthLevel = float(input("Select a Wealth Level 1-3: "))

    if wealthLevel == 1:

        currentMoney = random.randint(1, 100)
        robberyChancePerSegment = 10
        amountSpent = 0
        break

    elif wealthLevel == 2:

        currentMoney = random.randint(101, 500)
        robberyChancePerSegment = 40
        amountSpent = 64
        break

    elif wealthLevel == 3:

        currentMoney = random.randint(501, 1000)
        robberyChancePerSegment = 70
        amountSpent = 800
        break

    else:
        print("Please Enter a Number 1-3.")

""""""
'''

THE SHOP CODE

'''
""""""


def purchase(name, price):
    global currentMoney
    global amountSpent
    if currentMoney >= price:
        currentMoney -= price
        print("You purchased the " + name + ".")
        amountSpent += price
    else:
        print("You don't have enough to purchase the " + name + ".")


def mainshop():
    global shopLevel
    shopLevel = 1

    print("")
    print("You are at the shop. Your current shop level is level "
          + str(shopLevel) + ", and you have " + str(currentMoney)
          + " gold. What will you buy?")

    print("1. Weaponry")
    print("2. Armor")
    print("3. Useful Items")
    print("")
    print("4. Leave the Shop")

    shopselection = int(input())

    if shopselection == 1:
        shopLevel = 1
        weaponshop()
    elif shopselection == 2:
        shopLevel = 1
        armorshop()
    elif shopselection == 3:
        if hashadearplugs:
            specialshop()
        else:
            print("You cannot access this place yet.")
            mainshop()
    elif shopselection == 4:
        fishingmain()

    else:
        print("Please pick a number 1-4.")
        mainshop()


def weaponshop():
    if shopLevel == 1:
        print("")
        print("What weaponry will you buy? (You have " + str(currentMoney) + " gold.)")
        print("1. Rusted Sword [10G]")
        print("2. Broken Sickle [7G]")
        print("3. Damaged Longsword [15G]")
        print("4. Cracked Buckler Shield [10G]")
        print("5. Crooked Sickle [7G]")
        print("6. Bent Scutum Shield [15G]")
        print("")
        print("7. Go Back")

        itemselection = int(input())

        if itemselection == 1:
            purchase("Rusted Sword", 10)
            hasRustedSword = True
            weaponshop()

        elif itemselection == 2:
            purchase("Broken Sickle", 7)
            hasBrokenSickle = True
            weaponshop()

        elif itemselection == 3:
            purchase("Damaged Longsword", 15)
            hasDamagedLongsword = True
            weaponshop()

        elif itemselection == 4:
            purchase("Cracked Buckler Shield", 10)
            hasCrackedBucklerShield = True
            weaponshop()

        elif itemselection == 5:
            purchase("Crooked Sickle", 7)
            hasCrookedSickle = True
            weaponshop()

        elif itemselection == 6:
            purchase("Bent Scutum Shield", 15)
            hasBentScutumShield = True
            weaponshop()

        elif itemselection == 7:
            mainshop()

        else:
            print("Please select a number 1-7.")
            weaponshop()
    else:
        print("code error")


def armorshop():
    if shopLevel == 1:
        print("")
        print("What armor will you buy? (You have " + str(currentMoney) + " gold.)")
        print("1. Broken Helm [10G]")
        print("2. Cheap Chestplate [15G]")
        print("3. Leg Bandages [10G]")
        print("4. Beggars Boots [7G]")

        print("")
        print("5. Go Back")

        itemselection = int(input())

        if itemselection == 1:
            purchase("Broken Helm", 10)
            hasBrokenHelm = True
            armorshop()

        elif itemselection == 2:
            purchase("Cheap Chestplate", 15)
            hasCheapChestplate = True
            armorshop()

        elif itemselection == 3:
            purchase("Leg Bandages", 10)
            hasLegBandages = True
            armorshop()

        elif itemselection == 4:
            purchase("Beggars Boots", 7)
            hasBeggarsBoots = True
            armorshop()

        elif itemselection == 5:
            mainshop()

        else:
            print("Please select a number 1-7.")
            armorshop()
    else:
        print("code error")


hasearplugs = False
hashadearplugs = False


def specialshop():
    global hasearplugs
    if shopLevel == 1:
        print("")
        print("What special items will you buy? (You have " + str(currentMoney) + " gold.)")
        print("1. Earplugs [150G]")
        print("2. Go Back")

    itemselection = int(input())

    if itemselection == 1:
        purchase("Earplugs", 150)
        hasearplugs = True
        specialshop()
    elif itemselection == 2:
        mainshop()
    else:
        print("error")


def fishingmain():
    global currentMoney

    print("You are at the fishing pier.")
    print("An old fisher stands behind you, and claims he is willing to buy any fish caught.")
    print("")
    print("1. Go Fish")
    print("2. Inquire about The Rumors")
    print("3. Leave")

    fishingselection = int(input())

    if fishingselection == 1:
        fishthing = random.randint(1, 100)

        if fishthing <= 1:
            print("You drown and die.")
            exit()
        elif fishthing <= 5:
            mermaidorsiren = random.randint(1, 2)

            if mermaidorsiren == 1:
                goldblessing = random.randint(500, 1000)
                print("You fished a mermaid. It gives you " + str(goldblessing) + " gold!")
                currentMoney += goldblessing
                print(f"You now have {currentMoney} gold.")
                print("")
                fishingmain()
            elif mermaidorsiren == 2:
                global hasearplugs
                if hasearplugs:
                    print("You fished a siren. She attempts to call, but none is heard.")
                    print("You survive, at the cost of your earplugs.")
                    print("")
                    hasearplugs = False
                    fishingmain()

                elif not hasearplugs:
                    print("You fished a siren. She lures you into the sea, and you die.")
                    exit()
                else:
                    print("program error")

            else:
                print("program error")
        elif fishthing <= 10:
            print("You fished a golden fish. The old man gives you 200 gold.")
            currentMoney += 200
            print(f"You now have {currentMoney} gold.")
            print("")
            fishingmain()
        elif fishthing <= 25:
            print("You fished a Blue Lobster. The old man gives you 100 gold.")
            currentMoney += 100
            print(f"You now have {currentMoney} gold.")
            print("")
            fishingmain()
        elif fishthing <= 50:
            print("You caught a Green Flopper. The old man gives you 25 gold.")
            currentMoney += 25
            print(f"You now have {currentMoney} gold.")
            print("")
            fishingmain()
        elif fishthing <= 100:
            print("You caught a Gray Tuna. The old man gives you 10 gold.")
            currentMoney += 10
            print(f"You now have {currentMoney} gold.")
            print("")
            fishingmain()
        else:
            print("code error")
            exit()

    elif fishingselection == 2:
        global hashadearplugs
        print("")
        print("<i> You remember hearing a rumour about something called the Screeching Beauty.")
        print("<i> You decide to ask the old man.")
        print("")
        print(userName + ": Hey, old man. What can you tell me about the Screeching Beauty?")
        print("The Old Man: Ah... you must mean the Siren, that old hag.")
        print("")
        print("<i> The Old Man shifts uncomfortably, as if remembering unpleasant feelings.")
        print("The Old Man: She takes the appearance of mermaids. Rarely, she will let herself get caught.")
        print("I ran into her, once, and I would have died, had it not been for these.")
        print("")
        print("<i> The Old Man reveals a pair of two pristine ear plugs.")
        print("The Old Man: I've no use for these, at least not anymore. But you...")
        print("<i> The Old Man looks at you and smiles.")
        print("The Old Man: I see a fire in you, one I once held within myself. Take the earplugs.")
        print("They will keep you safe.")
        print("")
        print("You obtained the Earplugs.")

        hashadearplugs = True
        hasearplugs = True
        fishingmainpostrumors()

    elif fishingselection == 3:
        mainshop()
    else:
        print("Enter 1 or 2.")
        fishingmain()


def fishingmainpostrumors():
    global currentMoney

    print("You are at the fishing pier.")
    print("An old fisher stands behind you, and claims he is willing to buy any fish caught.")
    print("")
    print("1. Go Fish")
    print("2. Inquire about The Rumors")
    print("3. Leave")

    fishingselection = int(input())

    if fishingselection == 1:
        fishthing = random.randint(1, 100)

        if fishthing <= 1:
            print("You drown and die.")
            exit()
        elif fishthing <= 5:
            mermaidorsiren = random.randint(1, 2)

            if mermaidorsiren == 1:
                goldblessing = random.randint(500, 1000)
                print("You fished a mermaid. It gives you " + str(goldblessing) + " gold!")
                currentMoney += goldblessing
                print(f"You now have {currentMoney} gold.")
                print("")
                fishingmainpostrumors()

            elif mermaidorsiren == 2:
                global hasearplugs
                if hasearplugs:
                    print("You fished a siren. She attempts to call, but none is heard.")
                    print("You survive, at the cost of your earplugs.")
                    print("")
                    fishingmainpostrumors()

                elif not hasearplugs:
                    print("You fished a siren. She lures you into the sea, and you die.")
                    exit()
                else:
                    print("program error")

            else:
                print("program error")
        elif fishthing <= 10:
            print("You fished a golden fish. The old man gives you 200 gold.")
            currentMoney += 200
            print(f"You now have {currentMoney} gold.")
            print("")
            fishingmainpostrumors()
        elif fishthing <= 25:
            print("You fished a Blue Lobster. The old man gives you 100 gold.")
            currentMoney += 100
            print(f"You now have {currentMoney} gold.")
            print("")
            fishingmainpostrumors()
        elif fishthing <= 50:
            print("You caught a Green Flopper. The old man gives you 25 gold.")
            currentMoney += 25
            print(f"You now have {currentMoney} gold.")
            print("")
            fishingmainpostrumors()
        elif fishthing <= 100:
            print("You caught a Gray Tuna. The old man gives you 10 gold.")
            currentMoney += 10
            print(f"You now have {currentMoney} gold.")
            print("")
            fishingmainpostrumors()
        else:
            print("code error")
            exit()

    elif fishingselection == 2:
        print("The Old Man chuckles at you, and says he already has told you everything.")
        print("")
        fishingmainpostrumors()

    elif fishingselection == 3:
        mainshop()
    else:
        print("Enter 1 or 2.")
        fishingmainpostrumors()


mainshop()



