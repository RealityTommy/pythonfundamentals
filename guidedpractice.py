''' 

Functions

'''

def check_health(health):
    ''' Check to see if there is enough health can fight '''

    if health >= 40:
        return True
    else:
        return False

''' 

Game Details

'''

game_title = "Game Name"    # string data type

''' Player 1 details '''
player_name = "Player 1"   # string data type
player_health = 100        # integer data type
player_inventory = ["sword", "shield", "health_potion"]    # list data type
player_money = {"copper": 25, "silver": 2, "gold": 1}      # dictionary data type
player_quests = {"defeat dragon"}  # set data type
player_alive = True        # boolean data type

''' Enemy details '''
goblin_inventory = ["dagger", "health potion"]
dragon_health = 100
dragon_money = {"copper": 100, "silver": 25, "gold": 50}


''' Game intro '''
welcome_message = "Welcome, " + player_name + ", to " + game_title + "!"   # string concatenation
print(welcome_message)

print() # empty line

''' 

Level 1 

'''

print("Starting level 1...\n")
print("You found the a health potion and 5 copper.")

player_inventory.append("health_potion")   # list operation
print("Updated inventory:", player_inventory)

player_money["copper"] += 5    # dictionary operation and integer arithmetic
print("Updated money:", player_money)

print() # empty line

print("You got a new quest! Save the kitten from the goblin!")
player_quests.add("save kitten")   # set operation
print("Updated quests:", player_quests)

print() # empty line

''' Check to see if player can fight '''
print("Checking if you are well enough to fight...")
print("Your health:", player_health)

if player_health >= 40:
    # conditional statement
    print("You can fight!\n")
else:
    print("You are too weak. You run away.")

for goblin_health in range(100, 0, -10):
    # for loop
    if goblin_health <= 40:
        print("Goblin is weak! Finish it off!\n")
        break
    elif goblin_health == 90:
        print("Goblin is hurt, but now down.")
        continue

    print("You attack!")
    print("Goblin health:", goblin_health)

    print() # empty line

print("Goblin defeated and kitten saved!")
player_quests.discard("save kitten")

print("Updated quests:", player_quests)

print() # empty line

print("You took the Goblin's inventory.")
for item in goblin_inventory:
    player_inventory.append(item)
print("Updated inventory:", player_inventory)

print() # empty line

''' 

Level 2

'''

print("Starting level 2...\n")
print("There's a dragon! Defeat it!")

print() # empty line

while check_health(player_health):
    print("Dragon attacks!")
    player_health -= 10
    print("Player health:", player_health)

    print() # empty line

    print("You attack!")
    dragon_health -= 10
    print("Dragon health:", dragon_health)

    print() # empty line