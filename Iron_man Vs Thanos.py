# 💕Anubhav # Dracula This is Stone, Paper, Scissors game for project purpose.......Enjoy :)

                          #First we will define some ASCII art hand gestures you can take them from any third party website
import random

Rock = '''

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
Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
Tony = '''.
░░░░░░░██████████████████░░░░░░░
░░░░████▓▓▓█▓▓▓▓▓▓▓▓█▓▓▓███░░░░░
░░░██▓▓█▓▓▓█▓▓▓▓▓▓▓▓█▓▓▓█▓▓█░░░░
░░██████████▓▓▓▓▓▓▓▓██████████░░
░░██──────███████████───────██░░
░███───────██▓▓▓▓▓▓█────────███░
░████───────█▓▓▓▓▓▓█───────████░
░█▓██───────█▓▓▓▓▓▓█───────██▓█░
░██▓█───────█▓▓▓▓▓▓█───────█▓██░
████▓█──────█▓▓▓▓▓▓█──────█▓████
█▓██▓█──────▀██████▀──────█▓██▓█
█▓██▓█────────────────────█▓██▓█
█▓████────────────────────████▓█
█▓██▀──────────────────────▀██▓█
█▓██──█▀▀▀▀▄▄──────▄▄▀▀▀▀█──██▓█
███───█─────▀██▄▄██▀─────█───███
░██───▀█▄▄▄▄█▀────▀█▄▄▄▄█▀───██░
░███────────────────────────███░
░░█▓█──────────────────────█▓█░░
░░█▓▓█────────────────────█▓▓█░░
░░█▓▓▓█──────────────────█▓▓▓█░░
░░█▓▓▓█──────────────────█▓▓▓█░░
░░█▓▓▓▓█▄──────────────▄█▓▓▓▓█░░
░░░█▓▓█▀█──▄▀▀▀▀▀▀▀▀▄──█▀█▓▓█░░░
░░░░█▓█─▀▄▄▀────────▀▄▄▀─█▓█░░░░
░░░░░█▓█─────▄▄▄▄▄▄─────█▓█░░░░░
░░░░░░█▓█▄▄▄██▓▓▓▓██▄▄▄█▓█░░░░░░
░░░░░░░█▓▓▓█▓▓▓▓▓▓▓▓█▓▓▓█░░░░░░░
░░░░░░░░████████████████░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
████████████████████████████████
█░░░░█░░░░░░░██░░░░░░░█░░████░░█
█░░░░█░░██░░░██░░░██░░█░░░███░░█
██░░██░░░░░░███░░░██░░█░░░░░█░░█
██░░██░░██░░░██░░░██░░█░░█░░█░░█
█░░░░█░░███░░██░░░██░░█░░██░░░░█
█░░░░█░░███░░██░░░░░░░█░░███░░░█
████████████████████████████████
████████████████████████████████
██░░░█████░░░█░░░░░░██░░████░░██
██░░░░███░░░░█░░██░░██░░░███░░██
██░░█░░█░░█░░█░░░░░░██░░░░░█░░██
██░░██░░░██░░█░░██░░██░░██░░░░██
██░░███████░░█░░██░░██░░███░░░██
████████████████████████████████
'''
Tony2 = ''''''
images = [Rock, paper, Scissors, Tony]
                                       #It's time to apply some logic bhaiyaa!

                          #take users input
print(images[3])
Iron_man_choice = int(input("Hello sir I'm Zarvis, which weapon you want to deploy? Type 0 for Rock, 1 for paper or 2 for Scissors.\n"))
print(images[Iron_man_choice])
Thanos_choice = random.randint(0,2)
print("Thanos have :")
print(images[Thanos_choice])
if Iron_man_choice>= 3 or Iron_man_choice<0:
    print("Wrong weapon Tony, You lose")
elif Iron_man_choice ==0 and Thanos_choice == 2:
    print("Well done Tony, you won !")
elif Thanos_choice > Iron_man_choice:
    print("Ahh! Thanos won")
elif Iron_man_choice > Thanos_choice:
    print("Yupps! you won")
elif Thanos_choice == Iron_man_choice:
    print("Intresting it's a draw")
elif Iron_man_choice == 0 and Thanos_choice == 2:
    print("You lose Tony :(")



