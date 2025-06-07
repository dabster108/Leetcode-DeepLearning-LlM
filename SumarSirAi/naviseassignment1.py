import pandas as pd
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder

# Step 1: Create the dataset
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast',
                'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Temp.': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool',
              'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal',
                 'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong',
             'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
    'Decision': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes',
                 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)

# Step 2: Encode categorical features
le_outlook = LabelEncoder()
le_temp = LabelEncoder()
le_humidity = LabelEncoder()
le_wind = LabelEncoder()
le_decision = LabelEncoder()

df['Outlook'] = le_outlook.fit_transform(df['Outlook'])
df['Temp.'] = le_temp.fit_transform(df['Temp.'])
df['Humidity'] = le_humidity.fit_transform(df['Humidity'])
df['Wind'] = le_wind.fit_transform(df['Wind'])
df['Decision'] = le_decision.fit_transform(df['Decision'])

# Step 3: Separate features and target
X = df[['Outlook', 'Temp.', 'Humidity', 'Wind']]
y = df['Decision']

# Step 4: Train the model
model = CategoricalNB()
model.fit(X, y)

# Step 5: Predict for the given input:
# Outlook: Rain, Temp: Hot, Humidity: Normal, Wind: Strong
input_data = pd.DataFrame([[
    le_outlook.transform(['Rain'])[0],
    le_temp.transform(['Hot'])[0],
    le_humidity.transform(['Normal'])[0],
    le_wind.transform(['Strong'])[0]
]])

prediction = model.predict(input_data)
predicted_label = le_decision.inverse_transform(prediction)

print("Decision:", predicted_label[0])