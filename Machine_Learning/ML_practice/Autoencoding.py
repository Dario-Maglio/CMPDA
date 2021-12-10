"""Autoencoding assignmet"""

from math import pi

import numpy as np
import matplotlib.pyplot as plt

from keras.models import Model
from keras.layers import Input, Dense
from keras.callbacks import EarlyStopping, ReduceLROnPlateau
from tensorflow.keras.utils import plot_model
from sklearn.model_selection import train_test_split as test_split

N=1000

theta = np.random.random(N)*2*pi
radius = 0.95 + np.random.random(N)*0.1


x = radius*np.cos(theta)
y = radius*np.sin(theta)

X=np.stack((x,y), axis=1)

X_train, X_test, y_train, y_test = test_split(X, X, test_size=0.5, random_state=42)

plt.figure('Data')
plt.scatter(x,y)
plt.show()

"""GAN configuration and training"""

inputs = Input(shape=(2,))
hidden = Dense(50, activation='relu')(inputs)
hidden = Dense(50, activation='relu')(hidden)
latent = Dense(1, activation='sigmoid')(hidden)
hidden = Dense(50, activation='relu')(latent)
hidden = Dense(50, activation='relu')(hidden)
outputs = Dense(2, activation='linear')(hidden)

model = Model(inputs=inputs, outputs=outputs, name='autoencoder')
model.compile(loss='MSE')
model.summary()
plot_model(model)

history = model.fit(X_train, y_train,
          validation_data=(X_test, y_test),
          epochs=1000, verbose=2,
          callbacks=[
          EarlyStopping(monitor='val_loss', patience=20, verbose=0),
          ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=10, verbose=0)
          ])

plt.figure('Training')
plt.plot(history.history["val_loss"])
plt.plot(history.history["loss"])
plt.yscale('log')
plt.show()

'''Encoder & decoder'''

encoder = Model(inputs=inputs, outputs=latent, name='encoder')
encoder.summary()
plot_model(encoder)

decoder = Model(inputs=latent, outputs=outputs, name='decoder')
decoder.summary()
plot_model(decoder)

pred = decoder.predict(np.random.random(N))
plt.figure('Prediction')
plt.scatter(pred[:,0],pred[:,1])
plt.show()
