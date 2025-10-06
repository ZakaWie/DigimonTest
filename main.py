"""
This is just the entry point, but yeye 
"""
from digimon import render
from digimon import game_update
from digimon import clear

is_running = False

print("Do you want to start")

answere = input()

if answere == "Yes" or "yes":
    is_running = True

clear()
stage = 0

while is_running == True:
    render(stage)
    stage = game_update(stage) 
    if stage <= -1:
        is_running = False
    clear()

print("Hope you had fun")
