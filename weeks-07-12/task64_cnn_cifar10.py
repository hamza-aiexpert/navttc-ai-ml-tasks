"""Task 64 - CNN on the CIFAR-10 dataset (TensorFlow / Keras).
Requires: pip install tensorflow matplotlib   (internet needed once to download CIFAR-10)
Run:      python task64_cnn_cifar10.py
Expected: ~75-80% test accuracy in 15 epochs (higher with the augmentation below)."""
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.metrics import classification_report, ConfusionMatrixDisplay

classes = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
y_train, y_test = y_train.ravel(), y_test.ravel()

model = models.Sequential([
    layers.Input(shape=(32, 32, 3)),
    layers.RandomFlip("horizontal"), layers.RandomTranslation(0.1, 0.1),   # data augmentation
    layers.Conv2D(32, 3, padding="same", activation="relu"), layers.BatchNormalization(),
    layers.Conv2D(32, 3, padding="same", activation="relu"), layers.MaxPooling2D(), layers.Dropout(0.25),
    layers.Conv2D(64, 3, padding="same", activation="relu"), layers.BatchNormalization(),
    layers.Conv2D(64, 3, padding="same", activation="relu"), layers.MaxPooling2D(), layers.Dropout(0.25),
    layers.Conv2D(128, 3, padding="same", activation="relu"), layers.BatchNormalization(),
    layers.MaxPooling2D(), layers.Dropout(0.3),
    layers.Flatten(), layers.Dense(128, activation="relu"), layers.Dropout(0.4),
    layers.Dense(10, activation="softmax"),
])
model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
model.summary()

history = model.fit(x_train, y_train, epochs=15, batch_size=64, validation_split=0.1)
test_loss, test_acc = model.evaluate(x_test, y_test, verbose=0)
print(f"\nTest accuracy: {test_acc:.4f}")

pred = model.predict(x_test).argmax(1)
print(classification_report(y_test, pred, target_names=classes))

fig, ax = plt.subplots(1, 3, figsize=(17, 4.5))
ax[0].plot(history.history["accuracy"], label="train"); ax[0].plot(history.history["val_accuracy"], label="val")
ax[0].set_title("Accuracy"); ax[0].legend()
ax[1].plot(history.history["loss"], label="train"); ax[1].plot(history.history["val_loss"], label="val")
ax[1].set_title("Loss"); ax[1].legend()
ConfusionMatrixDisplay.from_predictions(y_test, pred, display_labels=classes, ax=ax[2],
                                        xticks_rotation=90, colorbar=False)
plt.tight_layout(); plt.savefig("outputs/task64_cifar10_results.png", dpi=120)
model.save("outputs/cifar10_cnn.keras")
