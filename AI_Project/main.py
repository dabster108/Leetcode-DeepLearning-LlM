import pandas as pd
import numpy as np

# Expanded list of real-world interests
interests = [
    # Technology
    "AI", "Cybersecurity", "Data Science", "Software Development", "Robotics",
    # Healthcare
    "Medicine", "Nursing", "Psychology", "Biomedical Engineering",
    # Business
    "Entrepreneurship", "Marketing", "Finance", "HR",
    # Arts
    "Graphic Design", "Film", "Music", "Creative Writing",
    # Law
    "Criminal Law", "Corporate Law", "Human Rights",
    # Science
    "Physics", "Biology", "Environmental Science",
    # Trades
    "Culinary Arts", "Fashion Design"
]

# Load your dataset
df = pd.read_csv("/Users/dikshanta/Documents/Introduction-to-LLM-models/AI_Project/datasets/education_career_success.csv")

# Calculate sum of current weights (for verification)
current_weights = [0.15, 0.1, 0.1, 0.1, 0.05,  # Tech-heavy weights
                   0.08, 0.05, 0.05, 0.04,      # Healthcare
                   0.07, 0.06, 0.05, 0.03,      # Business
                   0.03, 0.02, 0.02, 0.01,      # Arts
                   0.03, 0.02, 0.01,            # Law
                   0.02, 0.02, 0.01,            # Science
                   0.01, 0.01]                  # Trades

print(f"Sum of weights: {sum(current_weights)}")  # Should be 1.0

# Normalize weights to sum to 1
normalized_weights = np.array(current_weights) / sum(current_weights)

# Add random interests with normalized weights
df["Interest"] = np.random.choice(
    interests,
    size=len(df),
    p=normalized_weights
)

# Save with corrected path
output_path = "/Users/dikshanta/Documents/Introduction-to-LLM-models/AI_Project/datasets/student_data_interests.csv"
df.to_csv(output_path, index=False)

print(f"Dataset successfully saved with Interest column to: {output_path}")