import sys
from outputMessages import *
from text import monkeyText
try:
    if sys.argv[1] == "-t":
        string = str(sys.argv[2])
        monkeyText(string)
    elif sys.argv[1] == "--help" or sys.argv[1] == "-help" or sys.argv[1] == "-h":
        help()
except IndexError:
    error("Arguments aren't good, check help menu with --help")
except KeyboardInterrupt:
    error("Program stopped due to KeyboardInterrupt")