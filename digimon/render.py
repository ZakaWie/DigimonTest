import json

with open("digimon/digimons.json", mode="r") as f:
          digimons = json.load(f)

#current_digimon = digimons["kuramon_sprite"]
#print(digimons)

class color:
    default = "\033[0m"
    black = "\033[30m"
    red = "\033[31m"
    green = "\033[32m"
    yellow = "\033[93m"
    blue = "\033[34m"
    purple = "\033[35m"
    cyan = "\033[36m"
    white = "\033[37m"
    orange = "\033[33m"


def render(current_stage:int):
    match current_stage:
        case 0:
            current_digimon = digimons["kuramon_sprite"]
        case 1:
            current_digimon = digimons["Tsumemon_sprite"]
        case 2:
            current_digimon = digimons["Keramon_sprite"]
        case 3:
            current_digimon = digimons["Chrysalimon_sprite"]
    for x in range(0,16):
        for y in range(0,16):
            #if y == "x":
            #    break
            match current_digimon[x][y]:
                case "B":
                    current_digimon[x][y] = current_digimon[x][y].replace("B", color.black + "B" + color.default)

                case "R":
                    current_digimon[x][y] = current_digimon[x][y].replace("R", color.red + "R" + color.default)

                case "G":
                    current_digimon[x][y] = current_digimon[x][y].replace("G", color.green + "G" + color.default)

                case "Y":
                    current_digimon[x][y] = current_digimon[x][y].replace("Y", color.yellow + "Y" + color.default)

                case "B":
                    current_digimon[x][y] = current_digimon[x][y].replace("B", color.blue + "B" + color.default)

                case "P":
                    current_digimon[x][y] = current_digimon[x][y].replace("P", color.purple + "P" + color.default)

                case "C":
                    current_digimon[x][y] = current_digimon[x][y].replace("C", color.cyan + "C" + color.default)

                case "W":
                    current_digimon[x][y] = current_digimon[x][y].replace("W", color.white + "W" + color.default)

                case "O":
                    current_digimon[x][y] = current_digimon[x][y].replace("O", color.orange + "O" + color.default)
        
        print(" ".join(current_digimon[x]))

def clear():
    #print("this is suppose to clear the screen stupid xP")
    print("0\033[H\033[J", end="")

