#Starbucks Dataset
#Website Name: Starbucks.com
#Dataset URL:
# https://docs.google.com/spreadsheets/d/19FnfbdWOy1t5VY19Xq5p3JFZheE_0jEj0YMWdAVyq-U/edit?usp=sharing
#Dataset Source: https://www.starbucks.com/menu


#Starbucks.py
#Recommends a drink by filtering through the menu based on inputted preferences.

#init
import time
import pandas as pd
data = pd.read_csv("starbucks menu - Sheet1 (2).csv")

type = data['Type'].tolist()
cat_A = data['Category A'].tolist()
cat_B = data['Category B'].tolist()
item = data['Menu Item'].tolist()
filter1 = []

#func
def menulocate(typemenu,catamenu,catbmenu,itemmenu):
    filter1.clear()
    for i in range(len(item)):
        if typemenu in type[i]:
            if catamenu in cat_A[i]:
                if catbmenu in cat_B[i]:
                    if itemmenu in item[i]:
                        filter1.append(i)
                        return(data.loc[filter1])
                        break
        if itemmenu not in item:
            return("This is not a drink at starbucks")

def see_type_options(pref):
    filter1.clear()
    for i in range (len(item)):
        if pref in type[i]:
            filter1.append(i)
    return(data.loc[filter1])

def see_cata_options(pref1):
    filter1.clear()
    for i in range (len(item)):
        if pref1 in cat_A[i]:
            if cat_B[i] not in filter1:
                filter1.append(cat_B[i])
    return(filter1)

def see_catb_options(typemenu,catamenu,pref2):
    filter1.clear()
    for i in range (len(item)):
        if typemenu in type[i]:
            if catamenu in cat_A[i]:
                if pref2 in cat_B[i]:
                        filter1.append(item[i])
    return(filter1)

