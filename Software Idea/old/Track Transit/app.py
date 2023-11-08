import sqlite3

conn = sqlite3.connect('bus_data.db')  # This will create a new SQLite database file named bus_data.db
cursor = conn.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_data/<busid>')
def get_data(busid):
    q1 = 'select bus_id,emission_compliance,fuel_type,vehicle_no from buses where bus_id=%s'
    cursor.execute(q1, (busid,))
    data = cursor.fetchone()
    return {'data': data}

@app.route('/get_maps_link/<busid>')
def get_maps_link(busid):
    base_url = "https://www.google.com/maps?q="
    q1 = 'SELECT latitude, longitude FROM buses WHERE bus_id=%s'
    cursor.execute(q1, (busid,))
    coordinates = cursor.fetchone()

    if coordinates:
        latitude, longitude = float(coordinates[0]), float(coordinates[1])
        google_maps_link = f"{base_url}{latitude},{longitude}"
        return {'link': google_maps_link}
    else:
        return {'error': f"No coordinates found for bus ID {busid}"}

if __name__ == '__main__':
    app.run(debug=True)