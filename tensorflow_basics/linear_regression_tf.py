import tensorflow as tf

# Given data
X = tf.constant([1.0, 2.0, 3.0, 4.0])
Y = tf.constant([3.0, 5.0, 7.0, 9.0])

# Variables (weights & bias)
w = tf.Variable(0.0)
b = tf.Variable(0.0)

# Learning rate
lr = 0.01

# Training loop
for epoch in range(1000):
    with tf.GradientTape() as tape:
        y_pred = w * X + b
        loss = tf.reduce_mean(tf.square(Y - y_pred))  # MSE

    # Compute gradients
    grads = tape.gradient(loss, [w, b])
    w.assign_sub(lr * grads[0])
    b.assign_sub(lr * grads[1])

print(f"\nLearned parameters: w = {w.numpy():.2f}, b = {b.numpy():.2f}")
