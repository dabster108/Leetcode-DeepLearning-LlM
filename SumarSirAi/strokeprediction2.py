import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import os

# Function to get user input
def get_user_input():
    print("\nAvailable features: age, avg_glucose_level, bmi, hypertension, heart_disease")
    feature1 = input("Enter first feature: ").strip()
    feature2 = input("Enter second feature: ").strip()
    value1 = float(input(f"Enter value for {feature1}: "))
    value2 = float(input(f"Enter value for {feature2}: "))
    return [feature1, feature2], [value1, value2]

# Load and prepare data
script_dir = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(script_dir, 'healthcare-dataset-stroke-data.csv')

try:
    df = pd.read_csv(csv_path)
    df = df.dropna()
    
    # Let user choose features
    features, values = get_user_input()
    
    # Validate features
    available_features = ['age', 'avg_glucose_level', 'bmi', 'hypertension', 'heart_disease']
    if not all(f in available_features for f in features):
        raise ValueError("Invalid feature(s) selected")

    # Prepare data
    X = df[features]
    y = df['stroke']
    
    # Scale features
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Train model
    model = LogisticRegression(class_weight='balanced', random_state=42)
    model.fit(X_scaled, y)
    
    # Scale user input and predict
    user_input_scaled = scaler.transform([values])
    probability = model.predict_proba(user_input_scaled)[0, 1]
    
    # Show results
    print("\nPrediction Results:")
    print(f"Features used: {features[0]} and {features[1]}")
    print(f"Input values: {values[0]} ({features[0]}), {values[1]} ({features[1]})")
    print(f"Stroke Probability: {probability:.2%}")
    print("Risk Level: " + ("High" if probability > 0.5 else "Low"))
    
except FileNotFoundError:
    print(f"Error: File not found at {csv_path}")
except ValueError as e:
    print(f"Error: {str(e)}")
except Exception as e:
    print(f"An error occurred: {str(e)}")