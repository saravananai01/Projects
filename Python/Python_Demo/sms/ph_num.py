import tensorflow as tf
import tensorflow_addons as tfa
train,test = tf.keras.datasets.mnist.load_data()
x_train, y_train = train
x_train = x_train[..., tf.newaxis] / 255.0

# TFA layers and activations
model = tf.keras.Sequential([
  tf.keras.layers.Conv2D(filters=10, kernel_size=(3,3),
                         activation=tfa.activations.gelu),
  tfa.layers.GroupNormalization(groups=5, axis=3),
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(10, activation='softmax')
])

# TFA optimizers, losses and metrics
model.compile(
    optimizer=tfa.optimizers.RectifiedAdam(0.001),
    loss=tfa.losses.TripletSemiHardLoss(),
    metrics=[tfa.metrics.MultiLabelConfusionMatrix(num_classes=10)])

history = model.fit(x_train, y_train, epochs=10)