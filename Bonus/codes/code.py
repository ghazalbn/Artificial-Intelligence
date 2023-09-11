# -*- coding: utf-8 -*-
"""final_code.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oZBwoHoEgBaxBPq772ELdJd0_lLysDR0
"""

#Assinment 6
# FatemeZahra Bakhshande


import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
import random as rnd

from keras.datasets import  fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

print(train_images.shape)
print(train_labels.shape)
print(test_images.shape)
print(test_labels.shape)

plt.imshow(train_images[0], cmap='gray')
plt.title(train_labels[0])
plt.show()


np.random.seed(0)
rnd.seed(0)
tf.random.set_seed(0)

train_images = train_images / 255
test_images = test_images / 255


# Part 1

model = keras.models.Sequential(
     name='MyModel', layers=[
     keras.layers.Input(shape=(28, 28)),
     keras.layers.Flatten(),
     keras.layers.Dense(units=256, activation=keras.activations.relu),
     keras.layers.Dense(units=10, activation='softmax')
    ]
)
model.compile(
    loss=keras.losses.sparse_categorical_crossentropy,
    optimizer=keras.optimizers.SGD(learning_rate=0.001),
    metrics=['accuracy']
    )

model.summary()

result = model.fit(
          train_images,
          train_labels, 
          batch_size=256, 
          epochs=50,
          validation_data=(test_images, test_labels)
          )

history = result.history
print(history) 

plt.plot(history['loss'], label='l')
plt.plot(history['val_loss'], label='vl')
plt.title('loss')
plt.legend()
plt.show()


plt.plot(history['accuracy'], label='a')
plt.plot(history['val_accuracy'], label='va')
plt.title('accuracy')
plt.legend()
plt.show()


model.save('model/mymodel')


predicts = model.predict(test_images,)
print(predicts.shape)
my_predicts = predicts.argmax(axis=1)
print(my_predicts.shape)
(10000, 10)
(10000,)

test = test_images * 255
for i in range(0, 15):
  plt.subplot(3, 5, i + 1)
  plt.imshow(test[i], cmap='gray')
  plt.title(f'prediction: {my_predicts[i]}, true_label: {test_labels[i]}')
plt.subplots_adjust(right=2.5, top=2.3)
plt.show()


test_loss, test_accuracy = model.evaluate(test_images,  test_labels)

print('Test accuracy:', test_accuracy, ', Test loss:', test_loss)


# ----------------------------------------------------------------------------------------------------------------------------------


# Part 2
# model trainer function to use in the rest of the question


def model_trainer(hidden_units, optimizer, split, epochs=50):
  model = keras.models.Sequential(
      [
      keras.layers.Input(shape=(28, 28)),
      keras.layers.Flatten(),
      keras.layers.Dense(units=hidden_units, activation=keras.activations.relu),
      keras.layers.Dense(units=10, activation='softmax')
      ]
  )
  model.compile(
      loss=keras.losses.sparse_categorical_crossentropy,
      optimizer=optimizer,
      metrics=['accuracy']
      )
  
  print(model.summary())

  result = model.fit(
          train_images,
          train_labels, 
          batch_size=256, 
          epochs=epochs,
          validation_split=split
          )
  history = result.history

  plt.plot(history['loss'], label='l')
  plt.plot(history['val_loss'], label='vl')
  plt.title('loss')
  plt.legend()
  plt.show()

  plt.plot(history['accuracy'], label='a')
  plt.plot(history['val_accuracy'], label='va')
  plt.title('accuracy')
  plt.legend()
  plt.show()

  test_loss, test_accuracy = model.evaluate(test_images,  test_labels)
  print('Evaluation:\nTest accuracy:', test_accuracy, ', Test loss:', test_loss)

  print('\nPredict:')
  predicts = model.predict(test_images,)
  my_predicts = predicts.argmax(axis=1)

  test = test_images * 255
  plt.imshow(test[10], cmap='gray')
  plt.title(f'prediction: {my_predicts[10]}, true_label: {test_labels[10]}')
  plt.show()


# ج)
# accuracy of each number of hidden units, with validation_split = 0.2


# 1- 16 Hidden Units
model_trainer(16, keras.optimizers.SGD(learning_rate=0.001), 0.2)

