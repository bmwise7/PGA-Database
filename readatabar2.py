import json
import matplotlib.pyplot as plt

# Read the JSON file
with open('pgadatabase/data.json') as myjsonfile:
    data = json.load(myjsonfile)

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
plt.bar(brands, average_distances, color='lightgreen')
plt.xlabel('Driver Brand (Number of Players)')
plt.ylabel('Average Driving Distance (yards)')
plt.title('Driver Brands with Highest Average Driving Distance')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Set a custom ylim for the left axis to reduce the margin
plt.ylim(260, max(average_distances) + 10)  # Adjust the lower limit (260) to your preference

# Add annotations for the number of players next to the brand names
for i in range(len(brands)):
    plt.annotate(f"({num_players[i]})", xy=(i, average_distances[i]), ha='center', va='bottom')

plt.show()
