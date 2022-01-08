import sys
from outputMessages import *
from text import monkeyText
from art import monkeyArt

try:
    if sys.argv[1] == "-t":
        string = str(sys.argv[2])
        monkeyText(string)
    elif sys.argv[1] == "--help" or sys.argv[1] == "-help" or sys.argv[1] == "-h":
        help()
    elif sys.argv[1] == "-a":
        monkeyArt(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    else:
        error("Arguments aren't good, check help menu with --help")
except IndexError:
    error("Arguments aren't good, check help menu with --help")
except KeyboardInterrupt:
    error("Program stopped due to KeyboardInterrupt")

