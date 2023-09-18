from car import Car
from faker import Faker
from faker_vehicle import VehicleProvider

fake = Faker()
fake.add_provider(VehicleProvider)

my_new_car = Car(fake.vehicle_make(), fake.vehicle_model(), fake.vehicle_year())

print(my_new_car.get_descriptive_name())
