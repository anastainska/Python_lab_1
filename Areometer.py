from MeasureInstrument import MeasureInstrument


class Areometer(MeasureInstrument):
    def __init__(self, price, country, material, producer, measure_time, height_in_cm):
        super().__init__(price, country, material, producer, measure_time)
        self.height_in_cm = height_in_cm

    def __repr__(self):
        return repr((self.price, self.measure_time, self.producer, self.country,
                     self.height_in_cm))