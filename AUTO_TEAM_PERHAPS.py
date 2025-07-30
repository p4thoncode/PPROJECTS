'''
THE AUTO_TEAM_PERHAPS.PY FILE IS A PART OF THE AUTO TEAM PERHAPS PROJECT.
LOGS ALL JOBS AND RELATED INFORMATION BY CREATING A LOG FOLDER AND ADDING IT TO THE FOLDER.
'''
#AUTO_TEAM_PERHAPS.PY

#imports
import os
import shutil
import datetime
from datetime import datetime
from colorama import Fore

#start_up
input('Press Enter to start the Auto Team Perhaps setup...')

#all_functions
def crttime():
    print(datetime.now())

def create_log_folder():
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
    log_folder = os.path.join(desktop, 'logs')
    abs_path = os.path.abspath(log_folder)
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
        print(f'{Fore.GREEN}Log folder created successfully at: {abs_path}{Fore.RESET}')
    else:
        print(f'{Fore.YELLOW}Log folder already exists at: {abs_path}{Fore.RESET}')



def new_log():
    brand = input('Enter the brand name: ')
    model = input('Enter the model name: ')
    year = input('Enter the year of manufacture: ')
    extra_model_info = input('Enter any extra model information: ')
    plate = input('Enter the plate number: ')
    colour = input('Enter the color: ')
    fault = input('Enter the fault description: ')
    price = input('Enter the price: ')
    recdt = input('would you like to record the date? (y/n): ')
    if recdt.lower() == 'y':
        date = datetime.now().strftime('%Y-%m-%d')
    else:
        date = 'No date recorded'
    log_entry = f'---Brand: {brand}, Model: {model}, year of manufacture: {year}, Extra Model Info: {extra_model_info}, Plate: {plate}, Colour: {colour}, Fault: {fault}, Price: {price}, Date Recorded: {date}\n'
    log_file = os.path.join(os.path.expanduser('~'), 'Desktop', 'logs', 'log.txt')
    with open(log_file, 'a') as file:
        file.write(log_entry)
    print(f'{Fore.GREEN}Log entry added successfully!{Fore.RESET}')

create_log_folder()
new_log()
    