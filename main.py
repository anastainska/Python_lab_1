from Manager import *
from Areometer import Areometer
from Calorimeter import Calorimeter
from Thermometer import Thermometer


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

    manager = MeasureInstrumentManager(areometer_objects + calorimeter_objects + thermometer_objects)
    found_by_producer = manager.search_by_producer("Willi Wonka")

    print("--------------Sorted-----------------")

    sorted_by_price_asc = manager.sort_by_price(SortOrder.ASC)
    print(sorted_by_price_asc)

    sorted_by_price_desc = manager.sort_by_price(SortOrder.DESC)
    print(sorted_by_price_desc)

    print("-------------------------------------")

    print(found_by_producer)

    print("-------------------------------------")



if __name__ == "__main__":
    main()
