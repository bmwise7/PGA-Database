import json
import matplotlib.pyplot as plt

# Read the JSON file
with open('pgadatabase/data.json') as myjsonfile:
    data = json.load(myjsonfile)

#----------------BAR CHART: AVERAGE DRIVING DISTANCE FOR EACH PLAYER----------------#
# Prepare data for the bar chart
players_driving = []
driving_distances = []

# Iterate through each player in the data
for player_data in data.values():
    player_name = player_data.get("Player Name")
    driving_distance = player_data.get("Driving Distance")
    
    players_driving.append(player_name)
    driving_distances.append(driving_distance)

# Sort the data by driving distances in descending order
sorted_driving_data = sorted(zip(players_driving, driving_distances), key=lambda x: x[1])
players_driving, driving_distances = zip(*sorted_driving_data[::-1])  # Reverse the lists

# Create the bar chart for average driving distance
plt.figure(figsize=(12, 6))
plt.bar(players_driving, driving_distances, color='skyblue')
plt.xlabel('Player Name')
plt.ylabel('Average Driving Distance')
plt.title('Average Driving Distance for Each Player')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()

#----------------BAR CHART: STROKES GAINED PUTTING FOR EACH PLAYER----------------#
# Prepare data for the bar chart
players_putting = []
sg_putting_values = []

# Iterate through each player in the data
for player_data in data.values():
    player_name = player_data.get("Player Name")
    sg_putting = player_data.get("SG: Putting")
    
    players_putting.append(player_name)
    sg_putting_values.append(sg_putting)

# Sort the data by strokes gained putting in descending order
sorted_putting_data = sorted(zip(players_putting, sg_putting_values), key=lambda x: x[1])
players_putting, sg_putting_values = zip(*sorted_putting_data[::-1])  # Reverse the lists

# Create the bar chart for strokes gained putting
plt.figure(figsize=(12, 6))
plt.bar(players_putting, sg_putting_values, color='lightcoral')
plt.xlabel('Player Name')
plt.ylabel('Strokes Gained Putting')
plt.title('Strokes Gained Putting for Each Player')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
