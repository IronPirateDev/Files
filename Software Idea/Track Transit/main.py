from flask import Flask, render_template, request, redirect, jsonify
import mysql.connector as ms
from geopy.distance import great_circle
import random
import time

# Assuming you have established a connection named `conn`
db = ms.connect(host='localhost', user='root', password='dpsbn', database='hk')
cursor = db.cursor()

cursor.execute('select bus_id from buses')
a = cursor.fetchall()
l1 = []
for i in a:
    for j in i:
        if len(j) > 1:
            l1.append(j)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Loc.html')

@app.route('/err', methods=['POST'])
def modify_car():
    car_number = request.form.get('car_number')
    btn_pressed = request.form.get('btnpr')

    if btn_pressed == 'det':
        if car_number in l1:
            message = f"Details of {car_number}"
        else:
            message = f"{car_number} is an Invalid Bus Number"
    elif btn_pressed == 'livloc':
        if car_number in l1:
            get_location()
            writee()  
            randomgps(car_number)
            return redirect('/maps')
        else:
            message = f"{car_number} is an Invalid Bus Number"
    else:
        message = "Invalid action"

    return render_template('loc.html', message=message)

@app.route('/get_location')
def get_location():
    global latitude,longitude
    car_number = request.args.get('car_number')  # Get car_number from the request arguments
    cursor.execute('SELECT latitude, longitude FROM buses WHERE bus_id=%s', (car_number,))
    location = cursor.fetchone()
    latitude=location[0]
    longitude=location[1]
    return jsonify({'latitude': location[0], 'longitude': location[1]})
def writee():
    html_code = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <title>OpenStreetMap Display</title>
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.7.1/dist/leaflet.css" />
        <style>
            /* Set the height of the map container */
            #map {{ height: 500px; width: 100%; }}
            
            /* Increase the size of the bus icon */
            .bus-icon {{
                display: inline-block;
            }}
        </style>
    </head>
    <body>
        <div id="map"></div>

        <script src="https://unpkg.com/leaflet@1.7.1/dist/leaflet.js"></script>
        <script>
            var map = L.map('map').setView([{ latitude }, { longitude }], 15);
            L.tileLayer('https://{s}.tile.openstreetmap.org/{{z}}/{{x}}/{{y}}.png', {{
                maxZoom: 19,
            }}).addTo(map);

            var busMarker;
            var busSize = 50; // Set the desired bus size

            function updateBusSize() {{
                if (busMarker) {{
                    map.removeLayer(busMarker);
                }}

                var busIcon = L.divIcon({{
                    className: 'bus-icon',
                    html: '<span style="font-size:' + busSize + 'px;">&#128652;</span>',
                    iconAnchor: [busSize / 2, busSize / 2] // Set iconAnchor
                }});

                busMarker = L.marker([{ latitude }, { longitude }], {{ icon: busIcon }}).addTo(map);
            }}
            setInterval(function() {{
                location.reload();
            }}, 15000);

            // Call updateBusSize once immediately
            updateBusSize();
            
            function updateBusLocation() {{
                var car_number = '123'; // Replace with actual car number
                var url = '/get_location?car_number=' + car_number;
                
                fetch(url)
                    .then(response => response.json())
                    .then(data => {{
                        var latitude = data.latitude;
                        var longitude = data.longitude;

                        if (busMarker) {{
                            busMarker.setLatLng([latitude, longitude]);
                        }} else {{
                            var busIcon = L.divIcon({{
                                className: 'bus-icon',
                                html: '<span style="font-size:' + busSize + 'px;">&#128652;</span>',
                                iconAnchor: [busSize / 2, busSize / 2]
                            }});

                            busMarker = L.marker([latitude, longitude], {{ icon: busIcon }}).addTo(map);
                        }}
                    }});
            }}

            // Call updateBusLocation once immediately
            updateBusLocation();
        </script>
    </body>
    </html>
    '''

    with open('maps.html','w') as file:
        file.write(html_code)

@app.route('/maps')
def maps():
    return render_template('maps.html')

def randomgps(car_number):
    start_lat, start_lon = 13.121843505500348, 77.61101131509214
    end_lat, end_lon = 13.123456942202848, 77.63890477699468

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

    fake_route = generate_fake_route(start_lat, start_lon, end_lat, end_lon, 10)
    for i, point in enumerate(fake_route):
        print(f"Current Location: {point}")
        lat = point[0]
        lon = point[1]
        q1 = 'update buses set latitude=%s where bus_id=%s'
        cursor.execute(q1, (lat, car_number))
        db.commit()
        #time.sleep(20)

if __name__ == '__main__':
    app.run(debug=True)
