from mnist import MNIST
from keras import layers, models
from keras.utils.np_utils import to_categorical
import numpy as np

mndata = MNIST("mnist")

X_train, y_train = mndata.load_training()
X_test, y_test = mndata.load_testing()


#Data Scaling
X_train = np.array(X_train)/255.0
y_train = np.array(y_train)

X_test = np.array(X_test)/255.0
y_test = np.array(y_test)

y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

model = models.Sequential()
model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(64, activation="relu"))

model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(64, activation="relu"))

model.add(layers.Dense(10, activation="softmax"))
model.compile(optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"])

model.fit(X_train, y_train, batch_size=32, validation_split=0.1, epochs=25, verbose=1)
result = model.evaluate(X_test, y_test)

print("Testing loss = ", result[0])
print("Testing accuracy = ", result[1])

