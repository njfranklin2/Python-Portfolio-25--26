#norah
#pokemon.py
#pokemon game

#init
import time
import random
#func

#starting level, mood, day, and name
pokename = str.capitalize(input("Please name your Pokemon: "))
daynum = 1
pokelevel = 1
mood = 10
#the levels help keep track of which image to use for our pokemon.
def level1():
    print((r"             _.--\"\"`-..\n"))
    print((r"           ,'          `.\n"))
    print((r"         ,'          __  `.\n"))
    print((r"        /|          \" __   \\\n"))
    print((r"       , |           / |.   .\n"))
    print((r"       |,'          !_.'|   |\n"))
    print((r"     ,'             '   |   |\n"))
    print((r"    /              |`--'|   |\n"))
    print((r"   |                `---'   |\n"))
    print((r"    .   ,                   |                       ,\".\n"))
    print((r"     ._     '           _'  |                    , ' \\ `\n"))
    print((r" `.. `.`-...___,...---\"\"    |       __,.        ,`\"   L,|\n"))
    print((r" |, `- .`._        _,-,.'   .  __.-'-. /        .   ,    \\\n"))
    print(("-:..     `. `-..--_.,.<       `\"      / `.        `-/ |   .\n"))
    print((r" `,         \"\"\"\"'     `.              ,'         |   |  ',,\n"))
    print((r"   `.      '            '            /          '    |'. |/\n"))
    print((r"     `.   |              \\       _,-'           |       ''\n"))
    print((r"       `._'               \\   '\"\\                .      |\n"))
    print((r"          |                '     \\                `._  ,'\n"))
    print((r"          |                 '     \\                 .'|\n"))
    print((r"          |                 .      \\                | |\n"))
    print((r"          |                 |       L              ,' |\n"))
    print((r"          `                 |       |             /   '\n"))
    print((r"           \\                |       |           ,'   /\n"))
    print((r"         ,' \\               |  _.._ ,-..___,..-'    ,'\n"))
    print((r"        /     .             .      `!             ,j'\n"))
    print((r"       /       `.          /        .           .'/\n"))
    print((r"      .          `.       /         |        _.'.'\n"))
    print((r"       `.          7`'---'          |------\"'_.'\n"))
    print((r"      _,.`,_     _'                ,''-----\"'\n"))
    print((r"  _,-_    '       `.     .'      ,\\\n"))
    print((r"  -\" /`.         _,'     | _  _  _.|\n"))
    print((r"   \"\"--'---\"\"\"\"\"'        `' '! |! /\n"))
    print((r"                           `\" \" -' mh\n"))
    print(("\n"))
    print(("\n"))
def level2():
    print((r"                     ,-'`\\\n"))
    print((r"                 _,\"'    j\n"))
    print((r"          __....+       /               .\n"))
    print((r"      ,-'\"             /               ; `-._.'.\n"))
    print((r"     /                (              ,'       .'\n"))
    print((r"    |            _.    \\             \\   ---._ `-.\n"))
    print((r"    ,|    ,   _.'  Y    \\             `- ,'   \\   `.`.\n"))
    print((r"    l'    \\ ,'._,\\ `.    .              /       ,--. l\n"))
    print((r" .,-        `._  |  |    |              \\       _   l .\n"))
    print((r"/              `\"--'    /              .'       ``. |  )\n"))
    print((".\\    ,                 |                .        \\ `. '\n"))
    print(("`.                .     |                '._  __   ;. \\'\n"))
    print((r" `-..--------...'       \\                  `'  `-\"'.  \\\n"))
    print((r"     `......___          `._                        |  \\\n"))
    print((r"              /`            `..                     |   .\n"))
    print((r"             /|                `-.                  |    L\n"))
    print((r"            / |               \\   `._               .    |\n"))
    print((r"          ,'  |,-\"-.   .       .     `.            /     |\n"))
    print((r"        ,'    |     '   \\      |       `.         /      |\n"))
    print((r"      ,'     /|       \\  .     |         .       /       |\n"))
    print((r"    ,'      / |        \\  .    +          \\    ,'       .'\n"))
    print((r"   .       .  |         \\ |     \\          \\_,'        / j\n"))
    print((r"   |       |  L          `|      .          `        ,' '\n"))
    print((r"   |    _. |   \\          /      |           .     .' ,'\n"))
    print((r"   |   /  `|    \\        .       |  /        |   ,' .'\n"))
    print((r"   |   ,-..\\     -.     ,        | /         |,.' ,'\n"))
    print((r"   `. |___,`    /  `.   /`.       '          |  .'\n"))
    print((r"     '-`-'     j     ` /.\"7-..../|          ,`-'\n"))
    print((r"               |        .'  / _/_|          .\n"))
    print((r"               `,       `\"'/\"'    \\          `.\n"))
    print((r"                 `,       '.       `.         |\n"))
    print((r"            __,.-'         `.        \\'       |\n"))
    print((r"           /_,-'\\          ,'        |        _.\n"))
    print((r"            |___.---.   ,-'        .-':,-\"`\\,' .\n"))
    print((r"                 L,.--\"'           '-' |  ,' `-.\\\n"))
    print((r"                                       `.' mh\n"))
