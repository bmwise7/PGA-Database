import json
import matplotlib.pyplot as plt

# Read the JSON file
with open('pgadatabase/data.json') as myjsonfile:
    data = json.load(myjsonfile)

#----------------PIE CHART: LEADING PUTTER BRANDS----------------#
# Get the count of each putter brand
putter_brands = {}
for player_data in data.values():
    putter_brand = player_data.get("Putter Brand")
    if putter_brand in putter_brands:
        putter_brands[putter_brand] += 1
    else:
        putter_brands[putter_brand] = 1

# Create a pie chart for putter brands
plt.figure(figsize=(8, 8))
plt.pie(putter_brands.values(), labels=putter_brands.keys(), autopct='%1.1f%%', startangle=140)
plt.title("Leading Putter Brands")
plt.axis('equal')
plt.show()

#----------------PIE CHART: LEADING DRIVER BRANDS----------------#
# Get the count of each driver brand
driver_brands = {}
for player_data in data.values():
    driver_brand = player_data.get("Driver Brand")
    if driver_brand in driver_brands:
        driver_brands[driver_brand] += 1
    else:
        driver_brands[driver_brand] = 1

# Create a pie chart for driver brands
plt.figure(figsize=(8, 8))
plt.pie(driver_brands.values(), labels=driver_brands.keys(), autopct='%1.1f%%', startangle=140)
plt.title("Leading Driver Brands")
plt.axis('equal')
plt.show()
