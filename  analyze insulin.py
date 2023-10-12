import pandas as pd
import matplotlib.pyplot as plt

# Load insulin data from a CSV file (replace 'your_data.csv' with your actual data file)
insulin_data = pd.read_csv('your_data.csv')

# Plot a time series of blood glucose levels
plt.figure(figsize=(12, 6))
plt.plot(insulin_data['Timestamp'], insulin_data['Glucose'], marker='o', linestyle='-')
plt.title('Blood Glucose Levels Over Time')
plt.xlabel('Timestamp')
plt.ylabel('Glucose Level')
plt.grid(True)
plt.show()