def level3():
    print((r"                .\"-,.__\n"))
    print((r"                `.     `.  ,\n"))
    print((r"             .--'  .._,'\"-' `.\n"))
    print((r"            .    .'         `'\n"))
    print((r"            `.   /          ,'\n"))
    print((r"              `  '--.   ,-\"'\n"))
    print((r"               `\"`   |  \\\n"))
    print((r"                  -. \\, |\n"))
    print((r"                   `--Y.'      ___.\n"))
    print((r"                        \\     L._, \\\n"))
    print((r"              _.,        `.   <  <\\                _\n"))
    print((r"            ,' '           `, `.   | \\            ( `\n"))
    print((r"         ../, `.            `  |    .\\`.           \\ \\_\n"))
    print((r"        ,' ,..  .           _.,'    ||\\l            )  '\".\n"))
    print((r"       , ,'   \\           ,'.-.`-._,'  |           .  _._`.\n"))
    print((r"     ,' /      \\ \\        `' ' `--/   | \\          / /   ..\\\n"))
    print((r"   .'  /        \\ .         |\\__ - _ ,'` `        / /     `.`.\n"))
    print((r"   |  '          ..         `-...-\"  |  `-'      / /        . `.\n"))
    print((r"   | /           |L__           |    |          / /          `. `.\n"))
    print((r"  , /            .   .          |    |         / /             ` `\n"))
    print((r" / /          ,. ,`._ `-_       |    |  _   ,-' /               ` \\\n"))
    print((r"/ .           \\\"`_/. `-_ \\_,.  ,'    +-' `-'  _,        ..,-.    \\`.\n"))
    print((".  '         .-f    ,'   `    '.       \\__.---'     _   .'   '     \\ \\\n"))
    print(("' /          `.'    l     .' /          \\..      ,_|/   `.  ,'`     L`\n"))
    print(("|'      _.-\"\"` `.    \\ _,'  `            \\ `.___`.'\"`-.  , |   |    | \\\n"))
    print(("||    ,'      `. `.   '       _,...._        `  |    `/ '  |   '     .|\n"))
    print(("||  ,'          `. ;.,.---' ,'       `.   `.. `-'  .-' /_ .'    ;_   ||\n"))
    print(("|| '              V      / /           `   | `   ,'   ,' '.    !  `. ||\n"))
    print(("||/            _,-------7 '              . |  `-'    l         /    `||\n"))
    print((". |          ,' .-   ,' ||               | .-.        `.      .'     ||\n"))
    print((r"`'        ,'    `\".'    |               |    `.        '. -.'       `'\n"))
    print((r"         /      ,'      |               |,'    \\-.._,.'/'\n"))
    print((r"         .     /        .               .       \\    .''\n"))
    print((r"       .`.    |         `.             /         :_,'.'\n"))
    print((r"         \\ `...\\   _     ,'-.        .'         /_.-'\n"))
    print((r"          `-.__ `,  `'   .  _.>----''.  _  __  /\n"))
    print((r"               .'        /\"'          |  \"'   '_\n"))
    print((r"              /_|.-'\\ ,\".             '.'`__'-( \\\n"))
    print((r"                / ,\"'\"\\,'               `/  `-.|\" mh\n"))
