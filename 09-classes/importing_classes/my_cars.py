from faker import Faker
from car import Car, ElectricCar
from faker_vehicle import VehicleProvider

fake = Faker()
fake.add_provider(VehicleProvider)

my_ev = ElectricCar(fake.vehicle_make(), fake.vehicle_model(), fake.vehicle_year())
print(my_ev.get_descriptive_name())
my_ev.battery.describe_battery()
my_ev.battery.get_range()

my_car = Car(fake.vehicle_make(), fake.vehicle_model(), fake.vehicle_year())
print(my_car.get_descriptive_name())
