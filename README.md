# PyHarvest 🌿

Grow, harvest, and sell crops to maximize your profit in just 10 days in this simple to play text-based terminal Python game.

---

## Overview
**PyHarvest** lets you, the player, plant seeds, manage crops, and sell them to earn money. <br> 
There will also be special events that may occur before the beginning of each day which may either help or harm your goal of becoming the wealthiest farmer. 

---

## Motivation
PyHarvest was a game designed for my High School CS project which allowed me to practice basic skills such as 2D Lists, Writing Files and Classes.

---

## Features
- Plant different crops with unique costs and harvest times  
- Simulate day-by-day progression  
- Market price fluctuations based on the actions of the player
- Leaderboard System
- Random Events
---

## Gamplay Example
![PyHarvest example gif](https://github.com/user-attachments/assets/cf4cb257-3ac2-4223-9d6a-355002d64366)
---

## Project Structure
main.py - Runs day progression logic and user interactions <br>
defcrops.py - Details of each crop such as its growth times <br>
defmarket.py - Handles selling of crops, and adjusts pricing based on supply sold <br>
defshop.py - Handles buying crops and planting them <br>
defother.py - Other features such as the tutorial, leaderboard, and crop growth <br>

---

## How to Run

**With Poetry:**
```bash
git clone https://github.com/ryanwng/PyHarvest.git
cd PyHarvest
poetry install
poetry run python main.py
```

**Without Poetry**
```
git clone https://github.com/ryanwng/PyHarvest.git
cd PyHarvest
python main.py
```

---

## Extra

This helpful youtube video on how to push from Replit to Github which I used (https://www.youtube.com/watch?v=tlR1l952HDg)
