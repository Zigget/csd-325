# Made by: Samuel Sidzyik
# Module 1.4 Assignment.py
# Start Date January 11, 2026
# 
# Bottles on the wall song. Take an input and count down until song completes.
# Reused code from previous class to check input.
#
bottle_count = "."
while bottle_count == ".": # Keeps asking until a valid value passed
    try:
        bottle_count = input(f'Enter how many bottles we have. : ')
        if len(bottle_count) <= 0: # I won't allow blanks
            print('I will not allow blank entry.')
            bottle_count = "."
        elif len(bottle_count) > 2: # Just a quick limit to only have up to 99 on the count
            print("I'm limiting the number up to 99.")
            bottle_count = "."
        bottle_count = int(bottle_count)
        if bottle_count <= 0: # I won't allow zero or negatives
            print('I will not allow values less than 1.')
            bottle_count = "."

    except ValueError: # Catches non numerical values
        bottle_count = "."

    except: # I don't know what this catches but putting it in to be safe. Found in 6-29 image
        print('Unkown Error Occurred.')
        bottle_count = "."

#This is the song sung accurately. Also, I don't really drink so I made it Sprite because why not.
while bottle_count > 0:
    if bottle_count > 2:
        print(f"{bottle_count} bottles of Sprite on the wall, {bottle_count} bottles of Sprite!\nTake one down, pass it around, {bottle_count - 1} bottles of Sprite on the wall!\n")
    elif bottle_count > 1:
        print(f"{bottle_count} bottles of Sprite on the wall, {bottle_count} bottles of Sprite!\nTake one down, pass it around, 1 bottle of Sprite on the wall!\n")
    else:
        print(f"1 bottle of Sprite on the wall, 1 bottle of Sprite!\nTake one down, pass it around, no more bottles of Sprite on the wall!\n\nTime to buy more Sprite...\n")
    
    bottle_count = bottle_count - 1

# This is the song according to the assignment.
'''
while bottle_count > 0:
    if bottle_count > 1:
        print(f"{bottle_count} bottles of Sprite on the wall, {bottle_count} bottles of Sprite!\nTake one down, pass it around, {bottle_count - 1} bottle(s) of Sprite on the wall!")
    
    # This is what gets me. Your example accounts for non multiple 1 bottle, but puts in unkown plural "(s)" after bottles when the last one is removed. If you have that line coded separately already it should know to take account for no bottles
    else: 
        print(f"1 bottle of Sprite on the wall, 1 bottle of Sprite!\nTake one down, pass it around, no more bottles of Sprite on the wall!")
'''