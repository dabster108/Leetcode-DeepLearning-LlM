import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score, recall_score, f1_score
from sklearn.neighbors import KNeighborsClassifier

# Replace with your actual dataset path
dataset_path = "/Users/dikshanta/Documents/Introduction-to-LLM-models/SumarSirAi/healthcare-dataset-stroke-data.csv"

# Load dataset
try:
    df = pd.read_csv(dataset_path)
    print("Dataset loaded successfully!")
    print(f"Shape: {df.shape}")
    print("\nFirst 5 rows:")
    print(df.head())
except Exception as e:
    print(f"Error loading dataset: {e}")
    exit()

# Data Preprocessing
print("\nPreprocessing data...")

# Drop ID column if exists
if 'id' in df.columns:
    df = df.drop('id', axis=1)

# Handle missing values (example for bmi column)
if 'bmi' in df.columns:
    df['bmi'].fillna(df['bmi'].median(), inplace=True)

# Convert categorical variables
label_encoders = {}
categorical_cols = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']

for col in categorical_cols:
    if col in df.columns:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        label_encoders[col] = le

# Data Visualization
print("\nCreating exploratory visualizations...")
plt.figure(figsize=(18, 12))

# 1. Age distribution
plt.subplot(2, 3, 1)
sns.histplot(data=df, x='age', hue='stroke', kde=True)
plt.title('Age Distribution by Stroke Status')

# 2. Glucose level vs stroke
plt.subplot(2, 3, 2)
sns.boxplot(data=df, x='stroke', y='avg_glucose_level')
plt.title('Glucose Level by Stroke Status')

# 3. Hypertension relationship
plt.subplot(2, 3, 3)
sns.countplot(data=df, x='hypertension', hue='stroke')
plt.title('Hypertension and Stroke Relationship')

# 4. Heart disease relationship
plt.subplot(2, 3, 4)
sns.countplot(data=df, x='heart_disease', hue='stroke')
plt.title('Heart Disease and Stroke Relationship')

# 5. BMI distribution
plt.subplot(2, 3, 5)
sns.scatterplot(data=df, x='age', y='bmi', hue='stroke', alpha=0.6)
plt.title('Age vs BMI by Stroke Status')

plt.tight_layout()
plt.show()

# Prepare data for modeling
X = df.drop('stroke', axis=1)
y = df['stroke']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Feature scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Create and train Decision Tree
print("\nTraining Decision Tree model...")
dt_classifier = DecisionTreeClassifier(
    criterion='gini',
    max_depth=4,
    min_samples_split=10,
    min_samples_leaf=5,
    class_weight='balanced',  # Handles class imbalance
    random_state=42
)

dt_classifier.fit(X_train_scaled, y_train)

# Evaluate Decision Tree model
y_pred_dt = dt_classifier.predict(X_test_scaled)

print("\nDecision Tree Model Evaluation:")
accuracy_dt = accuracy_score(y_test, y_pred_dt)
precision_dt = precision_score(y_test, y_pred_dt)
recall_dt = recall_score(y_test, y_pred_dt)
f1_dt = f1_score(y_test, y_pred_dt)

print(f"Accuracy : {accuracy_dt:.4f}")
print(f"Precision: {precision_dt:.4f}")
print(f"Recall   : {recall_dt:.4f}")
print(f"F1 Score : {f1_dt:.4f}")

print("\nDetailed Classification Report:")
print(classification_report(y_test, y_pred_dt))

# Confusion Matrix for Decision Tree
plt.figure(figsize=(6, 4))
cm_dt = confusion_matrix(y_test, y_pred_dt)
sns.heatmap(cm_dt, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['No Stroke', 'Stroke'],
            yticklabels=['No Stroke', 'Stroke'])
plt.title('Decision Tree Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

# Feature Importance for Decision Tree
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Importance': dt_classifier.feature_importances_
}).sort_values('Importance', ascending=False)

plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=feature_importance)
plt.title('Feature Importance in Stroke Prediction (Decision Tree)')
plt.show()

# Visualize Decision Tree
plt.figure(figsize=(20, 10))
plot_tree(dt_classifier, 
          feature_names=X.columns, 
          class_names=['No Stroke', 'Stroke'],
          filled=True, 
          rounded=True,
          proportion=True,
          max_depth=2,  # Show first 2 levels for clarity
          fontsize=10)
plt.title('Decision Tree for Stroke Prediction (First 2 Levels)')
plt.show()

print("\nTraining and evaluation for Decision Tree complete!")

# ------------------------
# KNN Classifier Section
# ------------------------

print("\nTraining KNN model...")

# Initialize KNN with K=5 (you can tune this later)
knn = KNeighborsClassifier(n_neighbors=5)

# Train the model
knn.fit(X_train_scaled, y_train)

# Predict on test set
y_pred_knn = knn.predict(X_test_scaled)

# Evaluate KNN model
print("\nKNN Model Evaluation:")

accuracy_knn = accuracy_score(y_test, y_pred_knn)
precision_knn = precision_score(y_test, y_pred_knn)
recall_knn = recall_score(y_test, y_pred_knn)
f1_knn = f1_score(y_test, y_pred_knn)

print(f"Accuracy : {accuracy_knn:.4f}")
print(f"Precision: {precision_knn:.4f}")
print(f"Recall   : {recall_knn:.4f}")
print(f"F1 Score : {f1_knn:.4f}")

print("\nDetailed Classification Report:")
print(classification_report(y_test, y_pred_knn))

# Confusion Matrix for KNN
plt.figure(figsize=(6, 4))
cm_knn = confusion_matrix(y_test, y_pred_knn)
sns.heatmap(cm_knn, annot=True, fmt='d', cmap='Greens',
            xticklabels=['No Stroke', 'Stroke'],
            yticklabels=['No Stroke', 'Stroke'])
plt.title('KNN Confusion Matrix')
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.show()

print("\nTraining and evaluation for KNN complete!")
