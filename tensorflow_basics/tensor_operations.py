import tensorflow as tf

# Step 1: Check version
print("TensorFlow version:", tf.__version__)

# Step 2: Create tensors
a = tf.constant([[1, 2], [3, 4]])
b = tf.constant([[5, 6], [7, 8]])

# Step 3: Perform tensor operations
sum_result = tf.add(a, b)
mul_result = tf.matmul(a, b)

print("\nTensor A:\n", a.numpy())
print("\nTensor B:\n", b.numpy())
print("\nAddition Result:\n", sum_result.numpy())
print("\nMatrix Multiplication Result:\n", mul_result.numpy())
