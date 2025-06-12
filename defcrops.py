#Class of seeds that is used to design crops easily and efficiently
class Seeds:
  def __init__(self,name,price,info,growth):
    self.name = name
    self.price = price
    self.info = info
    self.growth = growth

  def __str__(self):
    return(self.info)

# List of all of the crops
# corn = Seeds("Corn",5,"Costs $5 and sells for ~$8. Grows in 2 turns",2)
# wheat = Seeds("Wheat",2,"Costs $2 and sells for ~$5. Grows in 1 turns",1)
# rice = Seeds("Rice",1,"Costs $1 and sells for ~$3. Grows in 1 turns",1)
# peppers = Seeds("Pepper",10,"Costs $10 and sells for ~$20. Grows in 2 turns",2)