#main
while True:
    #\/ gets input on if user wants food, drink, or to exit
    userinput = input("""
    Welcome to starbucks!
    We have many options to choose from!
    Would you like
    a. A DRINK
    b. A FOOD ITEM
    c. EXIT
    """).lower()

    if userinput == "a": #user chose a. A DRINK
        userinput = "Drink"
       #\/ gives user all of the broad categories for drinks. Category A in my csv file.
        userinputDRINK = input("""
        We have lots of drinks,
        These are your GENERAL drink options
        a. Protein Beverages
        b. Hot Coffee
        c. Cold Coffee
        d. Matcha
        e. Hot Tea
        f. Cold Tea
        g. Refreshers
        h. Frappuccino® Blended Beverage
        i. Hot Chocolate, Lemonade & More
        j. Bottled Beverages
        Which one would you like today?
        """).lower()

        if userinputDRINK == "a":
            #the user chose Category A drink choice of A, so, like before,
            #I will give the user all options for Protein beverages,
            #and this process will repeat through the Category B list,
            #until they decide on their final drink in the Menu Item list.
            userinputDRINK = "Protein Beverages"
            DRINKa = input(f"""
    These are your Specific drink options
    {see_cata_options(userinputDRINK)} a,b,c,etc
    Which type of {userinputDRINK.upper()} would you like today?
    """).lower()
            if DRINKa == "a":
                #gives users all final options from the past categories they chose
                #ALL "if DRINKa == "_": FUNCTIONS DO THIS!!!
                DRINKa = "High Protein Latte"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "b":
                DRINKa = "No Added Sugar Options"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)} a,b,c,etc
    Which type of {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

        if userinputDRINK == "b":
            #the user chose Category A drink choice of B,
            #so, i will take all the same steps
            #but this time through the Hot Coffee Category.
            userinputDRINK = "Hot Coffee"
            DRINKa = input(f"""
    These are your Specific drink options
    {see_cata_options(userinputDRINK)} a,b,c,etc
    Which type of {userinputDRINK.upper()} would you like today?
    """).lower()
            if DRINKa == "a":
                DRINKa = "Brewed Coffee"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                 continue

            if DRINKa == "b":
                DRINKa = "Americano"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "c":
                DRINKa = "Latte"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "d":
                DRINKa = "Cappuccino"
                DRINKb = input(f"""
    These are your final drink options
    {(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "e":
                DRINKa = "Mocha"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "f":
                DRINKa = "Macchiato"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "g":
                DRINKa = "Flat White"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "h":
                DRINKa = "Cortado"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "i":
                DRINKa = "Espresso Shot"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

        if userinputDRINK == "c":
            #the user chose Category A drink choice of C,
            #so, i will take all the same steps
            #but this time through the Cold Coffee Category.
            userinputDRINK = "Cold Coffee"
            DRINKa = input(f"""
    These are your Specific drink options
    {see_cata_options(userinputDRINK)} a,b,c,etc
    Which type of {userinputDRINK.upper()} would you like today?
    """).lower()
            if DRINKa == "a":
                DRINKa = "Cold Brew"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa,DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "b":
                DRINKa = "Nitro Cold Brew"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa,DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "c":
                DRINKa = "Iced Coffee"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa,DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "d":
                DRINKa = "Iced Shaken Espresso"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa,DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "e":
                DRINKa = "Iced Espresso"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa,DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "f":
                DRINKa = "Iced Americano"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa,DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "g":
                DRINKa = "Iced Latte"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa,DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "h":
                DRINKa = "Iced Mocha"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa,DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "i":
                DRINKa = "Iced Macchiato"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa,DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "j":
                DRINKa = "Iced Flat White"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa,DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

        if userinputDRINK == "d":
            #the user chose Category A drink choice of D,
            #so, i will take all the same steps
            #but this time through the Matcha Category.
            userinputDRINK = "Matcha"
            DRINKa = input(f"""
    These are your Specific drink options
    {see_cata_options(userinputDRINK)} a,b,c,etc
    Which type of {userinputDRINK.upper()} would you like today?
    """).lower()
            if DRINKa == "a":
                DRINKa = "Classic Matcha"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa,DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "b":
                DRINKa = "Specialty Matcha"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa,DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "c":
                DRINKa = "Protein Matcha"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa,DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

        if userinputDRINK == "e":
            #the user chose Category A drink choice of E,
            #so, i will take all the same steps
            #but this time through the Hot Tea Category.
            userinputDRINK = "Hot Tea"
            DRINKa = input(f"""
    These are your Specific drink options
    {see_cata_options(userinputDRINK)} a,b,c,etc
    Which type of {userinputDRINK.upper()} would you like today?
    """).lower()
            if DRINKa == "a":
                DRINKa = "Matcha"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa,DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "b":
                DRINKa = "Tea Latte"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa,DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "c":
                DRINKa = "Brewed Tea"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa,DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

        if userinputDRINK == "f":
            #the user chose Category A drink choice of F,
            #so, i will take all the same steps
            #but this time through the Cold Tea Category.
            userinputDRINK = "Cold Tea"
            DRINKa = input(f"""
    These are your Specific drink options
    {see_cata_options(userinputDRINK)} a,b,c,etc
    Which type of {userinputDRINK.upper()} would you like today?
    """).lower()
            if DRINKa == "a":
                DRINKa = "Iced Matcha"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa,DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "b":
                DRINKa = "Iced Tea Latte"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa,DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "c":
                DRINKa = "Iced Tea"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa,DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

        if userinputDRINK == "g":
            #the user chose Category A drink choice of G,
            #so, i will take all the same steps
            #but this time through the Refreshers Category.
            userinputDRINK = "Refreshers"
            DRINKa = input(f"""
    These are your Specific drink options
    {see_cata_options(userinputDRINK)} a,b,c,etc
    Which type of {userinputDRINK.upper()} would you like today?
    """).lower()
            if DRINKa == "a":
                DRINKa = "Cannon Ball Drink"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                 continue

            if DRINKa == "b":
                DRINKa = "Lemonade Refreshers"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "c":
                DRINKa = "Coconutmilk Refreshers"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "d":
                DRINKa = "Refreshers"
                DRINKb = input(f"""
    These are your final drink options
    {(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

        if userinputDRINK == "h":
            #the user chose Category A drink choice of H,
            #so, i will take all the same steps
            #but this time through the Frappuccino® Blended Beverage Category.
            userinputDRINK = "Frappuccino® Blended Beverage"
            DRINKa = input(f"""
    These are your Specific drink options
    {see_cata_options(userinputDRINK)} a,b,c,etc
    Which type of {userinputDRINK.upper()} would you like today?
    """).lower()
            if DRINKa == "a":
                DRINKa = "Coffee Frappuccino®"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "b":
                DRINKa = "Creme Frappuccino®"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)} a,b,c,etc
    Which type of {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

        if userinputDRINK == "i":
            #the user chose Category A drink choice of I,
            #so, i will take all the same steps
            #but this time through the Hot Chocolate, Lemonade & More Category.
            userinputDRINK = "Hot Chocolate, Lemonade & More"
            DRINKa = input(f"""
    These are your Specific drink options
    {see_cata_options(userinputDRINK)} a,b,c,etc
    Which type of {userinputDRINK.upper()} would you like today?
    """).lower()
            if DRINKa == "a":
                DRINKa = "Hot Chocolate"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                 continue

            if DRINKa == "b":
                DRINKa = "Lemonade"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "c":
                DRINKa = "Milk & Steamers"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

        if userinputDRINK == "j":
            #the user chose Category A drink choice of J,
            #so, i will take all the same steps
            #but this time through the Bottled Beverages Category.
            userinputDRINK = "Bottled Beverages"
            DRINKa = input(f"""
    These are your Specific drink options
    {see_cata_options(userinputDRINK)} a,b,c,etc
    Which type of {userinputDRINK.upper()} would you like today?
    """).lower()
            if DRINKa == "a":
                DRINKa = "Water & Sparkling"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                 continue

            if DRINKa == "b":
                DRINKa = "Protein & Milk"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "c":
                DRINKa = "Juice"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "d":
                DRINKa = "Soda"
                DRINKb = input(f"""
    These are your final drink options
    {(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

            if DRINKa == "e":
                DRINKa = "Energy"
                DRINKb = input(f"""
    These are your final drink options
    {see_catb_options(userinput,userinputDRINK,DRINKa)}
    Which {DRINKa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your drink:
        {menulocate(userinput,userinputDRINK,DRINKa, DRINKb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                    continue

    if userinput == "b": #user chose b. A FOOD ITEM
        userinput = "Food"
        #\/ gives user all of the broad categories for foods. Category A in my csv file.
        userinputFOOD = input("""
        We have lots of food,
        These are your GENERAL food options
        a. Breakfast
        b. Bakery
        c. Treats
        d. Lunch
        e. Lite Bites
        Which one would you like today?
        """).lower()

        #All of these if statements take input from user based on userinputFOOD,
        #and show all of the general options for that. Category B in my cvs file

        if userinputFOOD == "a":
            userinputFOOD = "Breakfast"
            FOODa = input(f"""
    These are your Specific food options
    {see_cata_options(userinputFOOD)} a,b,c,etc
    Which type of {userinputFOOD.upper()} would you like today?
    """).lower()
            if FOODa == "a":
                FOODa = "Breakfast Sandwiches"
                FOODb = input(f"""
    These are your final food options
    {see_catb_options(userinput,userinputFOOD,FOODa)}
    Which {FOODa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your food:
        {menulocate(userinput,userinputFOOD,FOODa, FOODb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                 continue

            if FOODa == "b":
                FOODa = "Breakfast Wraps"
                FOODb = input(f"""
    These are your final food options
    {see_catb_options(userinput,userinputFOOD,FOODa)}
    Which {FOODa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your food:
        {menulocate(userinput,userinputFOOD,FOODa, FOODb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                 continue

            if FOODa == "c":
                FOODa = "Egg Bites & Bakes"
                FOODb = input(f"""
    These are your final food options
    {see_catb_options(userinput,userinputFOOD,FOODa)}
    Which {FOODa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your food:
        {menulocate(userinput,userinputFOOD,FOODa, FOODb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                 continue

            if FOODa == "d":
                FOODa = "More Breakfast Classics"
                FOODb = input(f"""
    These are your final food options
    {see_catb_options(userinput,userinputFOOD,FOODa)}
    Which {FOODa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your food:
        {menulocate(userinput,userinputFOOD,FOODa, FOODb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                 continue

        if userinputFOOD == "b":
            #the user chose Category A food choice of A, so, like before,
            #I will give the user all options for breakfast options,
            #and this process will repeat through the Category B list,
            #until they decide on their final food in the Menu Item list.
            userinputFOOD = "Bakery"
            FOODa = input(f"""
    These are your Specific food options
    {see_cata_options(userinputFOOD)} a,b,c,etc
    Which type of {userinputFOOD.upper()} would you like today?
    """).lower()
            if FOODa == "a":
                FOODa = "Croissants & Danishes"
                FOODb = input(f"""
    These are your final food options
    {see_catb_options(userinput,userinputFOOD,FOODa)}
    Which {FOODa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your food:
        {menulocate(userinput,userinputFOOD,FOODa, FOODb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                 continue

            if FOODa == "b":
                FOODa = "Loaves, Muffins, & Cakes"
                FOODb = input(f"""
    These are your final food options
    {see_catb_options(userinput,userinputFOOD,FOODa)}
    Which {FOODa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your food:
        {menulocate(userinput,userinputFOOD,FOODa, FOODb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                 continue

            if FOODa == "c":
                FOODa = "Bagels"
                FOODb = input(f"""
    These are your final food options
    {see_catb_options(userinput,userinputFOOD,FOODa)}
    Which {FOODa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your food:
        {menulocate(userinput,userinputFOOD,FOODa, FOODb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                 continue

        if userinputFOOD == "c":
            #the user chose Category A food choice of A, so, like before,
            #I will give the user all options for breakfast options,
            #and this process will repeat through the Category B list,
            #until they decide on their final food in the Menu Item list.
            userinputFOOD = "Treats"
            FOODa = input(f"""
    These are your Specific food options
    {see_cata_options(userinputFOOD)} a,b,c,etc
    Which type of {userinputFOOD.upper()} would you like today?
    """).lower()
            if FOODa == "a":
                FOODa = "Cake Pops"
                FOODb = input(f"""
    These are your final food options
    {see_catb_options(userinput,userinputFOOD,FOODa)}
    Which {FOODa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your food:
        {menulocate(userinput,userinputFOOD,FOODa, FOODb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                 continue

            if FOODa == "b":
                FOODa = "Cookies, Brownies, & Bars"
                FOODb = input(f"""
    These are your final food options
    {see_catb_options(userinput,userinputFOOD,FOODa)}
    Which {FOODa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your food:
        {menulocate(userinput,userinputFOOD,FOODa, FOODb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                 continue

        if userinputFOOD == "d":
            #the user chose Category A food choice of A, so, like before,
            #I will give the user all options for breakfast options,
            #and this process will repeat through the Category B list,
            #until they decide on their final food in the Menu Item list.
            userinputFOOD = "Lunch"
            FOODa = input(f"""
    These are your Specific food options
    {see_cata_options(userinputFOOD)} a,b,c,etc
    Which type of {userinputFOOD.upper()} would you like today?
    """).lower()
            if FOODa == "a":
                FOODa = "Lunch Sandwiches"
                FOODb = input(f"""
    These are your final food options
    {see_catb_options(userinput,userinputFOOD,FOODa)}
    Which {FOODa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your food:
        {menulocate(userinput,userinputFOOD,FOODa, FOODb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                 continue

            if FOODa == "b":
                FOODa = "Pockets"
                FOODb = input(f"""
    These are your final food options
    {see_catb_options(userinput,userinputFOOD,FOODa)}
    Which {FOODa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your food:
        {menulocate(userinput,userinputFOOD,FOODa, FOODb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                 continue

            if FOODa == "c":
                FOODa = "Protein Boxes"
                FOODb = input(f"""
    These are your final food options
    {see_catb_options(userinput,userinputFOOD,FOODa)}
    Which {FOODa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your food:
        {menulocate(userinput,userinputFOOD,FOODa, FOODb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                 continue

        if userinputFOOD == "e":
            #the user chose Category A food choice of A, so, like before,
            #I will give the user all options for breakfast options,
            #and this process will repeat through the Category B list,
            #until they decide on their final food in the Menu Item list.
            userinputFOOD = "Lunch"
            FOODa = input(f"""
    These are your Specific food options
    {see_cata_options(userinputFOOD)} a,b,c,etc
    Which type of {userinputFOOD.upper()} would you like today?
    """).lower()
            if FOODa == "a":
                FOODa = "Protein Boxes"
                FOODb = input(f"""
    These are your final food options
    {see_catb_options(userinput,userinputFOOD,FOODa)}
    Which {FOODa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your food:
        {menulocate(userinput,userinputFOOD,FOODa, FOODb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                 continue

            if FOODa == "b":
                FOODa = "Pockets"
                FOODb = input(f"""
    These are your final food options
    {see_catb_options(userinput,userinputFOOD,FOODa)}
    Which {FOODa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your food:
        {menulocate(userinput,userinputFOOD,FOODa, FOODb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                 continue

            if FOODa == "c":
                FOODa = "Protein Popcorn"
                FOODb = input(f"""
    These are your final food options
    {see_catb_options(userinput,userinputFOOD,FOODa)}
    Which {FOODa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your food:
        {menulocate(userinput,userinputFOOD,FOODa, FOODb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                 continue

            if FOODa == "d":
                FOODa = "Protein & Snack Bars"
                FOODb = input(f"""
    These are your final food options
    {see_catb_options(userinput,userinputFOOD,FOODa)}
    Which {FOODa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your food:
        {menulocate(userinput,userinputFOOD,FOODa, FOODb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                 continue

            if FOODa == "e":
                FOODa = "Salty Snacks"
                FOODb = input(f"""
    These are your final food options
    {see_catb_options(userinput,userinputFOOD,FOODa)}
    Which {FOODa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your food:
        {menulocate(userinput,userinputFOOD,FOODa, FOODb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                 continue

            if FOODa == "f":
                FOODa = "Sweet Snacks"
                FOODb = input(f"""
    These are your final food options
    {see_catb_options(userinput,userinputFOOD,FOODa)}
    Which {FOODa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your food:
        {menulocate(userinput,userinputFOOD,FOODa, FOODb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                 continue

            if FOODa == "g":
                FOODa = "Cheese & Fruit"
                FOODb = input(f"""
    These are your final food options
    {see_catb_options(userinput,userinputFOOD,FOODa)}
    Which {FOODa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your food:
        {menulocate(userinput,userinputFOOD,FOODa, FOODb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                 continue

            if FOODa == "h":
                FOODa = "Spreads"
                FOODb = input(f"""
    These are your final food options
    {see_catb_options(userinput,userinputFOOD,FOODa)}
    Which {FOODa.upper()} would you like today?
    """).title()
                time.sleep(1)
                print(f"""
        Here is the info on your food:
        {menulocate(userinput,userinputFOOD,FOODa, FOODb)}""")
                time.sleep(3)
                exit = input("Would you like to find another item? (yes/no) ")
                if exit == "no":
                    print("Thanks for stopping by!")
                    break
                if exit == "yes":
                 continue

    if userinput == "c": #user chose c. EXIT
        print("Thanks for stopping by!")
        break
