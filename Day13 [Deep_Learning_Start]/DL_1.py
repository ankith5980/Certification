# Importing necessary libraries
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# Loading the Fashion MNIST dataset
(X_train, y_train), (X_test, y_test) = keras.datasets.fashion_mnist.load_data()

# Normalizing the pixel values to be between 0 and 1
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# Reshaping the data to include a channel dimension
X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)
# -1 means "Figures out this dimension based on the other dimensions"
# 1 is the number of channels (1 for grayscale images)