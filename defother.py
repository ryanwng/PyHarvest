from defcrops import Seeds
import os
from csv import reader
corn = Seeds("Corn",5,"Costs $5 and sells for ~$8. Grows in 2 turns",2)
wheat = Seeds("Wheat",2,"Costs $2 and sells for ~$5. Grows in 1 turns",1)
rice = Seeds("Rice",1,"Costs $1 and sells for ~$3. Grows in 1 turns",1)
peppers = Seeds("Pepper",10,"Costs $10 and sells for ~$20. Grows in 2 turns",2)

#The tutorial, which describes how to play
def tutorial():
  print("Welcome to PyHarvest. This is a farming game where you try and make the most money possible")
  print("Buying and then selling crops will be your source of revenue")
  print("Be careful though, because each crop will buy/sell for different amounts along with taking longer or shorter to grow")
  print("Make sure to strategize and look at the prices to try and make the most money!")
  print("I recommend you go buy some crops first with the input '2'...")
  print()


#After every turn, this function is run to grow crops. The list 'farmgrowth' consists of how long it takes for the crop to grow, with each entry corresponding to each crop at the same location, which decreases by 1 each turn
#Once it reaches 0, the crop is harvested and added to the total amount of crops the player owns
def crop_growth(farmplot,farmgrowth,harvested_crops):
  value = harvested_crops
  for i in range(3):
    for j in range(3):
      crop = farmplot[i][j]
      if crop != "empty":
        farmgrowth[i][j] -= 1
        growthtime = farmgrowth[i][j]

        if growthtime <= 0:
          if crop == "corn":
            value[0]+=1
          elif crop == "wheat":
            value[1]+=1
          elif crop == "rice":
            value[2]+=1
          elif crop == "peppers":
            value[3]+=1
          farmplot[i][j] = "empty"
          farmgrowth[i][j] = -1
  return(value)


#At turn 10, the game is considered to be complete. At this point it takes the amount of coins along with the name of the player. This info is added to the data/leaderboard_data.txt file, and then info from that file is used to make a public leaderboard in output/leaderboard.txt file
def leaderboard(coins):
  fname1 = "output/leaderboard.txt"
  fname2 = "data/leaderboard_data.txt"

  print("You made this many coins...")
  print("Read and write info of a leaderboard given #coins, name")
  name = input("What is your name you want on the leaderboard?" + "\n")
  scores = [[int(coins), name]]

  #Writes the info to the leaderboard_data.txt file
  with open (fname2, "a") as outfile:
    outfile.write(f"{scores[0][0]},{scores[0][1]}" + "\n")

  scores = []
  #Reads the scores from leaderboard_data
  with open (fname2) as infile: 
    data = reader(infile)
    for line in data:
      score = int(line[0])
      name = line[1]
      scores.append([score,name])

  #Creates leaderboard in descending order
  leaderboard = sorted(scores, reverse = True)
  length = len(leaderboard)

  #Clears leaderboard.txt file
  with open (fname1, "w") as outfile:
    pass

  #Makes leaderboard.txt file
  with open (fname1, "a") as outfile:
    for i in range(length):
      rank = i+1
      score = leaderboard[i][0]
      name = leaderboard[i][1]
      if i == 0:
        outfile.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n")
        outfile.write("RANK    |   SCORE   |   NAME  " + "\n")
        outfile.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n")
      if i!= length-1:
        outfile.write(f"{rank:<7} | {score:>9} | {name:<5}" + "\n")
      else:
        outfile.write(f"{rank:<7} | {score:>9} | {name:<5}" + "\n")


  print("Make sure to check out the leaderboard to see how you did!")