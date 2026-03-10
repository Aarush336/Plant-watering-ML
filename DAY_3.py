# Practise Question 4: Write a function called plant_status that takes two parameters — temperature and humidity. If temperature is above 39 AND humidity is below 50 print "Critical". Otherwise print "Stable".

def plant_status (temperature, humidity):
    if temperature > 39 and humidity < 50:
        return("Critical")
    else:
        return("Stable")

print(plant_status(40, 70))