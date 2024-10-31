import math

lat_one = float(input("input the latitude of coordinate 1: "))
lon_one = float(input("input the longitude of coordinate 1: "))
lat_two = float(input("input the latitude of coordinate 2: "))
lon_two = float(input("input the longitude of coordinate 2: "))

Radius_of_earth = 6371.01

lat_one = math.radians(lat_one)
lon_one = math.radians(lon_one)
lat_two = math.radians(lat_two)
lon_two = math.radians(lon_two)

distance = Radius_of_earth * math.acos(math.sin(lat_one) * math.sin(lon_one) + math.cos(lat_one) * math.cos(lon_one) * math.cos(lat_two - lon_two))

print(f"The distance between those points is: {distance: .13f} km")