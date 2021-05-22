from main import MeasureInstrument

class Thermometer(MeasureInstrument):
    def __init__(self, price, country, material, producer, measure_time, max_temp, kind):
        super().__init__(price, country, material, producer, measure_time)
        self.max_temp = max_temp
        self.kind = kind

    def __repr__(self):
        return repr((self._MeasureInstrument__price, self.measure_time, self.producer, self.country,
                     self.max_temp, self.kind))