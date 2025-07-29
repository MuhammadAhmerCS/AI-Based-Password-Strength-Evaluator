import pandas as pd
import string
import random

# Generate synthetic but realistic passwords
def generate_password(strength):
    if strength == 0:  # Weak
        samples = ['12345', 'password', 'abc', '111111', 'letmein']
    elif strength == 1:  # Medium
        samples = ['abc123', 'hello2024', 'welcome1', 'admin007', 'qwerty12']
    elif strength == 2:  # Strong
        samples = ['P@ssw0rd123', 'Secure@2024', 'Myp@ss_99', 'Tough#Pass!3', 'S3cur3#Me']
    return random.choices(samples, k=200)

# Create dataset
data = []
for label in [0, 1, 2]:
    for pwd in generate_password(label):
        data.append([pwd, label])

# Shuffle and save
df = pd.DataFrame(data, columns=['password', 'label'])
df = df.sample(frac=1).reset_index(drop=True)
df.to_csv("password_data.csv", index=False)

print("✅ password_data.csv created.")


from google.colab import files
files.download("password_data.csv")
