# 1. შექმენი ტრანსპორტის კლასი მინიმუმ 4 კლასის პარამეტრით
# 2. დაამატე ერთი სტატიკური მეთოდი.
# 3. დაამატე ორი კლასის მეთოდი.
# 4. დაამატე __init__ magic მეთოდი და მინიმუმ 3 ობიექტის
# პარამეტრი.
# 5. დაამატე მინიმუმ 2, ობიექტის მეთოდი.
# 6. დაამატე __repr__ magic მეთოდი
# 7. ზემოხსენებული კლასისგან შექმენი მინიმუმ 5 ობიექტი და
# გამოიძახე მისი ზოგიერთი მეთოდი და პარამეტრი.



class Transport:
    speed = 120
    color = 'Red'
    fuel_type = 'Petrol'
    current_location = 'Home'

    def __init__(self, mode, capacity, destination):
        self.mode = mode
        self.capacity = capacity
        self.destination = destination

    def __repr__(self):
        return f'This is a {self.mode}'

    @staticmethod
    def is_operational():
        print("This transport is operational!")

    
    @classmethod
    def show_color(cls):
        print(f"Transport color is: {cls.color}")


    @classmethod
    def show_speed_and_location(cls):
        print(f"Transport current location is {cls.current_location} and speed is {cls.speed}")


    def move_to(self, new_location):
        self.current_location = new_location
        print(f"The {self.mode} is moving to {new_location}.")


    def stop(self):
        print(f"The {self.mode} is stopping.")



car = Transport('Car', 5, 'Office')
car.show_color()
car.show_speed_and_location()
car.move_to('School')
car.stop()
print()

bus = Transport('Bus', 25, 'School')
bus.is_operational()
bus.move_to('School')
print()

bike = Transport('Bike', 2, 'Square')
print(bike)
bike.move_to('Square')
print()

lorry = Transport('Lorry', 3, 'Shopping center')
print(lorry)
lorry.show_color()
lorry.stop()
print()

helicopter = Transport('Helicopter', 4, 'Tbilisi')
helicopter.move_to('Tbilisi')
helicopter.stop()
