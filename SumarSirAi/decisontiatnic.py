import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load Titanic dataset (adjust path or load from seaborn or your file)
df = pd.read_csv('/Users/dikshanta/Documents/Introduction-to-LLM-models/SumarSirAi/titanic.csv')  # replace with your path

# Use specified features + target
features = ['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked']
target = 'survived'  # Adjust if your target column name is different

# Select features + target, drop missing values
df = df[features + [target]].dropna()

# One-hot encode categorical features (sex, embarked)
df = pd.get_dummies(df, columns=['sex', 'embarked'], drop_first=True)

# Split data into train (60%) and temp (40%)
X = df.drop(target, axis=1)
y = df[target]

X_train, X_temp, y_train, y_temp = train_test_split(X, y, train_size=0.6, random_state=42, stratify=y)

# Split temp into validation (20%) and test (20%) from original data
X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, train_size=0.5, random_state=42, stratify=y_temp)

# Hyperparameter tuning: try max_depth 1 to 10 on training + validation sets
best_depth = None
best_val_acc = 0
for depth in range(1, 11):
    clf = DecisionTreeClassifier(criterion='entropy', max_depth=depth, random_state=42)
    clf.fit(X_train, y_train)
    val_preds = clf.predict(X_val)
    val_acc = accuracy_score(y_val, val_preds)
    print(f"Max depth: {depth}, Validation Accuracy: {val_acc:.4f}")
    if val_acc > best_val_acc:
        best_val_acc = val_acc
        best_depth = depth

print(f"\nBest max_depth based on validation: {best_depth}")

# Retrain final model on train + validation sets with best max_depth
X_final_train = pd.concat([X_train, X_val])
y_final_train = pd.concat([y_train, y_val])

final_clf = DecisionTreeClassifier(criterion='entropy', max_depth=best_depth, random_state=42)
final_clf.fit(X_final_train, y_final_train)

# Evaluate on test set
y_test_pred = final_clf.predict(X_test)

accuracy = accuracy_score(y_test, y_test_pred)
precision = precision_score(y_test, y_test_pred)
recall = recall_score(y_test, y_test_pred)
f1 = f1_score(y_test, y_test_pred)

print("\nTest Set Performance:")
print(f"Accuracy:  {accuracy:.4f}")
print(f"Precision: {precision:.4f}")
print(f"Recall:    {recall:.4f}")
print(f"F1-score:  {f1:.4f}")

# Visualize decision tree
plt.figure(figsize=(20,10))
plot_tree(final_clf, feature_names=X_final_train.columns, class_names=['Not Survived', 'Survived'], filled=True, rounded=True)
plt.title("Final Decision Tree")
plt.show()

# Confusion matrix heatmap
cm = confusion_matrix(y_test, y_test_pred)
plt.figure(figsize=(6,5))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Not Survived', 'Survived'], yticklabels=['Not Survived', 'Survived'])
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()
