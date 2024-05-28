'''

This program demonstrates various operations with variables and different data types.
It performs string concatenation, arithmetic operations with integers and floats, list operations (append, remove),
set operations (add, discard), dictionary operations (update), and boolean operations (and, or, not).

'''

# String concatenation
player_name = "Hero"
game_title = "AdventureQuest"
welcome_message = "Welcome, " + player_name + ", to " + game_title + "!"
print("String Concatenation (Welcome Message):", welcome_message)

# Integer arithmetic operations
player_level = 5
enemy_level = 3
level_difference = player_level - enemy_level
print("Integer Arithmetic Operations (Level Difference):", level_difference)

# Float arithmetic operations
pi = 3.14
radius = 1.5
circumference = 2 * pi * radius
area = pi * radius ** 2
print("Float Arithmetic Operations (Circumference and Area):")
print("Circumference of a Circle:", circumference)
print("Area of a Circle:", area)

# List operations
player_inventory = ["sword", "shield", "potion"]
player_inventory.append("scroll")
player_inventory.remove("shield")
print("List Operations (Player Inventory):", player_inventory)

# Set operations
active_quests = {"defeat dragon", "rescue princess", "collect treasure"}
active_quests.add("explore dungeon")
active_quests.discard("rescue princess")
print("Set Operations (Active Quests):", active_quests)

# Dictionary operations
player_info = {"name": "John", "level": 2, "gold": 50}
player_info["gold"] += 20
player_info["silver"] = 100
player_info.pop("silver")
print("Dictionary Operations (Player Info):", player_info)

# Boolean operations
is_alive = True
is_enemy_defeated = False
print("Boolean Operations (Game Status):")
print("Is Player Alive?", is_alive)
print("Is Enemy Defeated?", is_enemy_defeated)
