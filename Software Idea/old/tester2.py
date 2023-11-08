import mysql.connector

# Connect to MySQL database
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='dpsbn',
    database='hk'
)

# Create a cursor to interact with the database
cursor = db_connection.cursor()

# Define the Bus class
class Bus:
    def __init__(self, bus_id, emission_compliance, fuel_type):
        self.bus_id = bus_id
        self.emission_compliance = emission_compliance
        self.fuel_type = fuel_type
        self.current_location = None

    def update_location(self, latitude, longitude):
        self.current_location = (latitude, longitude)

    def save_to_database(self):
        query = "INSERT INTO buses (bus_id, emission_compliance, fuel_type) VALUES (%s, %s, %s)"
        values = (self.bus_id, self.emission_compliance, self.fuel_type)
        cursor.execute(query, values)
        db_connection.commit()

# Create a BusDatabase class
class BusDatabase:
    def add_bus(self, bus):
        bus.save_to_database()

    def get_bus(self, bus_id):
        query = "SELECT * FROM buses WHERE bus_id = %s"
        cursor.execute(query, (bus_id,))
        result = cursor.fetchone()
        if result:
            return Bus(result[0], result[1], result[2])
        else:
            return None

if __name__ == "__main__":
    # Prompt user for bus details
    bus_id = input("Enter Bus ID: ")
    emission_compliance = input("Enter Emission Compliance: ")
    fuel_type = input("Enter Fuel Type: ")

    # Create a bus database object
    bus_db = BusDatabase()

    # Add buses to the database
    bus = Bus(bus_id, emission_compliance, fuel_type)
    bus_db.add_bus(bus)

    # Simulate updating bus locations
    latitude = float(input("Enter Latitude: "))
    longitude = float(input("Enter Longitude: "))
    bus.update_location(latitude, longitude)

    # Get information about a bus
    bus_info = bus_db.get_bus(bus_id)
    if bus_info:
        print("Bus Info:")
        print(f"Bus ID: {bus_info.bus_id}")
        print(f"Emission Compliance: {bus_info.emission_compliance}")
        print(f"Fuel Type: {bus_info.fuel_type}")
        print(f"Current Location: {bus_info.current_location}")
    else:
        print("Bus not found")

# Close the database connection
cursor.close()
db_connection.close()
