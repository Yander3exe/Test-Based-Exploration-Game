import json

#read data from json file ("r" = read), "as f" can be renamed, writing data to "statsReadout"
#with only uses the file while in block and closes it afterwards, alternative to using .close
with open("PlayerStats.json", "r") as f:
    #json.load makes it readable to python by putting it into variable statsReadout
    statsReadout = json.load(f)

#read specific stat username from statsReadout
print(statsReadout["username"])

newUsername = input("What would you like the new username to be? ")

#update information outside of with block in case of error, not gonna just wipe all of the data :)
#.update best used for updating multiple items in dictionary
#statsReadout["username"] = newUsername  -  best used for singular variable
statsReadout.update({"username": newUsername})

#opening file as write (ERASES WHOLE FILE!) .update to change specific date, stats readout already exists
#so dont need to repeat dumping data back to json in format (data to dump, dumping to, indentation peramiters)
with open("PlayerStats.json", "w") as f:
    json.dump(statsReadout, f, indent=4)


with open("weapons.json", "r") as weapon_list_file:
    weapon_list = json.load(weapon_list_file)

#reading specific entry in json file, format (created index, entry, data wanted)
inventory_weapon_name=(weapon_list[1]["weapon_name"])

print(inventory_weapon_name)

#writing data into weapon variable iteratively, so weapon fuctions as the entry in the list
for weapon in weapon_list:
    if weapon["weapon_name"] == inventory_weapon_name:
        damage = weapon["base_damage"]

print(damage)

######################################
############### To Do ################
######################################

# make system for moving though areas
# create monsters data
# spawn monsters in areas
# create battle system

# learn functions
# read up on classes
# 
