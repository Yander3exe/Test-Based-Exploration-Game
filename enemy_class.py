from enum import Enum, Flag, auto
import time
import random
import gc

#setting an empty list of enemies for each new enemy to be added into
enemy_list = []

class Enemy:

    #create enemy class and add it to list
    def __init__(self, name, max_hp, current_hp, strength, magica, agility, wisdom, stealth, availible_spawns, spawn_chance):
        self.name = name
        self.max_hp = max_hp
        self.strength = strength
        self.magica = magica
        self.agility = agility
        self.wisdom = wisdom
        self.stealth = stealth
        self.availible_spawns = availible_spawns
        self.spawn_chance = spawn_chance
        enemy_list.append(self)

    def spawns_in(self, location):
        self.availible_spawns.append(location)

class Area:

    #create area class
    def __init__(self, name, paths, area_type,spawnable_enemies, loot, discovered_location, dangerous):
        self.name = name
        self.paths = paths
        self.area_type = area_type
        self.spawnable_enemies = spawnable_enemies
        self.loot = loot
        self.discovered_location = discovered_location
        self.dangerous = dangerous

    #function for adding paths onto existing area
    def leads_to(self, new_path):
        self.paths.extend(new_path)

    #shows the availible paths by itterating through list
    def available_routes(self):
        for route in self.paths:
            print(f"{self.paths.index(route)+1}: {route.name}")

    #clears spawn table then generates new list by itterating through enemy_list
    def generate_enemy_spawn_table(self):
        self.spawnable_enemies.clear()
        for enemy in enemy_list:
            if self.area_type in enemy.availible_spawns:
                self.spawnable_enemies.append(enemy)

    #selects random enemy from spawnable_enemies list
    def spawn_enemy(self):
        if len(self.spawnable_enemies) > 0:
            spawned_enemy = random.choice(self.spawnable_enemies)
            print(spawned_enemy.name)

    #displays location name and sets location to discovered
    def area_discovered(self):
        print(f"Location Discovered! {self.name}")
        self.discovered_location = True


    def enter_area(self):
        if self.discovered_location == False:
            self.area_discovered()
        if self.dangerous:
            self.generate_enemy_spawn_table()
            self.spawn_enemy()
        self.available_routes()


## Area class instance creation ##

woods = Area("The Woods", [], "woods", [], [], False, True)
clearing = Area("The Clearing", [], "field", [], [], False, True)
gravel_road = Area("Gravel Road", [], "road", [], [], False, True)

## Area instance route creation ##

woods.leads_to([clearing, gravel_road])
clearing.leads_to([woods])
gravel_road.leads_to([woods])


goblin = Enemy("Goblin", 100, 100, 1, 1, 1, 1, 1, ["woods"], 2)

class Goblin(Enum):
    goblin_underling = Enemy("Goblin Underling", 30, 100, 1, 0, 1, 0, 1, ["woods"], 2)
    goblin_fighter = Enemy("Goblin Fighter", 50, 50, 2, 0, 2, 1, 2, ["woods"], 2)

wolf = Enemy("Wolf", 100, 100, 1, 1, 1, 1, 1, ["woods"], 2)

woods.enter_area()




