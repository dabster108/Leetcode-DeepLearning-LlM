# Step 1: Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt

# Step 2: Load the Wine dataset
# Dataset has no headers, so we'll add them
column_names = ['class', 'alcohol', 'malic_acid', 'ash', 'alcalinity_of_ash', 
                'magnesium', 'total_phenols', 'flavanoids', 'nonflavanoid_phenols', 
                'proanthocyanins', 'color_intensity', 'hue', 'od280_od315_of_diluted_wines', 
                'proline']

# Load the dataset
df = pd.read_csv('/Users/dikshanta/Documents/Introduction-to-LLM-models/wine_data.csv', names=column_names)

# Preview the dataset
print("Dataset Preview:")
print(df.head())
print("\nDataset Info:")
print(f"Number of samples: {len(df)}")
print(f"Class distribution: {df['class'].value_counts().to_dict()}")

# Step 3: Preprocess data
# Separate features and target
X = df.drop('class', axis=1)
y = df['class']

# Step 4: Split into training (60%), validation (20%), and testing (20%)
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42, stratify=y_temp)
# Now: 60% train, 20% val, 20% test

# Step 5: Normalize features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_val_scaled = scaler.transform(X_val)
X_test_scaled = scaler.transform(X_test)

# Step 6: Find best K using validation data
accuracy_list = []
k_values = range(1, 12)
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train_scaled, y_train)
    y_val_pred = knn.predict(X_val_scaled)
    acc = accuracy_score(y_val, y_val_pred)
    accuracy_list.append(acc)
    print(f"K={k}, Validation Accuracy={acc:.4f}")

# Plot the k values vs. accuracy
plt.figure(figsize=(10, 6))
plt.plot(k_values, accuracy_list, marker='o')
plt.title('K Value vs. Validation Accuracy')
plt.xlabel('K Value')
plt.ylabel('Accuracy')
plt.grid(True)
plt.xticks(k_values)
plt.savefig('knn_wine_validation_accuracy.png')
plt.close()

# Step 7: Train final model on train+val with best K
best_k = accuracy_list.index(max(accuracy_list)) + 1
print("\nBest K value based on validation set:", best_k)

# Combine train and validation sets
X_combined = pd.concat([X_train, X_val])
y_combined = pd.concat([y_train, y_val])

# Scale the combined training data
X_combined_scaled = scaler.fit_transform(X_combined)

# Train final model on combined data
final_knn = KNeighborsClassifier(n_neighbors=best_k)
final_knn.fit(X_combined_scaled, y_combined)

# Step 8: Evaluate on test set
X_test_scaled = scaler.transform(X_test)
y_test_pred = final_knn.predict(X_test_scaled)
test_accuracy = accuracy_score(y_test, y_test_pred)
print("\nFinal Test Accuracy:", test_accuracy)
print("\nFinal Classification Report:")
print(classification_report(y_test, y_test_pred))

# Step 9: Plot confusion matrix
from sklearn.metrics import confusion_matrix
import seaborn as sns

cm = confusion_matrix(y_test, y_test_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['Class 1', 'Class 2', 'Class 3'],
            yticklabels=['Class 1', 'Class 2', 'Class 3'])
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.savefig('wine_confusion_matrix.png')
plt.close()

# Step 10: Feature importance (using a simple approach - correlation with classes)
# One hot encode the classes for correlation
class_dummies = pd.get_dummies(df['class'], prefix='class')
features_with_class = pd.concat([df.drop('class', axis=1), class_dummies], axis=1)

# Calculate correlation with each class
correlations = features_with_class.corr()
class_correlations = correlations[['class_1', 'class_2', 'class_3']].iloc[:-3]

# Plot feature importance based on absolute correlation
plt.figure(figsize=(12, 8))
class_correlations.abs().plot(kind='bar')
plt.title('Feature Importance (Absolute Correlation with Each Class)')
plt.xlabel('Features')
plt.ylabel('Absolute Correlation')
plt.xticks(rotation=90)
plt.tight_layout()
plt.savefig('wine_feature_importance.png')
plt.close()

print("\nAnalysis complete! KNN classifier successfully trained and evaluated.")