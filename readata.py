import json

# Read the JSON file
with open('pgadatabase/data.json') as myjsonfile:
    data = json.load(myjsonfile)

"""
#----------------SORTED BY DRIVING DISTANCE----------------#
# Sort the data by driving distance in descending order
sorted_data = sorted(data.items(), key=lambda x: x[1]['Driving Distance'], reverse=True)

# Iterate through each player in the sorted data
for player_key, player_data in sorted_data:
    # Access the player name and other attributes for the current player
    player_name = player_data.get("Player Name")
    driver_brand = player_data.get("Driver Brand")
    driving_distance = player_data.get("Driving Distance")

    # Print the values for the current player
    print("Player Name:", player_name)
    print("Driver Brand:", driver_brand)
    print("Driving Distance:", driving_distance)
    print("------------------------")
"""

"""
#----------------SORTED BY STROKES GAINED PUTTING----------------#
# Sort the data by Strokes Gained Putting in descending order
sorted_data = sorted(data.items(), key=lambda x: x[1]['SG: Putting'], reverse=True)

# Iterate through each player in the sorted data
for player_key, player_data in sorted_data:
    # Access the player name and other attributes for the current player
    player_name = player_data.get("Player Name")

    sg_putting = player_data.get("SG: Putting")
    putter_brand = player_data.get("Putter Brand")

    # Print the values for the current player
    print("Player Name:", player_name)
    print("Putter Brand:", putter_brand)
    print("Strokes Gained Putting:", sg_putting)
    print("------------------------")
"""

#----------------ALL PLAYERS FROM DATABASE----------------#
# Iterate through each player in the data
for player_key, player_data in data.items():
    # Access the player name and other attributes for the current player
    player_name = player_data.get("Player Name")
    owgr = player_data.get("Official World Golf Ranking")
    sg_total = player_data.get("SG: Total")
    sg_off_the_tee = player_data.get("SG: Off-the-Tee")
    sg_tee_to_green = player_data.get("SG: Tee-to-Green")
    sg_around_the_green = player_data.get("SG: Around-the-Green")
    putter_brand = player_data.get("Putter Brand")
    sg_putting = player_data.get("SG: Putting")
    driver_brand = player_data.get("Driver Brand")
    driving_distance = player_data.get("Driving Distance")
    # Add other attributes as needed...
    

    # Print the values for the current player
    print("Player Name:", player_name)
    print("Offical World Golf Ranking:", owgr)
    print("SG: Total:", sg_total)
    print("SG: Off-the-Tee:", sg_off_the_tee)
    print("SG: Tee-to-Green:", sg_tee_to_green)
    print("SG: Around-the-Green:", sg_around_the_green)
    print("Putter Brand:", putter_brand)
    print("SG: Putting:", sg_putting)
    print("Driver Brand:", driver_brand)
    print("Driving Distance:", driving_distance)
    # Add other print statements as needed...
    print("------------------------")