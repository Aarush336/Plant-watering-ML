# Introduction to Panda's
import pandas as pd
import numpy as np

data = {
    "plant": ["Cactus", "Rose", "Sunflower", "Tulip"],
    "temperature": [41, 42, 35, 41],
    "humidity": [30, 65, 55, 60],
    "water_needed": [False, True, False, True]
}

df = pd.DataFrame(data)
df["status"] = np.where((df["temperature"] > 39) & (df["humidity"] < 50), "Critical", "Stable")
print(df)