'''
#timetables game
#This is a simple game where the user has to answer multiplication questions

'''
import random
import os
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Please enter a valid number.')

def play_game():
    print('Welcome to the timetables game!!!')
    print('We will ask a set of questions and your job is to see')
    print('how many you can answer correct in a row')
    name = input('Enter your name to start: ')
    rounds = 0
    while True:
        a = random.randint(1, 12)
        b = random.randint(1, 12)
        answer = get_int_input(f'{rounds + 1}) {a} x {b} = ')
        if answer == a * b:
            rounds += 1
            print('Correct!')
        else:
            print(f'Incorrect. The answer was {a * b}.')
            print(f'CONGRATULATIONS {name}, you lasted {rounds} rounds! Can you do better?...')
            break
    return name, rounds

def main():
    while True:
        play_game()
        again = input('Do you want to play again? (y/n): ').strip().lower()
        if again != 'y':
            print('Thanks for playing!')
            break

if __name__ == "__main__":
    main()
