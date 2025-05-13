# Import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Load and clean data
df = pd.read_csv('/Users/dikshanta/Documents/Introduction-to-LLM-models/SumarSirAi/healthcare-dataset-stroke-data.csv')
df = df.dropna()

# Select two features
features = ['age', 'avg_glucose_level']
X = df[features]
y = df['stroke']

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
model = LogisticRegression(class_weight='balanced', random_state=42)
model.fit(X_scaled, y)

# Create visualization
plt.figure(figsize=(10, 6))

# Create mesh grid
x_min, x_max = X_scaled[:, 0].min() - 1, X_scaled[:, 0].max() + 1
y_min, y_max = X_scaled[:, 1].min() - 1, X_scaled[:, 1].max() + 1
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                     np.linspace(y_min, y_max, 100))

# Predict probabilities
Z = model.predict_proba(np.c_[xx.ravel(), yy.ravel()])[:, 1]
Z = Z.reshape(xx.shape)

# Plot decision boundary
plt.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')

# Plot data points
plt.scatter(X_scaled[y==0, 0], X_scaled[y==0, 1], 
            c='blue', label='No Stroke', edgecolor='k', alpha=0.6)
plt.scatter(X_scaled[y==1, 0], X_scaled[y==1, 1], 
            c='red', label='Stroke', edgecolor='k', alpha=0.8)

plt.xlabel('Age (standardized)')
plt.ylabel('Average Glucose Level (standardized)')
plt.title('Stroke Risk: Age vs Glucose Level')
plt.colorbar(label='Stroke Probability')
plt.legend()
plt.show()

# Print model coefficients
print("Two-Feature Model Results:")
print(f"Coefficient for Age: {model.coef_[0][0]:.4f}")
print(f"Coefficient for Glucose: {model.coef_[0][1]:.4f}")
print(f"Intercept: {model.intercept_[0]:.4f}")