import sys
from outputMessages import *
from art import monkeyBlackWhite, monkeyArt
from text import monkeyText

try:
    if sys.argv[1] == "-t":
        string = str(sys.argv[2])
        monkeyText(string)
    elif sys.argv[1] == "--help" or sys.argv[1] == "-help" or sys.argv[1] == "-h":
        help()
    elif sys.argv[1] == "-a":
        if sys.argv[5] == "-bw":
            monkeyBlackWhite(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
        else:
             monkeyArt(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    else:
        error("Arguments aren't good, check help menu with --help")
except IndexError:
    error("Arguments aren't good, check help menu with --help")
except KeyboardInterrupt:
    error("Program stopped due to KeyboardInterrupt")

