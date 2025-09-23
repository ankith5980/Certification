# Importing necessary libraries
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

# Loading the Fashion MNIST dataset
(X_train, y_train), (X_test, y_test) = keras.datasets.mnist.load_data()

# Normalizing the pixel values to be between 0 and 1
X_train = X_train.astype('float32') / 255.0
X_test = X_test.astype('float32') / 255.0

# Reshaping the data to include a channel dimension
X_train = X_train.reshape(-1, 28, 28, 1)
X_test = X_test.reshape(-1, 28, 28, 1)
# -1 means "Figures out this dimension based on the other dimensions"
# 1 is the number of channels (1 for grayscale images)

# Build a simple CNN Model
model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation = 'relu', input_shape=(28, 28, 1)), # Convolutional layer with 32 filters and a kernel size of 3x3
    keras.layers.MaxPooling2D((2, 2)), # Max pooling layer with a pool size of 2x2
    keras.layers.Flatten(),
    keras.layers.Dense(64, activation='relu'), # Fully connected layer with 64 neurons
    # keras.layers.Dense(128, activation='relu'), # Fully connected layer with 128 neurons
    keras.layers.Dense(10, activation='softmax') # Output layer with 10 neurons (one for each class)
])

# Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Train the model
history = model.fit(
    X_train, y_train, 
    epochs=10, 
    batch_size=64, #Faster training
    validation_data = (X_test, y_test),
    verbose=1
) # verbose=1 for progress bar

# Evaluate the model
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=0)
print('\nTest accuracy:', round(test_acc * 100, 2), '%')

# Predicting on test data
predictions = model.predict(X_test[:1]) # get prediction probabilities for first image
predicted_label = predictions.argmax() # get the index of the highest probability

plt.imshow(X_test[0].reshape(28, 28), cmap='gray')
plt.title("Prediction: " + str(predicted_label))
plt.axis('off')
plt.show()