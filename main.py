import time, random, sys
from termcolor import colored
from os import system, name 


coins = 10
cchestcost = 10
ucchestcost = 15
rchestcost = 25
echestcost = 50
lchestcost = 100
inventory = [colored("Mobius","magenta"),colored("Mobius","magenta")]
bksellp = 30
msellp = 65
lbsellp = 110
cosellp = 75
vsellp = 35
ssellp = 15

def shop():
	global coinsgained
	equippableitems = ["Lightsbane","lightsbane","lights bane","Lights bane","Light's bane","light's bane","LIGHTSBANE","Venomous","venomous","stick","Stick","corruption orb","Corruption Orb","CORRUPTION ORB","mobius","MOBIUS","Mobius","banditsknife","BANDITSKNIFE","Banditskinfe","bandit's knife","BANDIT'S KNIFE","Bandit's knife","Bandit's Knife","Bandits knife","bandits knife","BANDITS KNIFE"]
	print("\nWelcome to the shop!")
	print(" _   |~  _\n[_]--'--[_]\n|'|""`""|'| | |\n| | /^\\ | |\n|_|_|I|_|_|")
	time.sleep(1)
	print("You can sell:\n")
	for i in inventory:
		print(i)
	time.sleep(1)
	sell = input("Would you like to sell anything [y/n]\n")
	if sell == "y":
		sellitem = input("What would you like to sell?\n")
		if sellitem in equippableitems:
			sellitem.lower()
			if sellitem == "lightsbane":
				if colored("Light's Bane","yellow") in inventory:
					print("You will recieve",colored(lbsellp,"yellow"),"coins for your",colored("Light's Bane","yellow"))
					selllb = input("Would you like to sell it? [y/n]")
					if selllb == "y":
						print("Sold",colored("Light's Bane","yellow"))
						inventory.remove(colored("Light's Bane","yellow"))
						coinsgained = lbsellp
				else:
					print("Sorry that's not in your inventory :(")
					time.sleep(1)
			elif sellitem == "lights bane":
				if colored("Light's Bane","yellow") in inventory:
					print("You will recieve",colored(lbsellp,"yellow"),"coins for your",colored("Light's Bane","yellow"))
					selllb = input("Would you like to sell it? [y/n]")
					if selllb == "y":
						print("Sold",colored("Light's Bane","yellow"))
						inventory.remove(colored("Light's Bane","yellow"))
						coinsgained = lbsellp
				else:
					print("Sorry that's not in your inventory :(")
					time.sleep(1)
			elif sellitem == "light's bane":
				if colored("Light's Bane","yellow") in inventory:
					print("You will recieve",colored(lbsellp,"yellow"),"coins for your",colored("Light's Bane","yellow"))
					selllb = input("Would you like to sell it? [y/n]")
					if selllb == "y":
						print("Sold",colored("Light's Bane","yellow"))
						inventory.remove(colored("Light's Bane","yellow"))
						coinsgained = lbsellp
				else:
					print("Sorry that's not in your inventory :(")
					time.sleep(1)
			elif sellitem == "banditsknife":
				if colored("Bandit's Knife","blue") in inventory:
					print("You will recieve",colored(bksellp,"yellow"),"coins for your",colored("Bandit's Knife","blue"))
					sellbk = input("Would you like to sell it? [y/n]")
					if sellbk == "y":
						print("Sold",colored("Bandit's Knife","blue"))
						inventory.remove(colored("Bandit's Knife","blue"))
						coinsgained = bksellp
			elif sellitem == "bandits knife":
				if colored("Bandit's Knife","blue") in inventory:
					print("You will recieve",colored(bksellp,"yellow"),"coins for your",colored("Bandit's Knife","blue"))
					sellbk = input("Would you like to sell it? [y/n]")
					if sellbk == "y":
						print("Sold",colored("Bandit's Knife","blue"))
						inventory.remove(colored("Bandit's Knife","blue"))
						coinsgained = bksellp
			elif sellitem == "bandit's knife":
				if colored("Bandit's Knife","blue") in inventory:
					print("You will recieve",colored(bksellp,"yellow"),"coins for your",colored("Bandit's Knife","blue"))
					sellbk = input("Would you like to sell it? [y/n]")
					if sellbk == "y":
						print("Sold",colored("Bandit's Knife","blue"))
						inventory.remove(colored("Bandit's Knife","blue"))
						coinsgained = bksellp
			elif sellitem == "corruptionorb":
				if colored("Corruption Orb","magenta") in inventory:
					print("You will recieve",colored(cosellp,"yellow"),"coins for your",colored("Corruption Orb","magenta"))
					sellco = input("Would you like to sell it? [y/n]")
					if sellco == "y":
						print("Sold",colored("Corruption Orb","magenta"))
						inventory.remove(colored("Corruption Orb","magenta"))
						coinsgained = cosellp
			elif sellitem == "corruption orb":
				if colored("Corruption Orb","magenta") in inventory:
					print("You will recieve",colored(cosellp,"yellow"),"coins for your",colored("Corruption Orb","magenta"))
					sellco = input("Would you like to sell it? [y/n]")
					if sellco == "y":
						print("Sold",colored("Corruption Orb","magenta"))
						inventory.remove(colored("Corruption Orb","magenta"))
						coinsgained = cosellp
			elif sellitem == "mobius":
				if colored("Mobius","magenta") in inventory:
					print("You will recieve",colored(msellp,"yellow"),"coins for your",colored("Mobius","magenta"))
					sellm = input("Would you like to sell it? [y/n]")
					if sellm == "y":
						print("Sold",colored("Mobius","magenta"))
						inventory.remove(colored("Mobius","magenta"))
						coinsgained = msellp
	else:		
		print("Sorry, that's not in your inventory :(")

