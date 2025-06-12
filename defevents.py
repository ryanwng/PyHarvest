events = []
import random
seed = random.randint(1,100)

#At the end of the day, there is a 37.5% chance of a random event occuring, with a 10% chance of each event running.
#This event will modify things such as the amount of coins the player has, blocking parts of the farm off, and it can speed up/slow down growth of some crops

def random_event(farmgrowth,farmplot,coins):
  values = [farmgrowth, farmplot, coins]
  go = True
  seednum = random.randint(1,8)
  if seednum <= 3: #~37.5% chance of an event
    event = random.randint(1,5)

    if event in events: #Runs to ensure a player will not encounter the same event twice in the same game!
      while go == True:
        event = random.randint(1,10)
        if event not in events:
          go = False
          events.append(event)

    events.append(event)
    if event == 1:
      print("Your grandparents decide to give you money to help you out on your farm")
      print("+5 Coins")
      coins+=5
      values = [farmgrowth, farmplot, coins]
      return(values)

    elif event == 2:
      print("A crop fairy has come to help you grow your crops.")
      print("All your crops in the top row have grown 1 turn faster!")
      for i in range(1):
        for j in range(3):
          farmgrowth[i][j] = -1

      print("Here is what your farm looks like now:")
      print("Your Farm")
      for r in range(3):
        for c in range(3):
          print(f"|{farmplot[r][c]}|", end="")
        print()
      values = [farmgrowth, farmplot, coins]
      return(values)

    elif event == 3:
      crops_lost = 0
      print("Due to the ongoing war, Ammar the bomber drops bombs on your field!")
      for i in range(3):
        for j in range(3):
          chance = random.randint(0,1)
          if chance == 0:
            farmplot[i][j] = "empty"
            farmgrowth[i][j] = -1
            crops_lost +=1

      print(f"You lost {crops_lost} crops!")
      print("Here is what your farm looks like now:")
      print("Your Farm")
      for r in range(3):
        for c in range(3):
          print(f"|{farmplot[r][c]}|", end="")
        print()
      values = [farmgrowth, farmplot, coins]
      return(values)

    elif event == 4:
      print("You did some research online and found Masroor's Tech Support Website")
      print("On the forums you discovered a new way of cryptomining")
      print("You did some cryptomining before your computer broke!")
      print("But you ended up making some money off of it")
      print("+15 coins")
      coins+=15
      values = [farmgrowth, farmplot, coins]
      return(values)

    elif event == 5:
      print("A massive meteorite hits your farm!")
      print("It makes your top right and top middle tile unusable permanently!")
      print("But, you manage to extract some rare metals from it")
      print("+40 coins")
      coins+=40

      farmplot[0][1]  = "METEOR"
      farmplot[0][2] = "METEOR"
      farmgrowth[0][1] = 999999
      farmgrowth[0][2] = 999999
      print("Here is what your farm looks like now:")
      print("Your Farm")
      for r in range(3):
        for c in range(3):
          print(f"|{farmplot[r][c]}|", end="")
        print()
      values = [farmgrowth, farmplot, coins]
      return(values)


    elif event == 6:
      print("From the ongoing war, you are forced to pay high amounts of tax for the war effort")
      print("-20 coins")
      coins -=20
      values = [farmgrowth, farmplot, coins]
      return(values)

    elif event == 7:
      crops_cursed = 0
      print("A witch has come cursing your crops!")
      print("some of your crops will now require an extra turn to grow")
      for i in range(3):
        for j in range(3):
          chance = random.randint(0,1)
          if chance == 0:
            farmgrowth[i][j] += 1
            crops_cursed +=1

      print(f"{crops_cursed} of your corps have been cursed!")
      values = [farmgrowth, farmplot, coins]
      return(values)

    elif event == 8:
      print("Your friend Jamshaid gives you 100 coins!!!")
      print("You go use some of it but you realize its counterfeit")
      print("However, you ended up getting some of the coins to your bank account anyways")
      print("You wonder if this is legal...")
      print("+15 coins")
      coins+=15
      values = [farmgrowth, farmplot, coins]
      return(values)

    elif event == 9:
      print("You go and get your fortune read")
      print("You pay 10 coins and get to see your fortune")
      fortune = random.randint(1,4)
      if fortune == 1:
        print("You got robbed!")
        print("Turns out it was a con artist")
        print("-10 coins")
        coins-=10
      elif fortune == 2:
        print("You get your fortune read but you think its a scam")
        print("You ask for a refund and get one")
        print("+0 coins")
      elif fortune == 3:
        print("You are a magnet to treasure for objects that you cannot possess...")
        print("You ended up finding 10 coins on the ground though, so you aren't sure how accurate that is")
        print("+10 coins")
        coins +=10
      elif fortune == 4:
        print("You go in the fortune test but no one is there...")
        print("However, you do find a big wad of cash")
        print("Maybe this is why people do fortune telling...")
        print("+20 coins")
        coins+=20
      values = [farmgrowth, farmplot, coins]
      return(values)

    elif event == 10:
      print("A crow came and ate one of your crops!")
      print("Pesky crows, if only you could buy a scarecrow...")
      i = random.randint(0,2)
      j = random.randint(0,2)
      farmplot[i][j] = "empty"

      print("Here is what your farm looks like now:")
      print("Your Farm")
      for r in range(3):
        for c in range(3):
          print(f"|{farmplot[r][c]}|", end="")
        print()
      values = [farmgrowth, farmplot, coins]
      return(values)

  return(values)
