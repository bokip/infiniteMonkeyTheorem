from random import randint
from outputMessages import *
from os import mkdir, path

def monkeyArt(width, height, numberOfArts):
    artsGenerated = 0
    if path.isdir("arts"):
        info("Direcotry \"arts\" alredy exists")
    else:
        mkdir("arts")
        info("Created directory \"arts\"")
    for i in range(numberOfArts):
        artsGenerated += 1
        with open(f"arts/art{artsGenerated}.ppm", "w") as art:
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

def monkeyBlackWhite(width, height, numberOfArts):
    artsGenerated = 0
    if path.isdir("arts"):
        info("Direcotry \"arts\" alredy exists")
    else:
        mkdir("arts")
        info("Created directory \"arts\"")
    for i in range(numberOfArts):
        artsGenerated += 1
        with open(f"arts/art{artsGenerated}.ppm", "w") as art:
            art.write("P3\n")
            art.write(f"{width} {height}\n")
            art.write("255\n")
            for y in range(height):
                for x in range(width):
                    if randint(0,1) == 0:
                        art.write("255 ")
                        art.write("255 ")
                        art.write("255   ")
                    else:
                        art.write("0 ")
                        art.write("0 ")
                        art.write("0   ")
            ok(f"Successfully generate art number {artsGenerated}!")
    ok(f"{numberOfArts} generated successfully")

def monkeyA(width, height, numberOfArts):
    artsGenerated = 0
    if path.isdir("arts"):
        info("Direcotry \"arts\" alredy exists")
    else:
        mkdir("arts")
        info("Created directory \"arts\"")
    for i in range(numberOfArts):
        artsGenerated += 1
        with open(f"arts/art{artsGenerated}.ppm", "w") as art:
            art.write("P3\n")
            art.write(f"{width} {height}\n")
            art.write("255\n")
            for y in range(height):
                for x in range(width):
                    if randint(0,1) == 0:
                        art.write("255 ")
                        art.write("255 ")
                        art.write("255   ")
                    else:
                        random = randint(1,5)
                        if random == 1:
                            art.write("255 ")
                            art.write("0 ")
                            art.write("0   ")
                        if random == 2:
                            art.write("0 ")
                            art.write("255 ")
                            art.write("0   ")
                        if random == 3:
                            art.write("0 ")
                            art.write("0 ")
                            art.write("255   ")
                        if random == 4 or random == 5:
                            art.write("0 ")
                            art.write("0 ")
                            art.write("0   ")
            ok(f"Successfully generate art number {artsGenerated}!")
    ok(f"{numberOfArts} generated successfully")
