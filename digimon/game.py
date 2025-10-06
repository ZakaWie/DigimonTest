import json
from .digimon import Digimon
from .digimon import Digicore


with open("digimon/digimons.json", mode="r") as f:
          wild_digimons = json.load(f)

wild_digimon = wild_digimons["Kuramon"]
my_digimon = Digimon


#don't forget to finish this okay
def battle():
    while my_digimon.hp >= 0 and wild_digimon[0] >= 0:
        if my_digimon.speed > wild_digimon[5]:
            dmg = my_digimon.attack - wild_digimon[2]
            wild_digimon[0] = wild_digimon[0] - dmg
            print(f"You did {dmg} dmg")
            
            dmg = wild_digimon[1] - my_digimon.defense
            my_digimon.hp = my_digimon.hp - dmg 
            print(f"you lost {dmg} Hp")
        else:
            dmg = wild_digimon[1] - my_digimon.defense
            my_digimon.hp = my_digimon.hp - dmg
            print(f"you lost {dmg} Hp")

            dmg = my_digimon.attack - wild_digimon[2]
            wild_digimon[0] = wild_digimon[0] - dmg
            print(f"you did {dmg} dmg")

#to make stats work this needs to be a funciton

def digivolv():
    my_digimon.stage = my_digimon.stage + 1
    match my_digimon.stage:
        case 1:
            new_stage = wild_digimons["Tsumemon"]

        case 2:
            new_stage = wild_digimons["Keramon"]

        case 3:
            new_stage = wild_digimons["Chrysalimon"]

    my_digimon.hp = my_digimon.hp + new_stage[0]
    my_digimon.attack = my_digimon.attack + new_stage[1]
    my_digimon.defense = my_digimon.defense + new_stage[2]
    my_digimon.special = my_digimon.special + new_stage[3]
    my_digimon.special_defense = my_digimon.special + new_stage[4]
    my_digimon.speed = my_digimon.speed + new_stage[5]
        


def game_update(stage:int):
   
    my_digimon.age = my_digimon.age + 1
    my_digimon.hunger = my_digimon.hunger - 1
    if my_digimon.hunger <= 0:
        my_digimon.happiness = my_digimon.happiness - 1

    if my_digimon.age >= 5 and my_digimon.happiness >= 5 and my_digimon.stage == 0:
        digivolv()
    if my_digimon.age >= 15 and my_digimon.happiness >=5 and my_digimon.stage == 1:
        digivolv()
    if my_digimon.age >= 25 and my_digimon.happiness >=5 and my_digimon.stage == 2:
        digivolv()

    print("Stage")
    print(my_digimon.stage)
    
    print("Age")
    print(my_digimon.age)

    print("Hp")
    print(my_digimon.hp)

    print("Pet, Feed, Care")

    if my_digimon == Digimon:
        print("Stats, Battle")

    player_choice = input()

    match player_choice:
        case "pet"|"Pet":
            my_digimon.happiness = my_digimon.happiness + 3

        case "feed" | "Feed":
            my_digimon.hunger = my_digimon.hunger + 3

        case "care" | "Care":
            my_digimon.hp = my_digimon.hp + 1
        
        case "Leave"|"leave": 
            return -1

        case "Stats"|"stats":
            print(f"Attack {my_digimon.attack}\n Defense {my_digimon.defense}\n Special {my_digimon.special}\n Special Defense {my_digimon.special_defense}\n Speed {my_digimon.speed}")
            scrap = input()

        case "Battle"|"battle":
            print("Let the battle begin")
            battle()
            scrap = input()
        
        case _:
            print("you chose to do nothing") 
    stage = my_digimon.stage

    if my_digimon.hp <= 0:
        print("You died T-T")
        scrap = input()
        return -1
    return stage 
