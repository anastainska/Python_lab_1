from enum import Enum


class MeasureInstrument:
    def __init__(self, price, country, material, producer, measure_time):
        self.price = price
        self.country = country
        self.material = material
        self.producer = producer
        self.measure_time = measure_time

    def __repr__(self):
        return repr(
            (self.price, self.measure_time, self.producer, self.country))


class Country(Enum):
    China = 1
    Ukraine = 2
    Germany = 3


class Kind(Enum):
    Digital = 1
    Oral = 2
    Forehead = 3
    Mercury = 4
    Pacifier = 5
    Digital_ear = 6


class Material(Enum):
    Glass = 1
    Metal = 2
    Plastic = 3

