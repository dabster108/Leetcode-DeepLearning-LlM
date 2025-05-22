import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt

# Step 1: Create the dataset
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 'Sunny',
                'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Temp': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 'Mild',
             'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal', 'High',
                 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Wind': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak',
             'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
    'Decision': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No',
                 'Yes', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)

# Step 2: Convert categorical variables to numerical
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()

for column in df.columns:
    df[column] = le.fit_transform(df[column])

# Step 3: Split features and target
X = df[['Outlook', 'Temp', 'Humidity', 'Wind']]
y = df['Decision']

# Step 4: Train Decision Tree
clf = DecisionTreeClassifier(criterion='entropy')  # Using ID3 algorithm
clf = clf.fit(X, y)

# Step 5: Visualize the Decision Tree
plt.figure(figsize=(12,8))
tree.plot_tree(clf, feature_names=['Outlook', 'Temp', 'Humidity', 'Wind'], class_names=['No', 'Yes'], filled=True)
plt.show()
