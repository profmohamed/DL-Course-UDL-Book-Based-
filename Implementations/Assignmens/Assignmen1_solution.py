# ques 1) using numpy create an array x , that contain 20 random numbers in range +1 , -1
# and apply Relu function to X and plot the output , to show the effect of Relu activation function

import numpy as np
import matplotlib.pyplot as plt

# Generate random numbers between -1 and 1
rand = 2 * np.random.rand(20) - 1

def relu(x):
    return np.maximum(0, x)


# Apply ReLU
result = relu(rand)

# Create visualization
plt.figure(figsize=(10, 6))
plt.scatter(range(len(rand)), rand, label='Original Values', color='blue')
plt.scatter(range(len(result)), result, label='After ReLU', color='red')
plt.axhline(y=0, color='k', linestyle='--')
plt.legend()
plt.title('Effect of ReLU Activation Function')
plt.xlabel('Sample Index')
plt.ylabel('Values')
plt.grid(True)
plt.show()

