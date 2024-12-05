import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = pd.read_csv("..\statcast_pitch_swing_data_20240402_20241030_with_arm_angle.csv")

data = data.dropna(subset=['bat_speed', 'swing_length'])
data['bat_speed'] = pd.to_numeric(data['bat_speed'], errors='coerce')
data['swing_length'] = pd.to_numeric(data['swing_length'], errors='coerce')
data = data.dropna(subset=['bat_speed', 'swing_length'])

bat_speed = data['bat_speed']
swing_length = data['swing_length']

bat_speed_mean = np.mean(bat_speed)
swing_length_mean = np.mean(swing_length)

plt.figure(figsize=(10, 6))
plt.scatter(bat_speed, swing_length, color = 'blue', alpha=0.7)

slope, intercept = np.polyfit(bat_speed, swing_length, 1)
trendline = slope * bat_speed + intercept
plt.plot(bat_speed, trendline, color='red', linewidth=2, label=f"Trendline: y = {slope:.2f}x + {intercept:.2f}")

correlation = np.corrcoef(bat_speed, swing_length)[0, 1]

plt.title("Correlation Between Bat Speed and Swing Length", fontsize=16)
plt.xlabel("Bat Speed", fontsize=14)
plt.ylabel("Swing Length", fontsize=14)

plt.axvline(bat_speed_mean, color='yellow', linestyle='--', linewidth=2, label=f"Mean Bat Speed: {bat_speed_mean:.2f}")
plt.axhline(swing_length_mean, color='pink', linestyle='--', linewidth=2, label=f"Mean Swing Length: {swing_length_mean:.2f}")


plt.grid(True)
plt.show()

print(correlation)
print(bat_speed_mean)
print(swing_length_mean)