
# carpark_classes.py
# Commit 2 - Added this comment for the Git assessment
''' 
Author: Mae Rockall
Student ID: 20147995
Email: 20147995@tafe.education.wa.edu.au

Resource used to help make classes: - https://www.w3schools.com/python/python_classes.asp
                                    - https://realpython.com/python3-object-oriented-programming/
'''

# The car class is a car using the parking system.
# It stores the license plate number so we can know the cars that enter and exit the carpark.
# step 1 make car class
class Car:
    # Step 2 set parameters, it should have licence number to identify cars.
    def __init__(self, license_plate):
        self.license_plate = license_plate
    # step 3 display car 
    # Resource used https://www.digitalocean.com/community/tutorials/python-str-repr-functions
    def __str__(self):
        return f"Car({self.license_plate})"


# The parking bay class is a parking spot in the carpark.
# It can be occupied or free, and can hold a Car object if one is parked there.
# Step 1 Make a class for the parking bay
class ParkingBay:
    # Step 2 set the paremeters, it should be either occupied or not and identfy what bay it is.
    def __init__(self, bay_id, occupied=False, car=None):
        # id for each parking bay
        self.bay_id = bay_id 
        # Shows if the bay is in use 
        self.occupied = occupied
        # If a car is parked in this bay
        self.car = car 

    # assign a car to this parking bay and marks it as occupied
    def assign_car(self, car):
        self.car = car
        self.occupied = True

    # when cars leave the parking bay the car is unassigned and the bay is now free
    def remove_car(self):
        self.car = None
        self.occupied = False

    # Display if the parking bay is free or occupied
    def __str__(self):
        return f"Bay {self.bay_id} {'Occupied' if self.occupied else 'Free'}"


# The CarPark class holds all parking bays and messages.
# It has method to park and remove cars, and to display messages.
class CarPark:
    def __init__(self, num_bays):
        # Create a list of parking bays, with an id.
        self.bays = [ParkingBay(number) for number in range(num_bays)]
        # A list of messages
        self.announcements = []

    # tries to park a car in the first avaulablebay
    def park_car(self, license_plate):
        for bay in self.bays:
            if not bay.occupied:
                bay.assign_car(Car(license_plate))
                return f"Car {license_plate} parked in bay {bay.bay_id}"
            return "No bays available."

    # Searches for a car by license plate and removes it if found
    def remove_car_by_plate(self, license_plate):
        for bay in self.bays:
            if bay.occupied and bay.car.license_plate == license_plate:
                bay.remove_car()
                return f"Car {license_plate} removed from Bay {bay.bay_id}"
        return "Car not found."

    # Adds a message to the announcements list
    def add_announcement(self, message):
        self.announcements.append(message)

    # Shows available parking spaces and messages
    def __str__(self):
        bay_status = "\n".join(str(bay) for bay in self.bays)
        return f"CarPark Status:\n{bay_status}\nAnnouncements: {self.announcements}"
    
