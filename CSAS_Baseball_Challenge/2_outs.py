import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Define a function to filter data and add to the plot
def plot_by_outs(outs, color, label):
    # Filter the data for the given number of outs
    filtered_data = data[data['outs_when_up'] == outs]

    # Extract relevant columns
    bat_speed = filtered_data['bat_speed']
    swing_length = filtered_data['swing_length']

    # Scatter plot for this condition
    plt.scatter(bat_speed, swing_length, color=color, alpha=0.7, label=label)

    # Optionally, add a trendline
    if len(bat_speed) > 1:  # Ensure enough points for trendline
        slope, intercept = np.polyfit(bat_speed, swing_length, 1)
        trendline = slope * bat_speed + intercept
        plt.plot(bat_speed, trendline, color=color, linestyle='--', linewidth=2)


# Load your data
file_path = "..\statcast_pitch_swing_data_20240402_20241030_with_arm_angle.csv"
data = pd.read_csv(file_path)

# Ensure columns are numeric and clean missing data
data = data.dropna(subset=['bat_speed', 'swing_length'])
data['bat_speed'] = pd.to_numeric(data['bat_speed'], errors='coerce')
data['swing_length'] = pd.to_numeric(data['swing_length'], errors='coerce')
data = data.dropna()

# Create the plot
plt.figure(figsize=(12, 8))

# Add data for each outs condition
plot_by_outs(outs=0, color='green', label='No Outs')
plot_by_outs(outs=1, color='purple', label='One Out')
plot_by_outs(outs=2, color='blue', label='Two Outs')

# Add labels, title, and legend
plt.title("Swing Speed vs. Bat Length by Outs", fontsize=16)
plt.xlabel("Bat Speed", fontsize=14)
plt.ylabel("Swing Length", fontsize=14)
plt.legend(fontsize=12)
plt.grid(True)

# Show the plot
plt.show()