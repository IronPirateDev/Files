from geopy.distance import great_circle
import folium
import random

def generate_fake_route(start_lat, start_lon, end_lat, end_lon, num_points):
    route = []
    start = (start_lat, start_lon)
    end = (end_lat, end_lon)
    for _ in range(num_points):
        distance = great_circle(start, end).miles
        random_distance = random.uniform(0, distance)
        bearing = random.uniform(0, 360)
        destination = great_circle().destination(point=start, bearing=bearing, distance=random_distance)
        route.append((destination.latitude, destination.longitude))
        start = (destination.latitude, destination.longitude)
    return route

# Define start and end coordinates
start_lat, start_lon = 40.7128, -74.0060  # Example: New York City
end_lat, end_lon = 34.0522, -118.2437    # Example: Los Angeles

# Generate fake route with 10 points
fake_route = generate_fake_route(start_lat, start_lon, end_lat, end_lon, 10)

# Create map centered at the midpoint of the route
map_center = ((start_lat + end_lat) / 2, (start_lon + end_lon) / 2)
mymap = folium.Map(location=map_center, zoom_start=5)

# Plot fake route on the map
for point in fake_route:
    folium.CircleMarker(location=point, radius=3, color='blue').add_to(mymap)

# Save the map to an HTML file
mymap.save('fake_route_map.html')
