# Ryan Wang
# 12 June 2024
# PyHarvest

import os
from defcrops import * #Class of Seeds
from defshop import buy_shop, buy_process, plant_crops #Whole process of buying/planting crops
from defother import * #Crop growth, tutorial, leaderboard
from defmarket import manipulate, market #Selling crops
from defevents import random_event #Random events

farmplot = [["empty" for i in range(3)] for j in range(3)]
farmgrowth = [[-1 for i in range(3)] for j in range(3)]

harvested_crops = [0] * 4

corn = Seeds("Corn",5,"Costs $5 and sells for ~$8. Grows in 2 turns",2)
wheat = Seeds("Wheat",2,"Costs $2 and sells for ~$5. Grows in 1 turns",1)
rice = Seeds("Rice",1,"Costs $1 and sells for ~$3. Grows in 1 turns",1)
peppers = Seeds("Pepper",10,"Costs $10 and sells for ~$20. Grows in 2 turns",2)

sell_prices = [8,5,3,20]
coins = 50
turn = 1
crop = "empty"

tutorial()

#The standard screen a player will see on the Home Screen, which will allow them to see the tutorial again, buy/plant crops, sell crops, see their farm plot and end their turn
def turn_start():
  global turn, harvest, coins, harvested_crops, sell_prices, farmplot, farmgrowth
  print("-------PyHarvest----------")
  print(f"Current Turn: |{turn}/10| ", end= "")

  for i in range(turn):
    print("[*]",end="")
  for j in range(10-turn):
    print("[]",end="")
  print()

  print(f"Current Number of Coins: {coins}")

  print()
  print("Your Farm")
  for r in range(3):
    for c in range(3):
      print(f"|{farmplot[r][c]}|", end="")
    print()

  #END of the game
  if turn == 10:
    leaderboard(coins) #from defother.py


  else:
    print("------------------------")
    print("What do you want to do...")
    print("(1) Read Tutorial (Again)")
    print("(2) Buy/Plant some crops")
    print("(3) Sell some crops")
    print("(4) Look at farmplot")
    print("(5) End your turn (Do this if you have nothing else to do!)")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    try:
      option = int(input())
      print()

    except:
      print("That's not a number! Please enter in an integer i.e. 1")
      os.system('clear')
      turn_start()

    if option == 1: #Look at tutorial (again)
      os.system('clear')
      tutorial()
      turn_start()

    elif option == 2: #Buy crops
      os.system('clear')
      crop = buy_shop(coins,farmplot)
      if crop == "corn" or crop == "rice" or crop == "peppers" or crop == "wheat":
        values = buy_process(coins,crop)
        try:
          amount = values[0]
          coins = values[1]
          plant_crops(farmplot,crop,amount,farmgrowth)
        except:
          pass
      turn_start()

    elif option == 3: #Sell crops
      os.system('clear')
      print(f"You currently have crops ready to sell!")
      values = market(coins,turn,harvested_crops)
      coins = values[0]
      harvested_crops = values[1]
      turn_start()

    elif option == 4: #Look at farmplot
      os.system('clear')
      print("Your Farm")
      for r in range(3):
        for c in range(3):
          print(f"|{farmplot[r][c]}|", end="")
        print()

      print("Time to grow crops")
      for r in range(3):
        for c in range(3):
          print(f"|{farmgrowth[r][c]}|", end="")
        print()

      turn_start()

    elif option == 5: #End Turn
      os.system('clear')
      print("The next turn begins...")
      turn+=1
      values = random_event(farmgrowth,farmplot,coins)
      farmgrowth = values[0]
      farmplot = values[1]
      coins = values[2]
      harvested_crops = crop_growth(farmplot,farmgrowth,harvested_crops)
      turn_start()

    else:
      print("That's not a valid number! Please enter an integer i.e. 1")


turn_start()