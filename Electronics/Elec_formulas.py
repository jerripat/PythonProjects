
class ohms_law():
    def __init__(self):
        self.name = 'ohms law'
        self.units = 'ohms'
        self.default_units = 'ohms'
        self.default_value = 0.0
        self.min_value = 0.0
        self.max_value = 1000.0
        self.step_size = 1.0
        self.decimals = 0
        self.description = 'The ohms law'

    # Resistance = v/i
    # Current = v/r
    # Voltage = i * r

    def get_resistor(self, i, v):
        return v/i

    def get_current(self, r, v):
        return v/r
    
    def get_voltage(self, i, r):
        i * r
