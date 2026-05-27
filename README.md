# Python-Portfolio-25--26
AP CSP Projects

---------------------------------------------------------------------------------------------------------------------------

Adventure.py
Choose Your Dream Vacation  
A simple interactive Python program that guides users through a short series of questions to recommend a personalized vacation destination. The script uses conditional logic to tailor suggestions based on the user’s climate and environment preferences.

Summary — The program asks whether the user prefers the ocean or the mountains, then narrows the choice further by asking about tropical or wintery conditions. Based on the combination of answers, it prints a curated travel recommendation such as the Bahamas, Iceland, St. Lucia, or an Italian ski resort.

Key Features

Interactive decision flow — Users receive different outcomes based on their choices.

Beginner‑friendly Python logic — Demonstrates input handling and nested conditionals in a clean, readable format.

Customizable structure — Easy to expand with more destinations, questions, or categories.

---------------------------------------------------------------------------------------------------------------------------

Pokémon.py
Virtual Training & Evolution Simulator  
A text‑based Pokémon game where players name, train, battle, and evolve their custom Pokémon over multiple in‑game days. The program uses branching choices, random outcomes, and ASCII art to create a playful, interactive experience.

Summary  
Players begin with a base‑level Pokémon whose mood, level, and evolution progress change based on daily actions. Training increases levels, battles introduce risk and reward, and evolution stages unlock unique ASCII art representations. The game continues until the player chooses to exit or challenges the final boss.

Key Features

Interactive gameplay loop — Choose daily actions like training, battling, resting, or viewing Pokémon stats.

Evolution system with ASCII art — Three evolution stages, each displaying detailed Pokémon artwork pulled directly from the script.

Mood & battle mechanics — Mood affects battle odds, and battles can raise or lower mood.

Randomized opponents & outcomes — Gym partners and final bosses are selected randomly for replayability.

Progression‑based difficulty — Higher levels dramatically improve final boss win chances.

Custom Pokémon naming — Player‑chosen names evolve with each stage (e.g., Charmander → Charmeleon → Charizard‑style naming).

---------------------------------------------------------------------------------------------------------------------------

Slot.py 
Virtual Slot Machine Simulator  
A simple, fast‑paced slot machine game where players deposit tokens, spin the reels, and try their luck at winning jackpots or matching symbols. The game uses randomized outcomes and a clean text interface to create a classic casino‑style experience.

Summary  
Players begin by depositing tokens, then choose whether to spin, deposit more, or cash out. Each spin costs 10 tokens and generates three random symbols from a weighted list. Matching symbols award bonus tokens, while hitting 777 triggers a jackpot. The game continues until the player chooses to exit and cash out their final balance.

Key Features

Token‑based economy — Players deposit 50, 100, or 500‑value tokens and manage their balance strategically.

Weighted symbol system — The slot reel includes common and rare symbols, affecting win probability.

Jackpot mechanic — Rolling 7‑7‑7 awards a massive token bonus.

Clean text‑based UI — Simple prompts, suspenseful delays, and clear feedback after each spin.

Randomized outcomes — Uses Python’s random module to simulate authentic slot machine unpredictability.

Player name tracking — Saves the player’s name for scorekeeping and personalization.

---------------------------------------------------------------------------------------------------------------------------

Snail.py
Tortoise, Hare & Snail Race Simulator  
A fun, randomized race simulation inspired by the classic fable — but with a twist. Three racers (tortoise, hare, and snail) compete to reach a 50‑meter finish line, each with unique movement rules and unpredictable behaviors.

Summary  
The tortoise moves steadily each round, the hare alternates between sprinting and falling asleep, and the snail creeps forward unless it randomly decides to hitch a ride on the hare. The program prints each racer’s position every turn until one crosses the finish line. The winner is determined by comparing final positions once the race ends.

Key Features

Distinct movement patterns — Tortoise moves 1–3 meters, hare moves 1–10 meters when awake, snail moves 1 meter unless it rides the hare.

Randomized behavior — Hare sleep chance and snail ride chance introduce unpredictability.

Live race updates — Each round prints the current positions of all three racers.

Multiple possible winners — Any racer can win depending on luck and movement patterns.

Simple, readable logic — Great example of loops, randomness, and conditionals in Python.

---------------------------------------------------------------------------------------------------------------------------

Starbucks.py 
Interactive Drink Recommendation System
A text‑based, interactive program that guides users through Starbucks drink categories and recommends a specific menu item. It simulates a conversational ordering experience by narrowing down choices step‑by‑step based on user preferences.

Summary
The script loads the Starbucks dataset and walks the user through a branching decision process: choosing between drinks or food, selecting a major category, then a subcategory, and finally a specific item. Behind the scenes, filtering functions search the dataset for matching entries. Once a drink is selected, the program prints the full menu information and offers to restart the search.

Key Features
Interactive CLI navigation — Users explore the Starbucks menu through guided prompts.

Dynamic filtering functions — Real‑time search using functions like menulocate, see_type_options, and see_catb_options.

Accurate item lookup — Returns the exact dataset row for the chosen drink.

Error handling — Detects invalid selections (“This is not a drink at Starbucks”).

Modular logic — Clear separation between data loading, filtering, and user interaction.
