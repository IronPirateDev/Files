from flask import Flask, jsonify
import mysql.connector as ms
app = Flask(__name__)
db=ms.connect(host='localhost',user='root',password='dpsbn',database='cars')
cursor=db.cursor()
@app.route('/get_coordinates/<bus_id>')
def get_coordinates(bus_id):
    long_query = 'SELECT longitude FROM buses WHERE bus_id=%s'
    lati_query = 'SELECT latitude FROM buses WHERE bus_id=%s'

    cursor.execute(long_query, (bus_id,))
    longitude = cursor.fetchall()

    cursor.execute(lati_query, (bus_id,))
    latitude = cursor.fetchall()

    if longitude:
        longitude = float(longitude[0][0])

    if latitude:
        latitude = float(latitude[0][0])

    return jsonify({"longitude": longitude, "latitude": latitude})

if __name__ == '__main__':
    app.run(debug=True)
