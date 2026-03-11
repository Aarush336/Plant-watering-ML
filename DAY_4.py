# Practise Question 1: Create a numpy array of soil moisture readings: [23, 45, 12, 67, 34, 89, 56]. Print the mean, max, and min. Then print only readings above 50.
import numpy as np

moisture = np.array([23, 45, 12, 67, 34, 89, 56])
print(moisture.mean())
print(max(moisture))
print(min(moisture))
print(moisture[moisture > 50])