# Practise Question 3: Create a list of humidity readings: [55, 70, 80, 45, 90, 60, 75]. Loop through them and print "High humidity" if above 70, "Normal" if 70 or below.
humidity_readings = [55, 70, 80, 45, 90, 60, 75]
for hum in humidity_readings:
    if hum > 70:
        print("High Humidity")
    else:
        print("Normal")
