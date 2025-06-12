import random, os
from defcrops import Seeds

corn = Seeds("Corn",5,"Costs $5 and sells for ~$8. Grows in 2 turns",2)
wheat = Seeds("Wheat",2,"Costs $2 and sells for ~$5. Grows in 1 turns",1)
rice = Seeds("Rice",1,"Costs $1 and sells for ~$3. Grows in 1 turns",1)
peppers = Seeds("Pepper",10,"Costs $10 and sells for ~$20. Grows in 2 turns",2)

sell_prices = [8,5,3,20]
crops_sold = [0] * 4
last_turn = 1
length = len(sell_prices)

#If a new turn begins, this function will run and change the current sell prices of the crops by making an "adjustment factor" determined using a random number generating and adding that to the current sell price
#AND/OR, if the user sells a lot of one type of crop, the price of that crop will drop
def manipulate(sell_prices, turn):  
  global currentturn
  global last_turn
  print(f"Current Turn: {turn}")
  adj = 0.4
  if turn < 7:
    adj = 0.25
  else:
    adj = 0.55 #Makes the game more risky/chaotic at the end


  if turn > last_turn:
    last_turn = turn


    for i in range(length):
      price = sell_prices[i]
      demand = crops_sold[i]
      lower, upper = int(-adj*price)-1 - int(demand*0.2), int(adj*price)+1 - int(demand*0.2)
      newadj = random.randint(lower,upper)
      newprice = price + newadj

      if newprice <= 0:
        newprice = 1

      sell_prices[i] = newprice

  return(sell_prices)

#This function allows for users to sell their crops to the market, displaying their price, the amount they currently have, and inputs in an integer which is the number of crops they want to sell. Then they will gain that much money.
def market(coins,turn,harvested_crops):
  global sell_prices
  sell_prices = manipulate(sell_prices,turn)
  go = True

  print("~~~~~~~~~~~~~~~~~~~~")
  print("Welcome to the market!")
  print("Here you will be able to sell your crops to the market")
  print("However, the price of crops will change everyday")
  print("Also, if you sell too many crops the price will also drop")
  print(f"You currently have {coins} coins")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

  print("Current Prices | Amount you have")
  print(f"Corn:  ${sell_prices[0]:>7} | {harvested_crops[0]:>2}")
  print(f"Wheat: ${sell_prices[1]:>7} | {harvested_crops[1]:>2}")
  print(f"Rice: ${sell_prices[2]:>7} | {harvested_crops[2]:>2}")
  print(f"Peppers: ${sell_prices[3]:>7} | {harvested_crops[3]:>2}")



  print("(1) Sell Corn")
  print("(2) Sell Wheat")
  print("(3) Sell Rice")
  print("(4) Sell Peppers")
  print("(5) Go back to farm (Sell nothing)")
  print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")  

  while go == True:

    try:
      option = int(input("What do you want to do?" + "\n"))
    except:
      os.system('clear')
      print("That's not an integer, please put one in!")
      print()
      return(coins,turn,harvested_crops)

    if option == 1: #Corn
      corn_amount = harvested_crops[0]
      while True:
        try:
          amount = int(input("How much do you want to sell?" + "\n"))
        except:
          print("That's not an int!")

        if amount > corn_amount:
          print(f"You don't have that much! You only have {corn_amount}")
        else:
          os.system('clear')
          corn_amount -= amount
          crops_sold[0] += amount
          harvested_crops[0] -= amount
          profit = sell_prices[0] * amount
          newbal = coins + profit
          print(f"You made {profit}, and now have {newbal}")
          values = [newbal, harvested_crops]
          return(values)

    elif option == 2: #Wheat
      wheat_amount = harvested_crops[1]
      while True:
        try:
          amount = int(input("How much do you want to sell?" + "\n"))
        except:
          print("That's not an int!")

        if amount > wheat_amount:
          print(f"You don't have that much! You only have {wheat_amount}")
        else:
          os.system('clear')
          wheat_amount -= amount
          crops_sold[1] += amount
          harvested_crops[1] -= amount
          profit = sell_prices[1] * amount
          newbal = coins + profit
          print(f"You made {profit}, and now have {newbal}")
          values = [newbal, harvested_crops]
          return(values)

    elif option == 3: #Rice
      rice_amount = harvested_crops[2]
      while True:
        try:
          amount = int(input("How much do you want to sell?" + "\n"))
        except:
          print("That's not an int!")

        if amount > rice_amount:
          print(f"You don't have that much! You only have {rice_amount}")
        else:
          os.system('clear')
          rice_amount -= amount
          crops_sold[2] += amount
          harvested_crops[2] -= amount
          profit = sell_prices[2] * amount
          newbal = coins + profit
          print(f"You made {profit}, and now have {newbal}")
          values = [newbal, harvested_crops]
          return(values)

    elif option == 4: #Peppers
      pepper_amount = harvested_crops[3]
      while True:
        try:
          amount = int(input("How much do you want to sell?" + "\n"))
        except:
          print("That's not an int!")

        if amount > pepper_amount:
          print(f"You don't have that much! You only have {pepper_amount}")
        else:
          os.system('clear')
          pepper_amount -= amount
          crops_sold[3] += amount
          harvested_crops[3] -= amount
          profit = sell_prices[3] * amount
          newbal = coins + profit
          print(f"You made {profit}, and now have {newbal}")
          values = [newbal, harvested_crops]
          return(values)

    elif option == 5:
      os.system('clear')
      go = False
      values = [coins,harvested_crops]
      return(values)

    else:
      print("Not a valid option! Please put in an integer i.e. '1'")
      market(coins,turn,harvested_crops)
