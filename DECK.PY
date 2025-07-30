'''
deck.py
This script moves files from the source directory to the destination directory.
It uses the shutil module to handle file operations.
'''

#IMPORTS
import datetime
from datetime import datetime
from colorama import Fore
import shutil
input('Press Enter to start the deck setup...')

#start time
start_time = datetime.now()
print(f'Start time: {start_time.strftime("%H:%M:%S")}')

# defining source and destination directories
while True:
    try:
        source_directory = input('Enter the source directory path: ').strip().strip('"\'')
        destination_directory = input('Enter the destination directory path: ').strip().strip('"\'')
        if not source_directory:
            raise ValueError("Source directory cannot be empty.")
        elif not destination_directory:
            raise ValueError("Destination directory cannot be empty.")
        break
    except ValueError as e:
        print(f'Error: {e}. Please try again.')

#confirming the directories
print('You have entered the following directories:')
print(f'Source Directory: {source_directory}')
print(f'Destination Directory: {destination_directory}')

# moving files from source to destination
try:
    shutil.move(source_directory, destination_directory)
    print(f'Files moved from {source_directory} to {destination_directory} successfully.')
except Exception as e:
    print(f'An error occurred while moving files: {e}')
if __name__ == '__main__':
    input('Press Enter to exit the deck setup...') 
#end time
end_time = datetime.now()
print(f'End time: {end_time.strftime("%H:%M:%S")}')

#total time taken  
total_time = end_time - start_time
print(f'Total time taken: {total_time}')


# End of deck.py
