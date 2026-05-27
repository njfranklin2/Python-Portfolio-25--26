#norah
#adventure.py
#choose your dream vacation

#init
#func
#generalized question
general = input("Which would you prefer: Ocean or Mountains? ")

#ocean rec
if general == "ocean":
    temp = input("Do you prefer tropical or wintery conditions? ")
    if temp == "tropical":
        print("You should take a trip to the Bahamas in the summertime!")
    else:
        print("You should take a trip on an Icelandic Cruise!")
else:
    temp = input("Do you prefer tropical or wintery conditions? ")
    if temp == "tropical":
        print("you should take a trip to St. Lucia in the summertime!")
    else:
        print("You should take a trip to an Italian Ski Resort!")
#main
