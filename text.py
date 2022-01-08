import time
from sys import stdout
from random import randint, choice
from outputMessages import *
characters = "abcdefghijklmnopqrstuvwxyz "
charactersNoSpace = "abcdefghijklmnopqrstuvwxyz"

def testString(stringToTest):
    if stringToTest == "":
        error("String for monkey to find can't be empty")
    for i in stringToTest:
        if i not in characters:
            error("Invalid character found, allowed characters are \"abcdefghijklmnopqrstuvwxyz \"")
def monkeyText(stringToFind):
    start = time.time()
    solved = False
    millionsNeededToFind = 0
    testString(stringToFind)
    ok("No illegal characters found")
    if " " in stringToFind:
        info("Since you have spaces in your string, they will be generated!")
        warning("String with spaces might take a long time to find!")
        while not solved:
            if millionsNeededToFind != 0:
                info("Starting with another one...")
            string = ''.join([choice(characters) for i in range(1000000)])
            if stringToFind not in string:
                info(f"Million characters(that is {millionsNeededToFind}th million) searched and your string is not found in there!")
                millionsNeededToFind += 1
            else:
                end = time.time()
                ok(f"found your string({stringToFind}) after {millionsNeededToFind} millions of characters in {end - start} seconds!")
                solved = True
    else:
        info("Since you don't have spaces in your string, they wouldn't be generated!")
        while not solved:
            if millionsNeededToFind != 0:
                info("Starting with another one...")
            string = ''.join([choice(charactersNoSpace) for i in range(1000000)])
            millionsNeededToFind += 1
            if stringToFind not in string:
                info(f"Million characters(that is {millionsNeededToFind}th million) searched and your string is not found in there!")
            else:
                end = time.time()
                ok(f"found your string({stringToFind}) after {millionsNeededToFind} millions of characters in {end - start} seconds!")
                solved = True
    print("""     
           ."`".
       .-./ _=_ \.-.
      {  (,(oYo),) }}
      {{ |   "   |} }
      { { \(---)/  }}
      {{  }'-=-'{ } }
      { { }._:_.{  }}
      {{  } -:- { } }
      {_{ }`===`{  _}
     ((((\)     (/))))""")
    print("""
                        .=\"=.
                      _/.-.-.\_     _
                     ( ( o o ) )    ))
                      |/  \"  \|    //
      .-------.        \'---'/    //
     _|~~ ~~  |_       /`\"\"\"`\\  ((
   =(_|_______|_)=    / /_,_\ \\  \\
     |:::::::::|      \_\\_'__/ \  ))
     |:::::::[]|       /`  /`~\  |//
     |o=======.|      /   /    \  /
     `\"\"\"\"\"\"\"\"\"`  ,--`,--'\/\    /
                   '-- \"--'  '--'
     """)