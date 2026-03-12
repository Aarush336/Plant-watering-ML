# Add a new column called needs_water to the same DataFrame. It should say “Yes” if days since last watered is above 3 AND soil moisture is below 40. Otherwise “No”. Print the full table with the new column.
import numpy as np
import pandas as pd

Data_frame = {
"name" : ["Cactus", "Dandelion", "Daisy", "Sunflower"],

"soil_moisture" :[ 20, 50, 30, 60],

"last_watered" : [10, 2, 7, 1],
}
df = pd. DataFrame(Data_frame)
df["needs_water"] = np.where((df["last_watered"] > 3) & (df["soil_moisture"] <40), "yes", "no")

print(df)

