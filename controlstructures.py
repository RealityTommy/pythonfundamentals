'''

This program illustrates conditional statements using an if-else statement, looping statements using
for and while loops, and control flow statements using break, continue, and pass statements.
Each example demonstrates how these control structures affect the flow of execution in the program.

'''

# Conditional Statements
player_health = 80
enemy_damage = 30

if player_health > enemy_damage:
    print("You defeated the enemy!")
else:
    print("Game Over. You were defeated by the enemy.")

# Looping Statements
print("\nCollecting treasures in a dungeon:")
for treasure in range(1, 6):
    print("Found treasure #", treasure)

print("\nSearching for the key to the next level:")
search_boxes = 0
while search_boxes < 5:
    search_boxes += 1
    if search_boxes == 5:
        print("Key found! Proceed to the next level.")
    else:
        print("Box is empty. Checking the next box... ")

# Control Flow Statements
print("\nEngaging in combat:")
for enemy_health in range(100, 0, -20):
    print("Enemy health:", enemy_health)
    if enemy_health <= 40:
        print("Enemy is weak! Finishing blow!")
        break
    elif enemy_health == 80:
        print("Enemy is hurt, but not down!")
        continue
    print("Attacking the enemy...")

# Pass statement
print("\nExploring a new area:")
for area in range(1, 6):
    if area == 3:
        pass  # Placeholder for future feature implementation
    else:
        print("Explored area #", area)