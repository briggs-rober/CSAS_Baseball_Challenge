import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("..\statcast_pitch_swing_data_20240402_20241030_with_arm_angle.csv")

data = data.dropna(subset=['bat_speed', 'swing_length'])
data['bat_speed'] = pd.to_numeric(data['bat_speed'], errors='coerce')
data['swing_length'] = pd.to_numeric(data['swing_length'], errors='coerce')
data = data.dropna(subset=['bat_speed', 'swing_length'])

def FilterData(data, column, variable, color, label, alpha, size):
    filtered_data = data[data[column] == variable]
    bat_speed = filtered_data['bat_speed']
    swing_length = filtered_data['swing_length']
    plt.scatter(bat_speed, swing_length, s = size, color = color, label = label, alpha = alpha)

def HomeTeamFilterData(data, team, color, label):
    filtered_data = data[data['home_score'] == data["bat_score"]]
    filtered_data2 = filtered_data[filtered_data['home_team'] == team]
    bat_speed = filtered_data2['bat_speed']
    swing_length = filtered_data2['swing_length']
    plt.scatter(bat_speed, swing_length, color = color, label = label)

def AwayTeamFilterData(data, team, color, label):
    filtered_data = data[data['away_score'] == data["bat_score"]]
    filtered_data2 = filtered_data[filtered_data['away_team'] == team]
    bat_speed = filtered_data2['bat_speed']
    swing_length = filtered_data2['swing_length']
    plt.scatter(bat_speed, swing_length, color = color, label = label)


plt.figure(figsize=(10, 6))
FilterData(data, "outs_when_up", 2, "red", "2 Outs", 1, 1)
FilterData(data, "outs_when_up", 1, "yellow", "1 Out", 1, 1)
FilterData(data, "outs_when_up", 0, "green", "0 Outs", 1, 1)

plt.title("Correlation Between Bat Speed and Swing Length", fontsize=16)
plt.xlabel("Bat Speed", fontsize=14)
plt.ylabel("Swing Length", fontsize=14)

plt.grid(True)
plt.legend()
plt.show()