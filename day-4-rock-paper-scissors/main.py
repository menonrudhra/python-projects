rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
options = [rock,paper,scissors]

user_option = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_option = random.randint(0,2)

if(user_option >=3 or user_option < 0):
  print("You typed an invalid number! You lose!")
else:
  print(options[user_option])

  print("Computer chose:")
  print(options[computer_option])

  if(user_option == computer_option):
    print("You both tied")
  else:
    if(user_option == 0):
      if(computer_option == 1):
        print("You lose")
      else:
        print("You win")
    elif(user_option == 1):
      if(computer_option == 0):
        print("You win")
      else:
        print("You lose")
    else:
      if(computer_option == 0):
        print("You lose")
      else:
        print("You win")
  