def c_dungeon_chest():
	loot = random.randint(1,200)
	drop = random.randint(1,2)
	if loot <= 5:
		loot = colored("legendary","yellow")
		if drop <= 2:
			drops = colored("100 coins","yellow")
			global coinsgained
			coinsgained = 100
		elif drop == 3:
			drops = colored("Light's Bane","yellow")
			coinsgained = 25
			inventory.append(drops)
	elif loot >= 6 and loot <= 25:
		loot = colored("epic","magenta")
		if drop == 1:
			drops = colored("50 coins","magenta")
			coinsgained = 50
		elif drop == 2:
			drops = colored("Corruption Stone","magenta")
			coinsgained = 10
			inventory.append(drops)
		elif drop == 3:
			drops = colored("Mobius","magenta")
			coinsgained = 10
			inventory.append(drops)
	elif loot >= 26 and loot <= 50:
		loot = colored("rare","blue")
		if drop == 1:
			drops = colored("25 coins","blue")
			coinsgained = 25
		elif drop == 2:
			drops = colored("Venomous","blue")
			coinsgained = 10
			inventory.append(drops)
		elif drop == 3:
			drops = colored("Bandit's Knife","blue")
			coinsgained = 10
			inventory.append(drops)
	elif loot >= 51 and loot <= 100:
		loot = colored("uncommon","green")
		if drop == 1:
			drops = colored("15 coins","green")
			coinsgained = 15
		elif drop >= 2:
			drops = colored("20 coins","green")
			coinsgained = 20
	elif loot >= 101 and loot <= 200:
		loot = colored("common","white")
		if drop == 1:
			drops = colored("10 coins","white")
			coinsgained = 10
		elif drop >= 2:
			drops = colored("stick","white")
			coinsgained = 5
			inventory.append(drops)
	print(drops,"-",loot)
	time.sleep(1)

def uc_dungeon_chest():
	loot = random.randint(1,200)
	drop = random.randint(1,3)
	if loot <= 5:
		loot = colored("legendary","yellow")
		if drop <= 2:
			drops = colored("100 coins","yellow")
			global coinsgained
			coinsgained = 100
		elif drop == 3:
			drops = colored("Light's Bane","yellow")
			coinsgained = 25
			inventory.append(drops)
	elif loot >= 6 and loot <= 25:
		loot = colored("epic","magenta")
		if drop == 1:
			drops = colored("50 coins","magenta")
			coinsgained = 50
		elif drop == 2:
			drops = colored("Corruption Orb","magenta")
			coinsgained = 10
			inventory.append(drops)
		elif drop == 3:
			drops = colored("Mobius","magenta")
			coinsgained = 10
			inventory.append(drops)
	elif loot >= 26 and loot <= 50:
		loot = colored("rare","blue")
		if drop == 1:
			drops = colored("25 coins","blue")
			coinsgained = 25
		elif drop == 2:
			drops = colored("Venomous","blue")
			coinsgained = 10
			inventory.append(drops)
		elif drop == 3:
			drops = colored("Bandit's Knife","blue")
			coinsgained = 10
			inventory.append(drops)
	elif loot >= 51 and loot <= 150:
		loot = colored("uncommon","green")
		if drop == 1:
			drops = colored("15 coins","green")
			coinsgained = 15
		elif drop >= 2:
			drops = colored("20 coins","green")
			coinsgained = 20
	elif loot >= 151 and loot <= 200:
		loot = colored("common","white")
		if drop == 1:
			drops = colored("10 coins","white")
			coinsgained = 10
		elif drop >= 2:
			drops = colored("stick","white")
			coinsgained = 5
			inventory.append(drops)
	print(drops,"-",loot)
	time.sleep(1)

