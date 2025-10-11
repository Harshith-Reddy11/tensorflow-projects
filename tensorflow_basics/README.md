# 🧠 TensorFlow Basics

[![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange.svg)](https://www.tensorflow.org/)

---

## 📚 Overview

This repository provides hands-on examples for learning the fundamentals of **TensorFlow**.  
It covers basic tensor operations and a simple implementation of linear regression using TensorFlow's low-level API.

---

## 📂 Project Structure

```
tensorflow_basics/
│── linear_regression_tf.py   # Linear regression using TensorFlow
│── tensor_operations.py      # Basic tensor operations (add, matmul)
│── test.py                   # Testing file
│── README.md                 # Project documentation
```

---

## 🚀 How to Run

1. **Navigate to the project folder:**
   ```sh
   cd tensorflow_basics
   ```
2. **Run the linear regression example:**
   ```sh
   python linear_regression_tf.py
   ```
3. **Run the tensor operations example:**
   ```sh
   python tensor_operations.py
   ```
4. **View the results:**
   - Console will display learned parameters for linear regression.
   - Tensor operations output will show addition and matrix multiplication results.

---

## ✅ Example Output

**Linear Regression:**

```
Learned parameters: w = 2.00, b = 1.00
```

**Tensor Operations:**

```
Tensor A:
 [[1 2]
 [3 4]]

Tensor B:
 [[5 6]
 [7 8]]

Addition Result:
 [[ 6  8]
 [10 12]]

Matrix Multiplication Result:
 [[19 22]
 [43 50]]
```

---

## 🧠 Key Learnings

- **TensorFlow** enables efficient computation with tensors and automatic differentiation.
- **Linear Regression** can be implemented from scratch using TensorFlow's gradient tape.
- **Tensor Operations** like addition and matrix multiplication are fundamental for deep learning.

---

## 💡 Pro Tip

- Experiment with different learning rates and epochs in `linear_regression_tf.py` for faster convergence.
- Try creating your own tensor operations to deepen your understanding.

---


**Happy TensorFlow Coding! 🚀**
