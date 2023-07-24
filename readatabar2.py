import json
import matplotlib.pyplot as plt

# Read the JSON file
with open('pgadatabase/data.json') as myjsonfile:
    data = json.load(myjsonfile)

#----------------BAR CHART: DRIVING BRAND DISTANCE LEADERS----------------#
# Prepare data for the bar chart
driver_brands = {}
for player_data in data.values():
    driver_brand = player_data.get("Driver Brand")
    driving_distance = player_data.get("Driving Distance")
    
    if driver_brand in driver_brands:
        driver_brands[driver_brand].append(driving_distance)
    else:
        driver_brands[driver_brand] = [driving_distance]

# Calculate the average driving distance for each driver brand and count the number of players using each brand
brand_stats = {}
for brand, distances in driver_brands.items():
    brand_stats[brand] = {
        "Average Driving Distance": sum(distances) / len(distances),
        "Number of Players": len(distances)
    }

# Sort the driver brands based on average driving distance in descending order
sorted_brands = dict(sorted(brand_stats.items(), key=lambda x: x[1]["Average Driving Distance"], reverse=True))

# Extract the brand names, average distances, and number of players for plotting
brands = list(sorted_brands.keys())
average_distances = [stats["Average Driving Distance"] for stats in sorted_brands.values()]
num_players = [stats["Number of Players"] for stats in sorted_brands.values()]

# Create the bar chart for driver brands with the highest average driving distance and number of players
plt.figure(figsize=(12, 6))
bars = plt.bar(brands, average_distances, color='lightgreen')
plt.xlabel('Driver Brand')
plt.ylabel('Average Driving Distance (yards)')
plt.title('Driver Brands with Highest Average Driving Distance')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Set a custom ylim for the left axis to reduce the margin
plt.ylim(260, max(average_distances) + 10)  # Adjust the lower limit (260) to your preference

# Add annotations for the number of players below the brand names and the average above the bars
for i, bar in enumerate(bars):
    plt.annotate(f"{average_distances[i]:.1f}", xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()), 
                 ha='center', va='bottom')
    plt.annotate(f"({num_players[i]})", xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()), 
                 ha='center', va='top')

plt.show()

#----------------BAR CHART: PUTTER BRAND SG PUTTING LEADERS----------------#
# Prepare data for the bar chart
putter_brands = {}
putter_sg_putting = {}

# Iterate through each player in the data
for player_data in data.values():
    putter_brand = player_data.get("Putter Brand")
    sg_putting = player_data.get("SG: Putting")
    
    if putter_brand in putter_brands:
        putter_brands[putter_brand]["count"] += 1
        putter_brands[putter_brand]["sg_putting_sum"] += sg_putting
    else:
        putter_brands[putter_brand] = {"count": 1, "sg_putting_sum": sg_putting}

# Calculate the average strokes gained putting for each putter brand
for brand, values in putter_brands.items():
    values["sg_putting_avg"] = values["sg_putting_sum"] / values["count"]

# Sort the data by average strokes gained putting in descending order
sorted_putter_data = sorted(putter_brands.items(), key=lambda x: x[1]["sg_putting_avg"], reverse=True)

putter_brands = [item[0] for item in sorted_putter_data]
average_sg_putting = [item[1]["sg_putting_avg"] for item in sorted_putter_data]
player_counts = [item[1]["count"] for item in sorted_putter_data]

# Create the bar chart for average strokes gained putting
plt.figure(figsize=(12, 6))
bars = plt.bar(putter_brands, average_sg_putting, color='lightcoral')
plt.xlabel('Putter Brands')
plt.ylabel('Average Strokes Gained Putting')
plt.title('Average Strokes Gained Putting for Each Putter Brand')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Add player counts above each brand name and average below each bar
for bar, count, avg in zip(bars, player_counts, average_sg_putting):
    plt.annotate(f"{avg:.2f}", (bar.get_x() + bar.get_width() / 2, bar.get_height()), 
                 ha='center', va='bottom', fontsize=8)
    plt.annotate(f"({count})", (bar.get_x() + bar.get_width() / 2, bar.get_height()), 
                 ha='center', va='top', fontsize=8)

# Adjust left margin to be smaller
plt.margins(0.05)

plt.show()
