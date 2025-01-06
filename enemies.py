

enemies = {
    "Goblin": {
         "AC": 12, # Armour Class
         "HP": 15, # Hit Points
         "Attack": [1,6] # Damage range for attacks (1d6)
    },
    "Skeleton": {
        "AC": 10, # Armour Class
         "HP": 20, # Hit Points
         "Attack": [1,8] # Damage range for attacks (1d8)
    },
    "Orc": {
        "AC": 14, # Armour Class
        "HP": 35, # Hit Points
        "Attack": [2,10] # Damage range for attacks (1d10)
    }
}
#print(enemies["Goblin"])
#goblin_stats = enemies["Goblin"]
#for stat, value in goblin_stats.items():
#    print(f"Goblin's {stat}: {value}")