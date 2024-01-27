import numpy as np

# Creating the random vector of size 20 with floats in the range 1-20
random_vector = np.random.uniform(1, 20, 20)

# Reshaping the array to 4 by 5
reshaped_array = random_vector.reshape(4, 5)

# Replacing the max in each row by 0 (axis=1)
reshaped_array[np.arange(len(reshaped_array)), reshaped_array.argmax(axis=1)] = 0

print("Random Vector:")
print(random_vector)
print("\nReshaped Array:")
print(reshaped_array)