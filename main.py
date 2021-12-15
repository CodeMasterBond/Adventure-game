import random
import math
import time
import os
import sys
ggs = """
   _____                           ____                 
  / ____|                         / __ \                
 | |  __  __ _ _ __ ___   ___    | |  | |_   _____ _ __ 
 | | |_ |/ _` | '_ ` _ \ / _ \   | |  | \ \ / / _ \ '__|
 | |__| | (_| | | | | | |  __/   | |__| |\ V /  __/ |   
  \_____|\__,_|_| |_| |_|\___|    \____/  \_/ \___|_|   
                                                        
                                                        
"""
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1/30)
clear = lambda: os.system('clear')

bal = 0
answer0 = input("Are you ready to play? (Y/N): ").upper()
thing = 0
while(answer0 == "N"):
  print("Let us know when you are ready...")
  answer0 = input("Are you ready to play? (Y/N)").upper()
  if (thing == 1):
    answer0 = input("Are you sure you don't want to play? (Y/N)").upper()
    if (answer0 == "N"):
      sys.exit()
    elif (answer == "Y"):
      answer0 = "Y"
clear()

slowprint('The story starts in classroom 3016, during first period "Foundations of Computer Science."')
time.sleep(1)
print()
slowprint("You had forgetten that... YOU HAVE A SUMMATIVE TODAY AND IT WILL IMPACT YOUR GRADE BY A LOT IF YOU DO BAD.")
time.sleep(1)
clear()
slowprint("First question: ")
sum = 0
print()
time.sleep(1)
num1 = input("What is the code word to make an input from the user into a decimal? ").upper()
if (num1 == "FLOAT"):
  sum += 1
print()
slowprint("Second question: ")
print()
time.sleep(1)
num2 = input("What is the statement to print something?: ").upper()
if (num2 == "PRINT"):
  sum += 1
print()
slowprint("Third question: ")
print()
time.sleep(1)
num3 = input("How do you import math?: ").upper()
if (num3 == "IMPORT MATH"):
  sum += 1
print()
print()
print("Test is over....")
time.sleep(2)
clear()
slowprint("You got {} out of 3!".format(sum))
print()
time.sleep(1)
if (sum == 3):
  slowprint("Amazing!")
  print()
  slowprint("You have earned yourself 300 CodeMaster Points. These points add on to your game score.")
  bal += 300
  time.sleep(1)
  clear()
elif (sum == 2):
  slowprint("Pretty good.")
  print()
  slowprint("You have earned yourself 200 CodeMaster Points. These points add on to your game score.")
  time.sleep(1)
  bal += 200
  clear()
else:
  slowprint("You didn't do so well, sorry. Maybe you should study instead of playing FORTNITE.")
  time.sleep(2)
  clear()
  slowprint("You walk out of the classroom and see Hank Green laugh at your terrible test score. You are embarrassed and feel furious.")
  time.sleep(1)
  print()
  choice1 = input("What will you do to Hank Green? Choices (PUNCH HIM or WALK AWAY): ").upper()
  while (not(choice1 == "PUNCH HIM" or choice1 == "WALK AWAY: ")):
    print()
    print("You did not enter a valid option response. Please try again.")
    print()
    time.sleep(1)
    choice1 = input("What will you do to Hank Green? Choices: (PUNCH HIM or WALK AWAY): ").upper()
  if (choice1 == "PUNCH HIM"):
    print()
    slowprint("You are now sent to the Dean for your disruptive actions.")
    slowprint(ggs)
    sys.exit()
  elif (choice1 == "WALK AWAY"):
    print()
    slowprint("You have chosen to ignore him.")
    print()
    time.sleep(0.5)
    slowprint("Good job for thinking and taking action with the right decision.")
    print()
    time.sleep(1)
    slowprint("You have earned yourself 100 CodeMaster Points. These points add on to your game score.")
    bal += 100
    time.sleep(2)
    clear()
slowprint("Your next class is English. You are not excited for this class.")
print()
choice2 = input("What will you do in response to your feelings? (SKIP CLASS or ATTEND CLASS): ").upper()
while(choice2 != "SKIP CLASS" and choice2 != "ATTEND CLASS"):
  print()
  print("That is not a valid answer. Please try again.")
  choice2 = input("What will you do in response to your feelings? (SKIP CLASS or ATTEND CLASS): ").upper()
if(choice2 == "SKIP CLASS"):
  print()
  slowprint("That is very wrong of you. That is a terrible decision! How could you do such a thing?!?! You are now sent to the Dean and put into trouble.")
  time.sleep(1)
  slowprint(ggs)
  sys.exit()
elif(choice2 == "ATTEND CLASS"):
  slowprint("Thank you for meeting the minimum standards of being a student under law.")
  time.sleep(1)
  print()
  slowprint("Unfortunately, that was an expected answer so you don't earn any CodeMaster points from that.")
  time.sleep(2)
