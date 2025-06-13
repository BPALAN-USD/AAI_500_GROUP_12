from faker import Faker
import random
import pandas as pd

fake = Faker()

# Parameters
num_users = 6000
countries = ['US', 'UK', 'IN']
genders = ['Male', 'Female', 'Other']

# Generate data
data = []
for i in range(1, num_users + 1):
    user = {
        'userid': f'User {i}',
        'age': random.randint(18, 80),
        'gender': random.choice(genders),
        'country': random.choice(countries)
    }
    data.append(user)

# Create DataFrame
df = pd.DataFrame(data)

# Optional: Save to CSV
df.to_csv('fake_users.csv', index=False)

print(df.head())
