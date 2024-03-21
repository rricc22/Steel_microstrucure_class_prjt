import pandas as pd
import tensorflow as tf
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
import os
from tqdm import tqdm
keras = tf.keras


dir_img = '/home/riccardo/PycharmProjects/Test1/data/Grains'
dir_mask = '/home/riccardo/PycharmProjects/Test1/data/Segmented'

list_img = sorted(os.listdir(dir_img))
list_img_path = []

for i in list_img:
    list_img_path.append(os.path.join(dir_img,i))

#len(list_img_path)

list_mask_path = []
for i in sorted(os.listdir(dir_mask)):
    list_mask_path.append(os.path.join(dir_mask,i))

list_img_load = []
list_mask_load = []

for i in tqdm(list_img_path):
    img = plt.imread(i)
    list_img_load.append(img)
    #plt.show()

for i in tqdm(list_mask_path):
    img = plt.imread(i)
    list_mask_load.append(img)

split = int(len(list_img_load)*0.75)

list_mask_load = np.array(list_mask_load)/255
list_mask_load = np.where(list_mask_load > 0.5, 1, 0)
list_img_load = np.array(list_img_load)

X_train = list_img_load[:split]
Y_train = list_mask_load[:split]
X_test = list_img_load[split:]
Y_test = list_mask_load[split:]


# def binary_accuracy_with_threshold(y_true, y_pred, threshold=0.5):
#     # Appliquer un seuil pour binariser les prédictions
#     y_pred_thresholded = tf.cast(y_pred > threshold, tf.float32)
#     # Utiliser l'accuracy binaire de Keras
#     return tf.keras.metrics.binary_accuracy(y_true, y_pred_thresholded)

# from tensorflow.keras.metrics import MeanIoU

# Nombre de classes de votre problème de segmentation. Pour une segmentation binaire, il y a 2 classes (fond et premier plan).
# num_classes = 2

# Initialiser MeanIoU avec le nombre de classes
# iou_metric = MeanIoU(num_classes=num_classes)

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same', input_shape=(300, 400, 3)),
    tf.keras.layers.Conv2D(32, (3, 3), activation='relu', padding='same'),

    tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same'),

    tf.keras.layers.Conv2D(1, (3, 3), activation='sigmoid', padding='same')
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
#model.compile(optimizer='adam',
#              loss='binary_crossentropy',
#             metrics=[lambda y_true, y_pred: binary_accuracy_with_threshold(y_true, y_pred, threshold=0.5)])

model.summary()

history = model.fit(x=X_train, y=Y_train, validation_data=(X_test,Y_test), batch_size=8, epochs=30)
history.history.keys()

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

loss = history.history['loss']
val_loss = history.history['val_loss']

epochs_range = range(30)

plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.plot(epochs_range, acc, label='accuracy')
plt.plot(epochs_range, val_acc, label='val_accuracy')
plt.legend(loc='lower right')
plt.title('Training and Validation Accuracy')

plt.subplot(1, 2, 2)
plt.plot(epochs_range, loss, label='Training Loss')
plt.plot(epochs_range, val_loss, label='Validation Loss')
plt.legend(loc='upper right')
plt.title('Training and Validation Loss')
plt.show()

model.save('test_grain3.h5')

test = model.predict(X_train[0].reshape(1,300,400,3))

plt.imshow(test.reshape(-1,400,1))
plt.show()