def r_dungeon_chest():
	loot = random.randint(1,200)
	drop = random.randint(1,3)
	if loot <= 15:
		loot = colored("legendary","yellow")
		if drop <= 2:
			drops = colored("100 coins","yellow")
			global coinsgained
			coinsgained = 100
		elif drop == 3:
			drops = colored("Light's Bane","yellow")
			coinsgained = 25
			inventory.append(drops)
	elif loot >= 16 and loot <= 25:
		loot = colored("epic","magenta")
		if drop == 1:
			drops = colored("50 coins","magenta")
			coinsgained = 50
		elif drop == 2:
			drops = colored("Corruption Orb","magenta")
			coinsgained = 10
			inventory.append(drops)
		elif drop == 3:
			drops = colored("Mobius","magenta")
			coinsgained = 10
			inventory.append(drops)
	elif loot >= 51 and loot <= 150:
		loot = colored("rare","blue")
		if drop == 1:
			drops = colored("25 coins","blue")
			coinsgained = 25
		elif drop == 2:
			drops = colored("Venomous","blue")
			coinsgained = 10
			inventory.append(drops)
		elif drop == 3:
			drops = colored("Bandit's Knife","blue")
			coinsgained = 10
			inventory.append(drops)
	elif loot >= 151 and loot <= 200:
		loot = colored("uncommon","green")
		if drop == 1:
			drops = colored("15 coins","green")
			coinsgained = 15
		elif drop >= 2:
			drops = colored("20 coins","green")
			coinsgained = 20
	print(drops,"-",loot)
	time.sleep(1)

def e_dungeon_chest():
	loot = random.randint(1,200)
	drop = random.randint(1,3)
	if loot <= 25:
		loot = colored("legendary","yellow")
		if drop <= 2:
			drops = colored("100 coins","yellow")
			global coinsgained
			coinsgained = 100
		elif drop == 3:
			drops = colored("Light's Bane","yellow")
			coinsgained = 25
			inventory.append(drops)
	elif loot >= 26 and loot <= 75:
		loot = colored("epic","magenta")
		if drop == 1:
			drops = colored("50 coins","magenta")
			coinsgained = 50
		elif drop == 2:
			drops = colored("Corruption Orb","magenta")
			coinsgained = 10
			inventory.append(drops)
		elif drop == 3:
			drops = colored("Mobius","magenta")
			coinsgained = 10
			inventory.append(drops)
	elif loot >= 76 and loot <= 175:
		loot = colored("rare","blue")
		if drop == 1:
			drops = colored("25 coins","blue")
			coinsgained = 25
		elif drop == 2:
			drops = colored("Venomous","blue")
			coinsgained = 10
			inventory.append(drops)
		elif drop == 3:
			drops = colored("Bandit's Knife","blue")
			coinsgained = 10
			inventory.append(drops)
	elif loot >= 176 and loot <= 200:
		loot = colored("uncommon","green")
		if drop == 1:
			drops = colored("15 coins","green")
			coinsgained = 15
		elif drop >= 2:
			drops = colored("20 coins","green")
			coinsgained = 20
	print(drops,"-",loot)
	time.sleep(1)

def l_dungeon_chest():
	loot = random.randint(1,200)
	drop = random.randint(1,3)
	if loot <= 50:
		loot = colored("legendary","yellow")
		if drop <= 2:
			drops = colored("100 coins","yellow")
			global coinsgained
			coinsgained = 100
		elif drop == 3:
			drops = colored("Light's Bane","yellow")
			coinsgained = 25
			inventory.append(drops)
	elif loot >= 51 and loot <= 175:
		loot = colored("epic","magenta")
		if drop == 1:
			drops = colored("50 coins","magenta")
			coinsgained = 50
		elif drop == 2:
			drops = colored("Corruption Orb","magenta")
			coinsgained = 10
			inventory.append(drops)
		elif drop == 3:
			drops = colored("Mobius","magenta")
			coinsgained = 10
			inventory.append(drops)
	elif loot >= 176 and loot <= 200:
		loot = colored("rare","blue")
		if drop == 1:
			drops = colored("25 coins","blue")
			coinsgained = 25
		elif drop == 2:
			drops = colored("Venomous","blue")
			coinsgained = 10
			inventory.append(drops)
		elif drop == 3:
			drops = colored("Bandit's Knife","blue")
			coinsgained = 10
			inventory.append(drops)
	print(drops,"-",loot)
	time.sleep(1)

