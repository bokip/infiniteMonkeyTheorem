import sys
from outputMessages import *
from art import monkeyBlackWhite, monkeyArt, monkeyA
from text import monkeyText
from number import monkeyNum

try:
    if sys.argv[1] == "-t":
        string = str(sys.argv[2])
        monkeyText(string)
    elif sys.argv[1] == "--help" or sys.argv[1] == "-help" or sys.argv[1] == "-h":
        help()
    elif sys.argv[1] == "-a":
        try:
            if sys.argv[5] == "-bw":
                monkeyBlackWhite(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
            elif sys.argv[5] == "-ab":
                monkeyA(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
        except IndexError:
             monkeyArt(int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]))
    elif sys.argv[1] == "-n":
        monkeyNum(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        error("Arguments aren't good, check help menu with --help")
except IndexError:
    error("Arguments aren't good, check help menu with --help")
except KeyboardInterrupt:
    error("Program stopped due to KeyboardInterrupt")

