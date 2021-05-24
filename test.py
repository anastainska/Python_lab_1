import unittest
from Thermometer import Thermometer
from Areometer import Areometer
from Calorimeter import Calorimeter
from Manager import *


class TestObject(unittest.TestCase):

    def test_object_creation(self):
        self.instrument = Thermometer(100, 1, 3, "Willi Wonka", "00:47", 100, 4)
        self.assertEqual(100, self.instrument.price)
        self.assertEqual(1, self.instrument.country)
        self.assertEqual(3, self.instrument.material)
        self.assertEqual("Willi Wonka", self.instrument.producer)
        self.assertEqual("00:47", self.instrument.measure_time)
        self.assertEqual(100, self.instrument.max_temp)
        self.assertEqual(4, self.instrument.kind)


class TestManager(unittest.TestCase):

    def setUp(self):
        self.areometer = Areometer(100, 1, 3, "Willi Wonka", "00:47", 15)
        self.calorimeter = Calorimeter(256, 2, 1, "Fabryka", "00:25", 11)
        self.thermometer = Thermometer(56, 3, 2, "Deshevyky", "01:16", 39, 1)
        instrument_objects = [
            self.areometer,
            self.calorimeter,
            self.thermometer,
        ]
        self.manager = MeasureInstrumentManager(instrument_objects)

    def test_search_by_producer(self):
        self.assertEqual(self.manager.search_by_producer("Willi Wonka"), [self.areometer])

    def test_sort_by_price(self):
        self.assertEqual(self.manager.sort_by_price(SortOrder.ASC), [self.thermometer, self.areometer, self.calorimeter])

    def test_sort_by_price(self):
        self.assertEqual(self.manager.sort_by_price(SortOrder.DESC), [self.calorimeter, self.areometer, self.thermometer])