def dungeon():
	equippableitems = ["Lightsbane","lightsbane","lights bane","Lights bane","Light's bane","light's bane","LIGHTSBANE","Venomous","venomous","stick","Stick","corruption orb","Corruption Orb","CORRUPTION ORB","mobius","MOBIUS","Mobius","banditsknife","BANDITSKNIFE","Banditskinfe","bandit's knife","BANDIT'S KNIFE","Bandit's knife","Bandit's Knife","Bandits knife","bandits knife","BANDITS KNIFE"]
	equip = input("Would you like to equip any items before going into the dungeon? [y/n]\n")
	global coinsgained
	if equip == "y":
		equipitem = input("What would you like to equip?")
		equippeditem = equipitem.lower()
		if equippeditem in equippableitems:
			if equippeditem == "lightsbane":
				if colored("Light's Bane","yellow") in inventory:
					print("Equipped",colored("Light's Bane","yellow"))
					damage = 25
					health = 10
			elif equippeditem == "lights bane":
				if colored("Light's Bane","yellow") in inventory:
					print("Equipped",colored("Light's Bane","yellow"))
					damage = 25
					health = 10
			elif equippeditem == "light's bane":
				if colored("Light's Bane","yellow") in inventory:
					print("Equipped",colored("Light's Bane","yellow"))
					damage = 25
					health = 10
			elif equippeditem == "venomous":
				if colored("Venomous","blue") in inventory:
					print("Equipped",colored("Venomous","blue"))
					damage = 10
					health = 10
			elif equippeditem == "stick":
				if colored("stick","white") in inventory:
					print("Equipped",colored("stick","white"))
					damage = 4
					health = 10
			elif equippeditem == "corruption orb":
				if colored("Corruption Orb","magenta") in inventory:
					print("Equipped",colored("Corruption Orb","magenta"))
					health = 25
					damage = 10
			elif equippeditem == "mobius":
				if colored("Mobius","magenta") in inventory:
					print("Equipped",colored("Mobius","magenta"))
					health = 10
					damage = 20
			elif equippeditem == "banditsknife":
				if colored("Bandit's Knife","blue") in inventory:
					print("Equipped",colored("Bandit's Knife","blue"))
					health = 10
					damage = 15
			elif equippeditem == "bandit's knife":
				if colored("Bandit's Knife","blue") in inventory:
					print("Equipped",colored("Bandit's Knife","blue"))
					health = 10
					damage = 15
			elif equippeditem == "bandits knife":
				if colored("Bandit's Knife","blue") in inventory:
					print("Equipped",colored("Bandit's Knife","blue"))
					health = 10
					damage = 15
			else:
				print("Did not equip anything")
				damage = 1
				health = 10
		else:
			print("You did not equip anything")
			damage = 1
			health = 10
	elif equip == "n":
		print("You did not equip anything")
		damage = 1
		health = 10
	print("You enter the dungeon...")
	time.sleep(1)
	r1chances = random.randint(1,10)
	if r1chances <= 3:
		troom = True
		froom = False
	else:
		froom = True
		troom = False
	if troom == True:
		print("You enter a room filled",colored("with treasures","yellow"),"you take some\n",colored("+50 Coins","yellow"))
		coinsgained = 50
	if froom == True:
		print("You stumble upon a room",colored("filled with monsters","red"))
		time.sleep(1)
		fight = input("Fight them?\n")
		if fight == "y":
			mhp = random.randint(5,15)
			mdmg = random.randint(1,5)
			print("Your health:",health,"\nMonster's health",mhp)
			time.sleep(1)
			while mhp > 0:
				mhp -= damage
				print("You did",colored(damage,"red"),"damage")
				time.sleep(1)
			if mhp <= 0:
				print("You killed the monster")
				time.sleep(1)
				print(colored("+10 Coins","yellow"))
				coinsgained = 10
	time.sleep(1)
	print("You find a door to a second room...")
	time.sleep(1)
	r2chances = random.randint(1,10)
	if r2chances <= 3:
		troom = True
		froom = False
	else:
		froom = True
		troom = False
	if troom == True:
		print("You enter a room filled",colored("with treasures","yellow"),"you take some\n",colored("+50 Coins","yellow"))
		coinsgained += 50
	if froom == True:
		print("You stumble upon a room",colored("filled with monsters","red"))
		time.sleep(1)
		fight = input("Fight them?\n")
		if fight == "y":
			mhp = random.randint(5,15)
			mdmg = random.randint(1,5)
			print("Your health:",health,"\nMonster's health",mhp)
			time.sleep(1)
			while mhp > 0:
				mhp -= damage
				print("You did",colored(damage,"red"),"damage")
				time.sleep(1)
			if mhp <= 0:
				print("You killed the monster")
				time.sleep(1)
				print(colored("+10 Coins","yellow"))
				coinsgained += 10
	bosshp = random.randint(50,75)
	bossdmg = 5
	while bosshp > 0:
		bosshp -= damage
		print("Bosses Health:",colored(bosshp,"red"))
		time.sleep(1)
										
