#norah and Charlie
#slot.py
#slot machine

#init
import random
import time
#func
slots = ["☀", "☀", "☀", "☀", "★", "★", "★", "♥", "♥", "7"]
balance = 0
name = input("Please enter your name to save your scores: ")


while True:
    play = str.upper(input(f"""
          Welcome to the slot machine!
          777 = Jackpot! +100 tokens
                       OR
          ☀☀☀, ★★★, ♥♥♥ = Win! +20 tokens
          Each roll costs 10 tokens
          To deposit, type D
          To spin, type S
          To exit, type X
          Goodluck!
          Balance: {balance} Tokens
          """))
    time.sleep(0.5)
    if play == "D":
        money = int(input("Please deposit tokens of 50, 100, or 500 value: "))
        if money != 50 and money != 100 and money != 500:
            time.sleep(0.5)
            print("Unable to process your token, please deposit 50, 100, or 500")
            time.sleep(0.5)
            print("Redirecting to menu...")
            time.sleep(0.25)
        else:
            balance = balance + money
            print(f"Your new Balance is: {balance}")
    if play == "S" and balance>=10:
        balance = balance - 10
        slot1 = slots[random.randint(0,len(slots) - 1)]
        slot2 = slots[random.randint(0,len(slots) - 1)]
        slot3 = slots[random.randint(0,len(slots) - 1)]
        time.sleep(0.25)
        print("...")
        time.sleep(0.25)
        print("...")
        time.sleep(0.5)
        print(slot1, slot2, slot3)
        if slot1=="7" and slot2=="7" and slot3=="7":
            time.sleep(0.5)
            print("Congratulations! You won the Jackpot!")
            balance =  balance + 4000
            time.sleep(0.5)
        elif slot1==slot2 and slot2==slot3:
            time.sleep(0.5)
            print("You won!")
            balance = balance + 100
            time.sleep(0.5)
        else:
            time.sleep(0.5)
            print("Sorry, you lost")
            time.sleep(0.5)
    if play == "S" and balance<10:
        time.sleep(0.5)
        print("INSUFFICIENT FUNDS. PLEASE INSERT TOKENS.")
        time.sleep(1)
    if play == "X":
        time.sleep(0.5)
        print(f"Cashing out, you won {balance} tokens!")
        time.sleep(0.5)
        break
#main
