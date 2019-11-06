import random
import numpy as np
import json
import time

def Save(dictionary):        #stores the data into the file
  saves = open('highscores.json', 'a')
  saves.write(str(save))
  saves.close()

alert = '\a' + '\a' + '\a' + '\a' + '\a' + '\a' + '\a' #creates an alert sound for input
space = '\t'
save = {} #used to store name and money values
money = 0

print('Welcome to the life simulator' + space + alert) #short welcome :)

time.sleep(3.5)
name = input('Please enter your name: ' + space + alert)

time.sleep(1.5)
print(name, 'you currently have: ', money, 'dollars' + alert)

again = 'y'

while again == 'y' or again == 'yes':
  action = input('What would you like to do (work, rest, shop, tv):' + ' ')
  if action == 'work':
    job = [
      'You work as a stripper',
      'You work as a cashier',
      'You work as a car washer',
      'You work as a valet',
      'You work as a mail carrier',
      'You work as a bank teller',
      'You work as a tailor',
      'You work as a waiter',
      'You work as a delivery driver',
      'You work as a writer'
   ]
    pay = [100, 25, 15, 65, 55, 10, 95, 86, 250, 500, 30, 70, 5, 29, 316, 401, 493, 275, 295, 1]

    time.sleep(3.5)
    print(random.choice(job))
    money = money + random.choice(pay)
    time.sleep(3.5)
    print('You now have: ', money, 'dollars.' + alert)
    save.update({name: money})
  elif action == 'rest':
    event = [
      'a cat died outside',
      'there was an accident in your neighborhood',
      'you wet the bed',
      'the new Drake album dropped',
      'R Kelly went to jail',
      'Bill Cosby got out of jail',
      'the purge happened',
      'an unknown person sat next to you',
      'literally nothing happened',
      'the grim reaper looked for you',
    ]

    reaper = [
      "You",
      "Your best friend",
      "One of your family members",
      "One of your coworkers",
      "One of your classmates",
      "One of your neighbors",
      'the grim reaper paid you a visit'
    ]
    outcome = random.choice(event)
    outcome2 = random.choice(reaper)

    time.sleep(1.5)
    print('You feel well rested, ', outcome, 'while you slept' + alert)
    
    if outcome == 'the grim reaper looked for you':
      print("You narrowly escaped death..." + alert)
      print("This time." + alert)
    elif outcome == 'the grim reaper paid you a visit':
      time.sleep(2.2)
      print("Uh oh, what happened?" + alert)
      time.sleep(3.5)
      print(outcome2, "died, you go into mourning" + alert)
      if outcome2 == "You":
        print("Your final score is: " + alert)
        time.sleep(1.2)
        print(save)
        break 
  elif action == 'shop':
    items = [
      'skateboard',
      'console',
      'katana',
      'gun',
      'dog',
      'hat',
      'food',
      'alcohol',
      'hooker',
      'uumu',
      'leopleuredon',
      'stock in google',
      'stock in apple'
    ] 

    item = []
    item.append(random.choice(items))
    cost = [100, 25, 650, 1000, 20, 10, 560, 450, 3, 365, 32, 75, 850, 56, 85, 970, 120, 320, 12, 1]
    money = money - random.choice(cost)
    print('You now own: ', item + alert)
    
    time.sleep(2)
    print('You now have: ', money, 'dollars' + alert)
    save.update({name: money})
  elif action == 'tv':
    shows = [
      'Fairy Tale',
      'Bukake',
      'Seven Deadly Sins',
      '13 reasons why',
      'Lucifer',
      'Porn',
      'The Kennedy Assassination',
      'tentacle hentai',
      'Game Theory',
      'Mia Khalifa playing Slap City',
      'Boondocks',
      'your mom have sex',
      'Adhesive Medical Strips',
      "Dad jokes",
      'Hoes Mad, music video',
      'Pokemon speedruns',
      "Jojo's Bizarre adventure",
      'Friends',
      'How to get away with Murder',
      'memes',
      'Persona 5',
      'Rise of the Shield Hero',
      'Dokappon kingdom',
      'Savage spikes in Smash Bros',
      'Anal',
      'Salty Runbacks',
      'One punch man',
      'Dedede taunts',
      'Deez nuts'
    ]

    watched = random.choice(shows)

    print('You watched: ', watched, "on tv." )
    print('Hah' + alert)
  else:
    print("Please try again. " + alert)
  again = input('Would you like to keep going? (y/n)' + alert)

print("Your final score is: " + alert)
time.sleep(1.2)
print(save)

Save(save)
