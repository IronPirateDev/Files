from geopy.distance import great_circle
import random
import time
import mysql.connector as ms
db=ms.connect(host='localhost',user='root',password='dpsbn',database='hk')
cursor=db.cursor()
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
start_lat, start_lon = 13.121843505500348, 77.61101131509214
end_lat, end_lon = 13.123456942202848, 77.63890477699468    
busid=input("Enter the Bus ID for Randomization:")
# Generate fake route with 10 points
fake_route = generate_fake_route(start_lat, start_lon, end_lat, end_lon, 20)
for i, point in enumerate(fake_route):
    print(f"Current Location: {point}")
    lat=point[0]
    lon=point[1]
    q1 = 'update buses set latitude=%s where bus_id=%s'
    cursor.execute(q1, (lat, busid))
    q2 = 'update buses set longitude=%s where bus_id=%s'
    cursor.execute(q2, (lon, busid))
    db.commit()
    time.sleep(10)
db.close()