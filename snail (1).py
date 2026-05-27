#norah
#snail.py
#tortise snail and hare race simulation

#init
import random
#func
#main
finish_line = 50        #Finish Line
tortoise_pos = 0        #Starting Position
hare_pos = 0		    #Starting Position
snail_pos = 0           #Starting Position
is_hare_asleep = False  #Hare starts Awake
is_snail_riding = False #snail starts alone

while tortoise_pos < finish_line and hare_pos < finish_line:
# Tortoise always moves a short distance between 1 - 3 meters at random
    tortoise_pos = tortoise_pos + random.randint(1,3)
# Hare has a 30% chance of falling a sleep for a turn
    is_hare_asleep = random.choice(["True","True","True","False","False","False","False","False","False","False"])
# If Hare is awake, it will move 1 - 10 meters at random
    if is_hare_asleep == "False":
        hare_pos = hare_pos + random.randint(1,10)

    snail_pos = snail_pos + 1
    is_snail_riding = random.choice(["True","False","False","False","False","False","False","False","False","False"])
    if is_snail_riding == "True":
        snail_pos = hare_pos
# Print the positions of the Hare and Tortoise after each round
    print(f"| Hare: {hare_pos} | Tortoise: {tortoise_pos} | Snail: {snail_pos} |")
if tortoise_pos >= hare_pos and tortoise_pos > snail_pos:
    print("🐢 The Tortoise wins!")
if hare_pos > tortoise_pos and hare_pos > snail_pos:
    print("🐇 The Hare wins!")
if snail_pos > tortoise_pos and snail_pos >= hare_pos:
    print("🐌 The Snail wins!")
