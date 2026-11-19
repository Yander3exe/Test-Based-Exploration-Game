import random
import time
import json

class Player:

    def __init__(self, username, max_hp, current_hp, lvl, exp, strength, magica, agility, wisdom, stealth, hunger):
        self.username = username
        self.max_hp = max_hp
        self.current_hp = current_hp
        self.lvl = lvl
        self.exp = exp
        self.strength = strength
        self.magica = magica
        self.agility = agility
        self.wisdom = wisdom
        self.stealth = stealth
        self.hunger = hunger

    def hunger_down(self):
        self.hunger -= 1

    def damage_player(self, damage_taken):
        self.current_hp -= damage_taken

def create_new_player():
    with open("PlayerStats.json", "r") as f:
        default_stat = json.load(f)
        new_player_name = input("Please Choose a name: ")
        new_player = Player(new_player_name, default_stat["max_hp"], default_stat["current_hp"], default_stat["lvl"], default_stat["exp"], default_stat["strength"], default_stat["magica"], default_stat["agility"], default_stat["wisdom"], default_stat["stealth"], default_stat["hunger"])
        return new_player

created_player = create_new_player()

print(created_player.username)
print(created_player.current_hp)










#test_player = Player("Test", 100, 100, 1, 1, 1, 1, 1, 1, 1, 10)

#print(test_player.username)
#print(test_player.current_hp)
#damage = int (input())
#test_player.damage_player(damage)
#print(test_player.current_hp)
