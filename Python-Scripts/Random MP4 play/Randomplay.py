# For the listdir and Startfile in Win32
import os

# For randomly selecting one file from the list
import random

# For the regular expression of filetype matching
import re

# For executing the file on GNU/Linux Systems
import subprocess, sys

# Finds the absolute path of the current directory
path = os.path.dirname(os.path.abspath(__file__))

# List of all the files in said directory, which in our case is the current dir
files = (os.listdir(path))

# Instantiates empty list for storing Mp4s
mp4s = []

# Iterating in the list of files
for fil in files:
    # We use Regex to match the file names to of '*.mp4'. Gives a Bool output.
    x = re.match(".*?\.mp4", fil)
    
    # If X is true, then Print that it is true, and add it to the mp4s list
    if x:
        print(f"{fil} is an mp4")
        mp4s.append(fil)
    
    # If not, then just print that it is not a .mp4
    else:
        print(f"{fil} not an mp4")

# If there is more than one file in mp4, 
if len(mp4s) > 0:

    # Choose a random video
    current_video = random.choice(mp4s)
    # If the user platform is GNU/Linux, then steps for execute.
    # https://stackoverflow.com/questions/29823028/attributeerror-module-object-has-no-attribute-startfile 
    if sys.platform.startswith('linux'):
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, current_video])
    elif sys.platform.startswith('win32'):
        os.startfile(current_video)
    else:
        print(f"{sys.platform} not currently supported")
else:
    print(f"\n {path} does not contain any .mp4 files")