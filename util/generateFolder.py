import os
import sys
from pathlib import Path

# Generates the folder structure I have been using for DCP problems.
def genFolder(args):
    # Arg 0 is the command, 1 is the first command line arg, etc.
    num = args[1]
    folderName = "Problem" + num
    os.mkdir(folderName)
    print("Directory " , folderName ,  " Created ")
    Path(folderName + '/ProblemStatement.txt').touch()
    Path(folderName + '/solution.py').touch()

if (len(sys.argv) != 2):
    print("Usage: `python generateFolder.py 5`. This example would generate the folder/file structure for problem 5.")
else:
    genFolder(sys.argv)