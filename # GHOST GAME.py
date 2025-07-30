'''
# GHOST GAME
# A simple text-based game where the player chooses doors to find a ghost or earn points.
'''

DOOR_1 = '''
+-------------+
|   _______   |
|  |       |  |
|  |  [1]  |  |
|  |       |  |
|  |_______|  |
|             |
|             |
|             |
+-------------+
'''
DOOR_2 = '''
+-------------+
|   _______   |
|  |       |  |
|  |  [2]  |  |
|  |       |  |
|  |_______|  |
|             |
|             |
|             |
+-------------+
'''
DOOR_3 = '''
+-------------+
|   _______   |
|  |       |  |
|  |  [3]  |  |
|  |       |  |
|  |_______|  |
|             |
|             |
|             |
+-------------+
'''
Ghost_door_image = '''
+-------------+
|   _____     |
|  /     \    |
| |  ---  |   |
| |   ^   |   |
| |  '-'  |   |
|  \_____/    |
|   GHOST!    |
|             |
+-------------+
'''
Normal_image = '''
+-------------+
|             |
|   _______   |
|  |  1pt  |  |
|  |_______|  |
|             |
|   Normal    |
|             |
|             |
+-------------+
'''

Dbl_points_image = '''
+-------------+
|             |
|   _______   |
|  |  2pt  |  |
|  |_______|  |
|             |
| Double Pts! |
|             |
|             |
+-------------+
'''



import os
from random import randint
from colorama import Fore

SCORES_FILE = 'ghost_scores.txt'

def load_scores():
    if os.path.exists(SCORES_FILE):
        with open(SCORES_FILE, 'r') as f:
            scores = f.read().strip()
            if scores:
                print(Fore.YELLOW + '\nPrevious scores:')
                print(scores + Fore.RESET)
    else:
        print(Fore.YELLOW + '\nNo previous scores found.' + Fore.RESET)

def save_score(score):
    with open(SCORES_FILE, 'a') as f:
        f.write(f'{score}\n')

print('THE GHOST GAME' + Fore.GREEN)
load_scores()
Feeling_brave = None
Score = 0
while Feeling_brave == None:
    Ghost_door = randint(1,3)
    Dbl_points = randint(1,3)
    Normal = randint(1,3)
    print('There are 3 doors ahead...'+Fore.RED)
    print(Fore.RESET)
    print('6H02T'+Fore.LIGHTGREEN_EX)
    print(Fore.RESET)
    print('Hides behind one of them...')
    print('choose a door...')
    try:
        print(DOOR_1 , DOOR_2 , DOOR_3)
        choose = int(input('Choose: '))
        if choose == Ghost_door:
            print(Ghost_door_image + Fore.RED)
            Feeling_brave = False
        elif choose == Dbl_points:
            print(Dbl_points_image)
            Score += 2
            print('current score: ',Score)
        else:
            print(Normal_image)
            Score += 1
            print('current score: ',Score)
    except ValueError:
        print('Enter a valid value, 1 , 2 or 3')
    # Removed unnecessary else block after except
print('6H02T: RUN AWAY!!!'+Fore.RED)
print(Fore.RESET)
print(f'You scored {Score}')
save_score(Score)
