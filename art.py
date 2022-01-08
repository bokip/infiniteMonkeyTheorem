import time
from random import randint
from outputMessages import *

def monkeyArt(width, height, numberOfArts):
    start = time.time()
    solved = False
    artsGenerated = 0
    for i in range(numberOfArts):
        artsGenerated += 1
        with open(f"art{artsGenerated}.ppm", "w") as art:
            art.write("P3\n")
            art.write(f"{width} {height}\n")
            art.write("255\n")
            for y in range(height):
                for x in range(width):
                    art.write(str(randint(0,255)) + " ")
                    art.write(str(randint(0,255)) + " ")
                    art.write(str(randint(0,255)) + "   ")
            ok(f"Successfully generate art number {artsGenerated}!")
    ok(f"{numberOfArts} generated successfully")

