#This entire piece of code focuses on the process of buying/planting crops

import os
from defcrops import *
corn = Seeds("Corn",5,"Costs $5 and sells for ~$8. Grows in 2 turns",2)
wheat = Seeds("Wheat",2,"Costs $2 and sells for ~$5. Grows in 1 turns",1)
rice = Seeds("Rice",1,"Costs $1 and sells for ~$3. Grows in 1 turns",1)
peppers = Seeds("Pepper",10,"Costs $10 and sells for ~$20. Grows in 2 turns",2)
harvested_crops = [0] * 4


#The player can choose which crop to buy with the amount of coins they currently have
def buy_shop(coins,farmplot):
  go = True
  print("~~~~~~~~~~~~~~~~~~~~~~~")
  print(f"You currently have {coins} coins left")
  print("What do you want to buy?")
  print()
  print("(1) Corn", corn)
  print("(2) Wheat", wheat)
  print("(3) Rice", rice)
  print("(4) Peppers", peppers)
  print("(5) Don't buy anything")
  print("Your Farm")
  for r in range(3):
    for c in range(3):
      print(f"|{farmplot[r][c]}|", end="")
    print()

  print()

  while go == True:
    try:
      option = int(input())
    except:
      os.system('clear')
      print("That's not an integer, please put one in")
      return()

    if option == 1: #Corn
      crop = "corn"
      return(crop)
      os.system('clear')

    elif option == 2: #Wheat
      crop = "wheat"
      return(crop)
      os.system('clear')

    elif option == 3:
      crop = "rice"
      return(crop)
      os.system('clear')

    elif option == 4:
      crop = "peppers"
      return(crop)
      os.system('clear')

    elif option == 5:
      os.system('clear')
      return("empty")


    else:
      os.system('clear')
      print("That's not a valid option! Please put in a different input i.e. 1 for corn")
      buy_shop(coins,farmplot)




#This process regulates how buying crops works, by ensuring they buy the right amount of crop and have enough to afford it. This then passes the amount that they bought to the next function, "plant_crops", to begin planting
def buy_process(coins,crop):
  print("~~~~~~~~~~~~~~~~~~~~~~~")
  print("How many do you want to buy?")
  try:
    amounts = int(input())
  except:
    print("Not an integer!")
    buy_process(coins,crop)
    amounts = 1

  if amounts <=0:
    print(f"You have to buy more than 0 {crop}!")
    print("Please put in an integer greater than 0")
    buy_process(coins,crop)

  if crop == "corn":
    adj = corn.price
  elif crop == "wheat":
    adj = wheat.price
  elif crop == "rice":
    adj = rice.price
  elif crop == "peppers":
    adj = peppers.price

  cost = coins - amounts*adj
  if cost < 0:
    print("You cannot buy that much! You don't have that much money")
    return()
  else:
    print(f"You successfully bought {amounts} {crop}")
    values = [amounts,(cost)]

    return(values)
    os.system('clear')   

#This process lets the user plant the crops only in locations where there is not already a crop growing
#
def plant_crops(farmplot,crop,amount,farmgrowth):
  go = True
  crops = 0
  while go == True:
    if amount == 0:
      print(f"You have no more {crop}")
      print("You will now go back to the home screen...")
      return()


    print(f"Where do you want to place your {crop} which you have {amount} left?")
    print("Insert a coordinate i.e. 0,0 for the top left and 2,2 for the bottom right")
    print("Your Farm")
    for r in range(3):
      for c in range(3):
        print(f"|{farmplot[r][c]}|", end="")
      print()

    print("~~~~~~~~~~~~~~~~")


    for i in range(3):
      for j in range(3):
        if farmplot[i][j] != "empty":
          crops+=1

    #Checks to see if the farmplot is full, which brings them back to the home screen
    if crops == 9:
      os.system('clear')
      print("Your farmplot is full!, returning to home screen")
      go = False
      os.system('clear')
      return()

    else:
      crops = 0 #Resets the counting of crops

      try:
        coords = input().split(",")
        x = int(coords[0])
        y = int(coords[1])
        if x >= 3 or y>=3 or x <= -1 or y <= -1:
          print("Those aren't valid coords, (OUT OF BOUNDS)")
          plant_crops(farmplot, crop, amount, farmgrowth)
      except:
        print("Those aren't valid coords, (FORMATTING ISSUE)")
        #plant_crops(farmplot,crop,amount, farmgrowth)



      else:      
        #Plants the crop, and puts its crop respective timer into a 2d list
        if farmplot[x][y] == "empty":
          os.system('clear')
          print("Nice job you planted" , crop)
          farmplot[x][y] = crop
          if crop == "wheat" or crop == "rice":
            farmgrowth[x][y] = 1
          else:
            farmgrowth[x][y] = 2
          amount-=1

        else:
          os.system('clear')
          print("There's already a crop there!!!")
          print("Please plant a crop at a different location")





