import outputMessages
from random import randint
import time

def monkeyNum(numberToFind, minimalNumber, greatestNumber):
    numberIsFound = False
    count = 0
    start = time.time()
    if numberToFind < minimalNumber:
        error("<numberToFind> can't be smaller than <minimalNumber>")
    while not numberIsFound:
        if randint(minimalNumber, greatestNumber) != numberToFind:
            count += 1
        else:
            end = time.time()
            outputMessages.ok(f"Found number {numberToFind} after generating {count} pseudorandom numbers in range beetween {minimalNumber} and {greatestNumber} for {end-start} seconds")
            numberIsFound = True
