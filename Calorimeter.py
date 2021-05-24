from MeasureInstrument import MeasureInstrument


class Calorimeter(MeasureInstrument):
    def __init__(self, price, country, material, producer, measure_time, max_heat):
        super().__init__(price, country, material, producer, measure_time)
        self.max_heat = max_heat

    def __repr__(self):
        return repr((self.price, self.measure_time, self.producer, self.country,
                     self.max_heat))