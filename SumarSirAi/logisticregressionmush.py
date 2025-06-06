import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
import seaborn as sns
import matplotlib.pyplot as plt

# 1. Load dataset
df = pd.read_csv("/Users/dikshanta/Documents/Introduction-to-LLM-models/SumarSirAi/mushrooms.csv")

# 2. Handle missing values
df.replace("?", pd.NA, inplace=True)
df.dropna(inplace=True)

# 3. Encode categorical variables
label_encoders = {}
for column in df.columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# 4. Split data into features and target
X = df.drop("class", axis=1)
y = df["class"]

# 5. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 6. Train logistic regression model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# 7. Predict on test data
y_pred = model.predict(X_test)

# 8. Calculate evaluation metrics
acc = accuracy_score(y_test, y_pred)
prec = precision_score(y_test, y_pred)
rec = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("Accuracy:", acc)
print("Precision:", prec)
print("Recall:", rec)
print("F1-Score:", f1)

# 9. Confusion matrix plot
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=["Edible", "Poisonous"],
            yticklabels=["Edible", "Poisonous"])
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")
plt.show()

# 10. Plot all metrics in one bar chart
metrics = {"Accuracy": acc, "Precision": prec, "Recall": rec, "F1-Score": f1}
metrics_df = pd.DataFrame.from_dict(metrics, orient='index', columns=['Score']).reset_index()
metrics_df.columns = ['Metric', 'Score']

plt.figure(figsize=(8,5))
sns.barplot(x='Metric', y='Score', data=metrics_df, palette='viridis')
plt.ylim(0, 1)
plt.title("Logistic Regression Performance Metrics")
plt.ylabel("Score")

# Optional: Add value labels on top of bars
for index, row in metrics_df.iterrows():
    plt.text(index, row.Score + 0.02, f"{row.Score:.2f}", ha='center', fontsize=12)

plt.show()

# Optional: Print full classification report
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=["Edible", "Poisonous"]))

