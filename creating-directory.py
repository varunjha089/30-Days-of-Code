"""
    Trying to create some directory at
    ~/30-Days-of-Code/
"""

import os

# path at which dir to be created
parent_dir = '~/30-Days-of-Code/'

for num in range(0, 30):
    # Initial directory name
    directory = "Day-"

    # a number is added at the last of each dir, incremented every time by 'for' loop
    directory += str(num)

    # joining directory to parent_dir
    path = os.path.join(parent_dir, directory)

    # creating the directory
    os.mkdir(path)

    # Printing the directory name
    print("directory '%s' created", directory)

print("Thanks for using the automation service")