Confusion Matrix
A Confusion Matrix is a performance measurement tool for machine learning classification problems. It is a table that allows visualization of the performance of an algorithm, showing the actual vs. predicted classifications.

What is a Confusion Matrix?
A confusion matrix summarizes the results of a classification model by showing the counts of:

Correct and incorrect predictions broken down by each class.

How well the model is performing in terms of true and false positives and negatives.

Components of a Confusion Matrix
For a binary classification problem, the confusion matrix has four main components:

Predicted Positive	Predicted Negative
Actual Positive	True Positive (TP)	False Negative (FN)
Actual Negative	False Positive (FP)	True Negative (TN)

True Positive (TP): Correctly predicted positive cases.

True Negative (TN): Correctly predicted negative cases.

False Positive (FP): Incorrectly predicted positive cases (Type I error).

False Negative (FN): Incorrectly predicted negative cases (Type II error).

Metrics Derived from Confusion Matrix
Accuracy:

Accuracy
=
𝑇
𝑃
+
𝑇
𝑁
𝑇
𝑃
+
𝑇
𝑁
+
𝐹
𝑃
+
𝐹
𝑁
Accuracy= 
TP+TN+FP+FN
TP+TN
​
 
Precision:

Precision
=
𝑇
𝑃
𝑇
𝑃
+
𝐹
𝑃
Precision= 
TP+FP
TP
​
 
Recall (Sensitivity):

Recall
=
𝑇
𝑃
𝑇
𝑃
+
𝐹
𝑁
Recall= 
TP+FN
TP
​
 
F1 Score:

F1 Score
=
2
×
Precision
×
Recall
Precision
+
Recall
F1 Score=2× 
Precision+Recall
Precision×Recall
​
 
Example
Consider a binary classification model tested on 100 samples with the following confusion matrix:

Predicted Positive	Predicted Negative
Actual Positive	40	10
Actual Negative	5	45

TP = 40

FN = 10

FP = 5

TN = 45

From this:

Accuracy = (40 + 45) / 100 = 0.85 (85%)

Precision = 40 / (40 + 5) = 0.89 (89%)

Recall = 40 / (40 + 10) = 0.80 (80%)

F1 Score = 2 * (0.89 * 0.80) / (0.89 + 0.80) ≈ 0.84 (84%)