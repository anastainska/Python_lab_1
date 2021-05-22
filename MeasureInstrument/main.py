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


def search_by_producer(list_of_objects):
    print("Введіть бажаного виробника: ")
    wanted_producer = input()

    for i in list_of_objects:
        if wanted_producer == i.producer:
            print(i)


def main():
    areometer_objects = [
        Areometer(100, 1, 3, "Willi Wonka", "00:47", 15),
        Areometer(256, 2, 1, "Fabryka", "00:25", 11),
        Areometer(56, 3, 2, "Deshevyky", "01:16", 21),
    ]

    calorimeter_objects = [
        Calorimeter(100, 1, 3, "Willi Wonka", "00:47", 15),
        Calorimeter(256, 2, 1, "Fabryka", "00:25", 11),
        Calorimeter(56, 3, 2, "Deshevyky", "01:16", 21),
    ]

    thermometer_objects = [
        Thermometer(100, 1, 3, "Willi Wonka", "00:47", 100, 4),
        Thermometer(256, 2, 1, "Fabryka", "00:25", 45, 2),
        Thermometer(56, 3, 2, "Deshevyky", "01:16", 39, 1),
        Thermometer(75, 4, 2, "slnfkls", "00:01", 89, 1),
    ]

    sorted(areometer_objects, key=lambda areometer: areometer.price)
    print(sorted)

    print("-------------------------------------")



    print("-------------------------------------")

    search_by_producer(thermometer_objects)


if __name__ == "__main__":
    main()
