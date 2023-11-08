class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.available_spaces = capacity
        self.base_price = 10

    def check_availability(self):
        return self.available_spaces

    def calculate_price(self):
        return self.base_price + (self.capacity - self.available_spaces) * 2

    def park_vehicle(self):
        if self.available_spaces > 0:
            self.available_spaces -= 1
            return True
        else:
            return False

    def leave_parking(self):
        if self.available_spaces < self.capacity:
            self.available_spaces += 1
            return True
        else:
            return False


class User:
    def __init__(self, name, vehicle_number):
        self.name = name
        self.vehicle_number = vehicle_number


class ParkingSystem:
    def __init__(self):
        self.parking_lot = ParkingLot(20)
        self.users = []

    def add_user(self, user):
        self.users.append(user)

    def park_vehicle(self, user):
        if user in self.users:
            if self.parking_lot.park_vehicle():
                return f'{user.name} parked. Price: {self.parking_lot.calculate_price()}'
            else:
                return f'{user.name} could not park. Parking full.'
        else:
            return f'User {user.name} not registered.'

    def leave_parking(self, user):
        if user in self.users:
            if self.parking_lot.leave_parking():
                return f'{user.name} left. Available spaces: {self.parking_lot.check_availability()}'
            else:
                return f'No vehicle to leave.'
        else:
            return f'User {user.name} not registered.'


def main():
    parking_system = ParkingSystem()

    user1 = User('John Doe', 'ABC123')
    user2 = User('Jane Doe', 'DEF456')

    parking_system.add_user(user1)
    parking_system.add_user(user2)

    # Simulate vehicles entering and leaving the parking lot
    print(parking_system.park_vehicle(user1))
    print(parking_system.park_vehicle(user2))
    print(parking_system.park_vehicle(User('Bob Smith', 'GHI789')))  # Not registered

    print(parking_system.leave_parking(user1))
    print(parking_system.leave_parking(user2))
    print(parking_system.leave_parking(User('Alice Johnson', 'JKL012')))  # Not registered


if __name__ == "__main__":
    main()