# 2- 32 Hidden Units
model_trainer(32, keras.optimizers.SGD(learning_rate=0.001), 0.2)

# 3- 64 Hidden Units
model_trainer(64, keras.optimizers.SGD(learning_rate=0.001), 0.2)

# 4- 128 Hidden Units
model_trainer(128, keras.optimizers.SGD(learning_rate=0.001), 0.2)

# 5- 256 Hidden Units
model_trainer(256, keras.optimizers.SGD(learning_rate=0.001), 0.2)

# -------------------------------------------------------------------------
# د)
# Change validation split


# 1- validation split = 0.15

# 16 Hidden Units
model_trainer(16, keras.optimizers.SGD(learning_rate=0.001), 0.15)

# 32 Hidden Units
model_trainer(32, keras.optimizers.SGD(learning_rate=0.001), 0.15)

# 64 Hidden Units
model_trainer(64, keras.optimizers.SGD(learning_rate=0.001), 0.15)

# 128 Hidden Units
model_trainer(128, keras.optimizers.SGD(learning_rate=0.001), 0.15)

# 256 Hidden Units
model_trainer(256, keras.optimizers.SGD(learning_rate=0.001), 0.15)



# 2- validation split = 0.25


# 16 Hidden Units
model_trainer(16, keras.optimizers.SGD(learning_rate=0.001), 0.25)

# 32 Hidden Units
model_trainer(32, keras.optimizers.SGD(learning_rate=0.001), 0.25)

# 64 Hidden Units
model_trainer(64, keras.optimizers.SGD(learning_rate=0.001), 0.25)

# 128 Hidden Units
model_trainer(128, keras.optimizers.SGD(learning_rate=0.001), 0.25)

# 256 Hidden Units
model_trainer(256, keras.optimizers.SGD(learning_rate=0.001), 0.25)



# 3- validation split = 0.3


# 16 Hidden Units
model_trainer(16, keras.optimizers.SGD(learning_rate=0.001), 0.3)

# 32 Hidden Units
model_trainer(32, keras.optimizers.SGD(learning_rate=0.001), 0.3)

# 64 Hidden Units
model_trainer(64, keras.optimizers.SGD(learning_rate=0.001), 0.3)

# 128 Hidden Units
model_trainer(128, keras.optimizers.SGD(learning_rate=0.001), 0.3)

# 256 Hidden Units
model_trainer(256, keras.optimizers.SGD(learning_rate=0.001), 0.3)



# -------------------------------------------------------------------------
# ه)
# Change optimizer


# 1- Adam
model_trainer(256, keras.optimizers.Adam(learning_rate=0.001), 0.25)

# 2- RMSprop
model_trainer(256, keras.optimizers.RMSprop(learning_rate=0.001), 0.25)

# 3- Adagrad
model_trainer(256, keras.optimizers.Adagrad(learning_rate=0.001), 0.25)



# -------------------------------------------------------------------------
# و)
# Change learning rate



# learning rate = 0.1
model_trainer(256, keras.optimizers.Adam(learning_rate=0.1), 0.25)

# learning rate = 0.01
model_trainer(256, keras.optimizers.Adam(learning_rate=0.01), 0.25)

# learning rate = 0.001
model_trainer(256, keras.optimizers.Adam(learning_rate=0.001), 0.25)

# learning rate = 0.0001
model_trainer(256, keras.optimizers.Adam(learning_rate=0.0001), 0.25)



# -------------------------------------------------------------------------
# ز)
# Change epochs


# epochs = 10
model_trainer(256, keras.optimizers.Adam(learning_rate=0.001), 0.25, 10)


# -------------------------------------------------------------------------
# ح)
# hidden units


# 1- 16 Hidden Units
model_trainer(16, keras.optimizers.Adam(learning_rate=0.001), 0.25)

# 2- 32 Hidden Units
model_trainer(32, keras.optimizers.Adam(learning_rate=0.001), 0.25)

# 3- 64 Hidden Units
model_trainer(64, keras.optimizers.Adam(learning_rate=0.001), 0.25)

# 4- 128 Hidden Units
model_trainer(128, keras.optimizers.Adam(learning_rate=0.001), 0.25)

# 5- 256 Hidden Units
model_trainer(256, keras.optimizers.Adam(learning_rate=0.001), 0.25)

