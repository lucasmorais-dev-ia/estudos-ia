from dataclasses import dataclass


@dataclass
class City:
    name: str
    latitude: float
    longitude: float


cuiaba = City("Cuiabá", -15.60, -56.10)
print(cuiaba.name)
print(cuiaba)

cities = [
    City("Sinop", -11.86, -55.50),
    City("Cuiabá", -15.60, -56.10),
]

for city in cities: 
    print(f"{City.name}: {City.latitude}")