import random
import time

class Weapon:

    def __init__(self, name, type, base_dmg, crit_chance, crit_bonus):
        self.name = name
        self.base_dmg = base_dmg
        self.crit_chance = crit_chance
        self.crit_bonus = crit_bonus

    def crit(self):
        return self.base_dmg * self.crit_bonus

    def attack_dmg(self):
        if random.randint(0,100) <= self.crit_chance:
            return self.crit()
        else:
            return self.base_dmg

The_Throngler = Weapon("The Throngler", "Sword", 69, 50, 2)
Rusty_Spoon = Weapon("Rusty Spoon", "Special", 10000, 100, 2)

print("You have found a weapon!")
eqpd_wpn = Rusty_Spoon
time.sleep(1)
print(f"You have recieved {eqpd_wpn.name} \nDamage: {eqpd_wpn.base_dmg} \nCrit Chance: {eqpd_wpn.crit_chance} \nCrit Bonus: {eqpd_wpn.crit_bonus}")
time.sleep(1)
print(eqpd_wpn.base_dmg)

while True:
    input()
    print(eqpd_wpn.attack_dmg())