clear()
slowprint("In English class, you are writing a heavily graded essay.")
print()
slowprint("Everything feels super boring to you.")
slowprint("UNTIL...")
print()
time.sleep(1)
slowprint("Suddenly a HUGE BLACK HOLE OPENS IN THE MIDDLE OF THE WALL IN THE CLASSROOM.")
time.sleep(1)
choice3 = input("YOU ARE SURPRISED THAT THIS IS ACTUALLY HAPPENING. WILL YOU TRY TO WALK INTO THIS BLACKHOLE? (Y/N): ").upper()
while(choice3 != "Y" and choice3 != "N"):
  print()
  print("That is not a valid option. Please try again.")
  print()
  choice3 = input("YOU ARE SURPRISED THAT THIS IS ACTUALLY HAPPENING. WILL YOU TRY TO WALK INTO THIS BLACKHOLE? (Y/N): ").upper()
clear()
if(choice3 == "Y"):
  print()
  slowprint("You have been hallucinating and there was no blackhole at all.")
  print()
  slowprint("That was an unwise decision of you and you have not hit your head onto the wall.")
  slowprint("You have now developed a severe concussion that has put you into the hospital emergency room.")
  time.sleep(1)
  print(ggs)
  sys.exit()
elif(choice3 == "N"):
  print()
  slowprint("You have chosen not to dangerously step into an unknown blackhole.")
  print()
  slowprint("But you have been hallucinating and there was no blackhole at all.")
  print()
  slowprint("You chose to not mistakenly bump your head into the wall like a dummy.")
  print()
  slowprint("Thank you for not being stupid. You have earned 300 CodeMaster points.")
  bal += 300
  print()
  time.sleep(2)
clear()
slowprint("English class is now over. You are now travelling to the East building for Math class.")
slowprint("You must chose the right path to get to class on time.")
time.sleep(1)
print()
choice4 = input("Which way are you going? (THROUGH INSIDE THE BUILDING or THROUGH OUTSIDE THE BUILDING) ").upper()
if(choice4 == "THROUGH INSIDE THE BUILDING"):
  time.sleep(1)
  slowprint("You have chosen to travel through inside the building.")
  slowprint("This guy comes up to you asking if you can guess a number between 1 and 5 for 1000 CodeMaster points. But if you lose, you lose the game.")
  time.sleep(1)
  minichoice1 = input("Do you choose to accept the offer? (Y/N)").upper()
  if(minichoice1 == "Y"):
    print()
    time.sleep(1) 
    slowprint("You have chosen to take this offer, you are CRAZY!!!")
    numberchoice = int(input("Choose a number between 1 and 10 (inclusive): "))
    randomint1 = random.randint(1,10)
    if(numberchoice == randomint1):
      print("CONGRATULATIONS YOU HAVE CHOSEN THE RIGHT NUMBER AND YOU HAVE WON 1000 CODEMASTER POINTS!!!")
      bal += 1000
    else:
      print("So sorry, you have not guessed the right number between 1 and 10. This results to you losing the game... sorry.")
      print(ggs)
      sys.exit()
if(choice4 == "THROUGH OUTSIDE THE BUILDING"):
  print("You have chosen to travel through outside the building.")
  print("You have forgotten that the weather happens to be extremely cold today at 30 DEGREES FAHRENHEIT AND YOU JUST REALIZED THAT YOU LEFT YOUR SWEATER IN YOUR ENGLISH CLASS.")
  minichoice2 = input("Do you chose to go back to get your sweater? (Y/N): ").upper()
  if(minichoice2 == "Y"):
    print("You have chosen to get your sweater.")
    print("After running back to your english class, you get your sweater. You are now outside and halfway to your next class when that is just the time the bell rings.")
    print("You are now marked tardy and that is definitely not good since it shows up on your report card.")
    print(ggs)
    sys.exit()
  if(minichoice2 == "N"):
    print("You have not chosen to get your sweater.")
    print("It is super duper cold and you don't have a sweater.")
    print("You have now developed stage 5 Hypothermia.")
    print(ggs)
    sys.exit()
if (bal >= 1000):
  print("Congratulations, you have over 1000 CodeMaster points! You have won!")
else:
  print("You don't have enough points to win the game, sorry." )
  minichoice3 = input("As the second person narrator, I will a flip a coin which will determine if you win or lose the game. Now, heads or tails? (HEADS or TAILS): ").upper()
HEADS = 1
TAILS = 2
randomcoin = random.randint(1,2)
if(randomcoin == minichoice3):
  print("CONGRATULATIONS, YOU HAVE WON THE GAME!!!")
  print(""""
$$\     $$\                                                                     $$$\   
\$$\   $$  |                                                                     \$$\  
 \$$\ $$  /$$$$$$\  $$\   $$\       $$\  $$\  $$\  $$$$$$\  $$$$$$$\        $$\   \$$\ 
  \$$$$  /$$  __$$\ $$ |  $$ |      $$ | $$ | $$ |$$  __$$\ $$  __$$\       \__|   $$ |
   \$$  / $$ /  $$ |$$ |  $$ |      $$ | $$ | $$ |$$ /  $$ |$$ |  $$ |             $$ |
    $$ |  $$ |  $$ |$$ |  $$ |      $$ | $$ | $$ |$$ |  $$ |$$ |  $$ |      $$\   $$  |
    $$ |  \$$$$$$  |\$$$$$$  |      \$$$$$\$$$$  |\$$$$$$  |$$ |  $$ |      \__|$$$  / 
    \__|   \______/  \______/        \_____\____/  \______/ \__|  \__|          \___/  
                                                                                       """)
if(randomcoin != minichoice3):
  print("Sorry, you have lost the game. Play again!")
  print(ggs)
  sys.exit()