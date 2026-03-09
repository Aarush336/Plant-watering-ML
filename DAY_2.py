def check_water(plants):
    if plants ["temperature"] > 39:
        return("Needs water")
    else:
        return("Normal")
plants = [
    {"name": "Cactus", "temperature": 38, "water_needed": False},
    {"name": "Rose", "temperature": 42, "water_needed": True},
    {"name": "Sunflower", "temperature": 35, "water_needed": False}
]
for breed in plants:
    print(breed["name"] , breed["temperature"], check_water(breed))