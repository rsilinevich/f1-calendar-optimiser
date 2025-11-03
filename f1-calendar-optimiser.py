import math

def haversine(lat1, lon1, lat2, lon2):
    # Calculate the great circle distance between two points on the earth (specified in decimal degrees)
    # Returns distance in kilometers
    
    # Convert degrees to radians
    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    
    # Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    radius = 6371  # Earth's radius in kilometers
    distance = c * radius
    return distance


def nearest_neighbor(lat, lon, points):
    # Find the nearest neighbor to a given point from a list of points
    
    # Args:
    #     lat: latitude of current point
    #     lon: longitude of current point
    #     points: list of (name, (lat, lon)) tuples
    
    # Returns:
    #     tuple: nearest neighbor point
    min_distance = float('inf')
    nearest = None
    
    for point in points:
        distance = haversine(lat, lon, point[1][0], point[1][1])
        if distance < min_distance:
            min_distance = distance
            nearest = point
    
    return nearest


def optimize_route(locations): 
    # Optimize route using nearest neighbor algorithm
    
    # Args:
    #     locations: list of (name, (lat, lon)) tuples
    
    # Returns:
    #     list: optimized route as list of (from_location, to_location) tuples
    route = []
    remaining = locations.copy()
    current = remaining.pop(0)  # Start from first location
    
    while remaining:
        lat, lon = current[1]
        nearest = nearest_neighbor(lat, lon, remaining)
        route.append((current, nearest))
        current = remaining.pop(remaining.index(nearest))
    
    return route


def calculate_total_distance(route_pairs):
    # Calculate total distance for a route
    total = 0
    for loc1, loc2 in route_pairs:
        distance = haversine(loc1[1][0], loc1[1][1], loc2[1][0], loc2[1][1])
        total += distance
    return total


def print_route(locations, route_pairs, title):
    # Print route with distances
    print(f"\n{title}")
    print("=" * 60)
    
    total_distance = 0
    for i, (loc1, loc2) in enumerate(route_pairs, 1):
        distance = haversine(loc1[1][0], loc1[1][1], loc2[1][0], loc2[1][1])
        total_distance += distance
        print(f"{i:2d}. {loc1[0]:20s} → {loc2[0]:20s} ({distance:7.2f} km)")
    
    print("-" * 60)
    print(f"Total distance: {total_distance:.2f} km\n")


# F1 race locations with coordinates
locations = [
    ("Bahrain", (26.0347, 50.5089)),
    ("Saudi Arabia", (21.6334, 39.1035)),
    ("Australia", (-37.8490, 144.9680)),
    ("Azerbaijan", (40.4083, 49.8622)),
    ("Miami", (25.9566, -80.2310)),
    ("Imola", (44.3447, 11.7155)),
    ("Monaco", (43.7347, 7.4197)),
    ("Spain", (41.5728, 2.2661)),
    ("Canada", (45.5079, -73.5290)),
    ("Austria", (47.2183, 14.7606)),
    ("Great Britain", (52.0786, -1.0169)),
    ("Hungary", (47.5106, 19.2556)),
    ("Belgium", (50.4373, 5.9750)),
    ("Netherlands", (52.3744, 4.5397)),
    ("Monza", (45.6237, 9.2844)),
    ("Singapore", (1.2931, 103.8550)),
    ("Japan", (34.8414, 136.5460)),
    ("Qatar", (25.4861, 51.4523)),
    ("Austin", (30.1375, -97.6400)),
    ("Mexico", (19.4052, -99.0930)),
    ("Brazil", (-23.7010, -46.6980)),
    ("Las Vegas", (36.1068, -115.1600)),
    ("Abu Dhabi", (24.4749, 54.6038))
]

# Calculate original calendar order distance
original_route = [(locations[i], locations[i+1]) for i in range(len(locations) - 1)]
print_route(locations, original_route, "Official Calendar Order")

# Calculate optimized route
optimized_route = optimize_route(locations)
print_route(locations, optimized_route, "Optimized Route (Nearest Neighbor)")

# Calculate improvement
original_distance = calculate_total_distance(original_route)
optimized_distance = calculate_total_distance(optimized_route)
improvement = ((original_distance - optimized_distance) / original_distance) * 100

print(f"Distance saved: {original_distance - optimized_distance:.2f} km ({improvement:.1f}%)")