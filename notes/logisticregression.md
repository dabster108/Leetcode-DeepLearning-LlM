# Logistic Regression

**Logistic Regression** is a statistical method used for **binary classification** — predicting one of two possible outcomes based on input features. Despite its name, it is a **classification** algorithm, not a regression algorithm.

---

## 🔍 Key Concepts

- **Purpose**: Predict categorical outcomes (usually binary like Yes/No, 0/1).
- **Output**: A probability value between 0 and 1.
- **Decision Rule**: If probability ≥ 0.5, classify as 1; otherwise, classify as 0.
- **Model Formula**:

  \[
  P(Y=1) = \frac{1}{1 + e^{-(b_0 + b_1x_1 + b_2x_2 + ... + b_nx_n)}}
  \]

- This uses the **sigmoid function** to convert the linear combination of features into a probability.

---

## 🧠 How It Works

1. Compute a linear combination of inputs:
   \[
   z = b_0 + b_1x_1 + b_2x_2 + \dots + b_nx_n
   \]

2. Apply the **sigmoid function** to convert `z` into a value between 0 and 1:
   \[
   \sigma(z) = \frac{1}{1 + e^{-z}}
   \]

3. Use a threshold (commonly 0.5) to classify the result into class 0 or 1.

---

## 📌 Use Cases

- Email spam detection (Spam/Not Spam)
- Customer churn prediction (Churn/No Churn)
- Disease diagnosis (Positive/Negative)
- Loan approval (Approve/Reject)

---

## ✅ Advantages

- Simple and easy to implement
- Interpretable coefficients
- Probabilistic output
- Works well for linearly separable data

---

## ⚠️ Limitations

- Assumes linearity in the log-odds
- Not suitable for complex, non-linear relationships
- Sensitive to outliers and multicollinearity

---

## 📈 Sigmoid Function Plot (Optional)

You can visualize the sigmoid function with the equation:

\[
\sigma(z) = \frac{1}{1 + e^{-z}}
\]

It maps any real number to a value between 0 and 1.

---

## 📌 Summary

Logistic Regression is a powerful and interpretable model used to classify binary outcomes using probability estimates. It is most effective when the relationship between features and the outcome is approximately linear in the log-odds.