def clear(): 
  
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
  
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 								
def load():
	print("Made by:")
	print(" __ _             _ _       \n/ _\\ |_ _   _  __| (_) ___  \n\\ \\| __| | | |/ _` | |/ _ \\ \n_\\ \\ |_| |_| | (_| | | (_) |\n\\__/\\__|\\__,_|\\__,_|_|\\___/ ")
	time.sleep(2)
	clear()
	print("Loading |")
	time.sleep(.5)
	clear()
	print("Loading /")
	time.sleep(.5)
	clear()
	print("Loading -")
	time.sleep(.5)
	clear()
	print("Loading \\")
	time.sleep(.5)
	clear()
	print("Loading |")
	time.sleep(.5)
	clear()
	print("Loading /")
	time.sleep(.5)
	clear()
	print("Loading -")
	time.sleep(.5)
	clear()
	print("Loading \\")
	time.sleep(.5)
	clear()
	print("Loading |")
	time.sleep(.5)
	clear()
	print("Loading /")
	time.sleep(.5)
	clear()
	print("Loading -")
	time.sleep(.5)
	clear()
	print("Loading \\")
	time.sleep(.5)
	clear()
	print("Loading |")
	time.sleep(.5)
	clear()
	print("Loading /")
	time.sleep(.5)
	clear()
	print("Loading -")
	time.sleep(.5)
	clear()
	print("Loading \\")
	time.sleep(.5)
	clear()
	print("Loading |")
	time.sleep(.5)
	clear()
load()
for i in range(100):
	print("\nHome\n")
	print("Your balance:",coins)
	print("Your inventory:")
	for i in inventory:
		print(i)
	print("\nWhat would you like to do?")
	choice = input("c for chest, d for dungeon, s for shop, or h for help\n")
	if choice == "c":
		print("What chest would you like to open?")
		chest = input("common, uncommon, rare, epic, or legendary\n")
		if chest == "common":
			print("This will cost",cchestcost,"coins. Would you like to buy it? [y/n]")
			sure = input("")
			if sure == "y" and coins >= cchestcost:
				coins -= cchestcost
				c_dungeon_chest()
				coins += coinsgained
			elif sure == "y" and coins < cchestcost:
				print("Sorry, you don't have enough coins, go do a dungeon")
			else:
				print("Cancelled chest purchase")
		if chest == "uncommon":
			print("This will cost",ucchestcost,"would you like to buy it? [y/n]")
			sure = input("")
			if sure == "y" and coins >= ucchestcost:
				coins -= ucchestcost
				uc_dungeon_chest()
				coins += coinsgained
			elif sure == "y" and coins < ucchestcost:
				print("Sorry, you don't have enough coins")
			else:
				print("Cancelled chest purchase")
		if chest == "rare":
			print("This wil cost",rchestcost,"would you like to buy it? [y/n]")
			sure = input("")
			if sure == "y" and coins >= rchestcost:
				coins -= rchestcost
				r_dungeon_chest()
				coins += coinsgained
			elif sure == "y" and coins < rchestcost:
				print("Sorry, you don't have enough coins")
			else:
				print("Cancelled chest purchase")
		if chest == "epic":
			print("This wil cost",echestcost,"would you like to buy it? [y/n]")
			sure = input("")
			if sure == "y" and coins >= echestcost:
				coins -= echestcost
				e_dungeon_chest()
				coins += coinsgained
			elif sure == "y" and coins < echestcost:
				print("Sorry, you don't have enough coins")
			else:
				print("Cancelled chest purchase")
		if chest == "legendary":
			print("This wil cost",lchestcost,"would you like to buy it? [y/n]")
			sure = input("")
			if sure == "y" and coins >= lchestcost:
				coins -= lchestcost
				l_dungeon_chest()
				coins += coinsgained
			elif sure == "y" and coins < lchestcost:
				print("Sorry, you don't have enough coins")
			else:
				print("Cancelled chest purchase")
	elif choice == "d":
		dungeon()
		coins += coinsgained
	elif choice == "reload":
		sys.exit()
	elif choice == "h":
		print("c for chest, d for dungeon, or h for help")
	elif choice == "s":
		shop()
		coins += coinsgained
	time.sleep(1)
	clear()