#changes name per evolution and image
def evolve():
    if pokelevel < 10:
        level1()
        pokename = f"{pokename}mander"
        print(f"You are a stage 1 {pokename}!")
    if pokelevel >= 10 and pokelevel < 20:
        level2()
        if pokelevel == 10:
            print("You have evolved!!")
        pokename = f"{pokename}meleon"
        print(f"You are a stage 2 {pokename}!")
    if pokelevel >= 20 and pokelevel <= 30:
        level3()
        if pokelevel == 20:
            print("You have evolved!!")
        pokename = f"{pokename}izard"
        print(f"You are a stage 3 {pokename}!")

#main
while True:
    #prints the menu screen, to choose next action
    print(f"Day {daynum}")
    print("What would you like to do today?")
    print("   Train Pokemon")
    print("   See Pokemon Info")
    print("   Sleep Until Next Day")
    print("   Battle Friendly Gym Partners ")
    print("   Battle Final Boss")
    print("   Exit Game")

    #gets answer fpr what they want to do, brings to next option
    ans = str.lower(input("   "))

    #trains pokemon w random opponent
    if ans == "train pokemon" or ans == "train":
        print("Training Your Pokemon")
        time.sleep(1)
        print("Practicing Skills")
        time.sleep(1)
        print("Your Pokemon Leveled Up!!!")
        pokelevel = pokelevel+1
        time.sleep(2)
        daynum = daynum + 1
        print("Sleeping Through The Night")
        time.sleep(2)

    #shows info - image, level, evolution, name, and more
    if ans == "see pokemon info" or ans == "see info" or ans == "info":
        evolve()
        print(f"{pokename} is at level {pokelevel}")
        print(f"{pokename} feels {mood}/10")
        if mood <= 5:
            print(f"Win some more battles! {pokename} needs something to lift them up!")
        time.sleep(5)

    #skips day if they want to rest pokemon, if mood was finished, this would improve it
    if ans == "sleep" or ans == "sleep until next day":
        daynum = daynum + 1
        print("Sleeping Through The Night")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(1)
        print(".")
        time.sleep(2)

    #battle gym, 70/30 winning odds, adds 2 levels and was supposed to boost mood but unfinished
    if ans == "battle friendly gym partners" or ans == "battle gym" or ans == "battle gym partners" or ans == "gym":
        print("Welcome to the gym, where winning rewards +2 levels!")
        print(f"Remember, {pokename}'s mood plays a huge role in winning!")
        print(f"their mood is currently {mood}/10.")
        time.sleep(0.5)
        print("Are you ready to battle?")
        ready = str.lower(input())
        if ready == "yes" or ready == "yeah" or ready == "ready" or ready == "yea":
            gympartner = "Bullbasur", "Ivysaur", "Venusaur", "Charmander", "Charmeleon", "Charizard", "Squirtle", "Wartortle", "Blastoise", "Caterpie", "Metapod", "Butterfree"
            opponent = random.choice(gympartner)
            print(f"Your opponent is... {opponent}!")
            time.sleep(0.5)
            print("3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            print("Go!!")
            time.sleep(0.5)
            print("What attack would you like to use: Kick, Flame, or Slice")
            input()
            print("Great Job!")
            time.sleep(0.5)
            print("One more!")
            time.sleep(0.5)
            print("Would you like to use: Punch, Wave, or Boulder")
            input()
            print("Wonderful! Lets see how you did!")
            time.sleep(0.5)
            winner = random.randint(1,100)
            if mood > 7:
                if winner <= 50:
                    print("You won!!")
                    time.sleep(0.5)
                    print("+2 levels")
                    pokelevel = pokelevel + 2
                    daynum = daynum + 1
                    if mood < 10:
                        mood = mood + 1
                    time.sleep(2)
                if winner > 50:
                    print("Sorry, you lost, try again next time.")
                    daynum = daynum + 1
                    if mood > 0:
                        mood = mood - 1
                    time.sleep(2)
            if mood < 7:
                if winner <= 30:
                    print("You won!!")
                    time.sleep(0.5)
                    print("+2 levels")
                    pokelevel = pokelevel + 2
                    daynum = daynum + 1
                    if mood < 10:
                        mood = mood + 1
                    time.sleep(2)
                if winner > 30:
                    print("Sorry, you lost, try again next time.")
                    daynum = daynum + 1
                    if mood > 0:
                        mood = mood - 1
                    time.sleep(2)

        elif ready == "no":
            continue

    #final battle, game ends when done. harder to win when lower level
    if ans == "battle final boss" or ans == "final boss" or ans == "battle boss" or ans == "boss":
        print("Welcome to the final battle! The higher your level, the better chances you have")
        time.sleep(0.5)
        print("Fighting the final boss ends the game.")
        print("Are you ready to battle?")
        ready = str.lower(input())
        if ready == "yes" or ready == "yeah" or ready == "ready":
            finalopp = "Kanto", "Hoenn", "Alola", "Giovanni", "Paldea"
            opponent = random.choice(finalopp)
            print(f"Your final opponent is... {opponent}!!")
            time.sleep(0.5)
            print("3...")
            time.sleep(1)
            print("2...")
            time.sleep(1)
            print("1...")
            time.sleep(1)
            print("Go!!")
            time.sleep(0.5)
            print("How would you like to attack?")
            input()
            print("Nice hit!")
            time.sleep(0.5)
            print("Choose another attack, quick!")
            input()
            print("Great job!")
            if pokelevel < 10:
                winner = random.randint(1,100)
                if winner <= 10:
                    print("Wow! you won!")
                    time.sleep(0.5)
                    print("Congratulations on beating the game! Play again soon!!")
                    evolve()
                    print(f"{pokename} beat the game at level {pokelevel}")
                    break
                if winner > 10:
                    print("Sorry, you lost!")
                    time.sleep(0.5)
                    print("To battle the final boss again, you must play the game again.")
                    time.sleep(0.5)
                    print("We hope to see you again soon!")
                    evolve()
                    print(f"{pokename} finished at level {pokelevel}")
                    break
            if pokelevel >= 10 and pokelevel < 20:
                winner = random.randint(1,100)
                if winner <= 50:
                    print("Wow! you won!")
                    time.sleep(0.5)
                    print("Congratulations on beating the game! Play again soon!!")
                    evolve()
                    print(f"{pokename} beat the game at level {pokelevel}")
                    break
                if winner > 50:
                    print("Sorry, you lost!")
                    time.sleep(0.5)
                    print("To battle the final boss again, you must play the game again.")
                    time.sleep(0.5)
                    print("We hope to see you again soon!")
                    evolve()
                    print(f"{pokename} finished at level {pokelevel}")
                    break
            if pokelevel >= 20 and pokelevel <= 30:
                winner = random.randint(1,100)
                if winner <= 75:
                    print("Wow! you won!")
                    time.sleep(0.5)
                    print("Congratulations on beating the game! Play again soon!!")
                    evolve()
                    print(f"{pokename} beat the game at level {pokelevel}")
                    break
                if winner > 75:
                    print("Sorry, you lost!")
                    time.sleep(0.5)
                    print("To battle the final boss again, you must play the game again.")
                    time.sleep(0.5)
                    print("We hope to see you again soon!")
                    evolve()
                    print(f"{pokename} finished at level {pokelevel}")
                    break
        if ready == "no":
            continue

    #ends game if needed
    if ans == "exit" or ans == "exit game":
        end = str.lower(input("Are you sure? Your progress will be lost: "))
        if end == "yes" or end == "exit" or end == "exit game":
            break
        else:
            time.sleep(2)
            continue

#began to add mood aditions but UNFINISHED
