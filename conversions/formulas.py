class Formula:
    def __init__(self):
        self.unit = 0

    def FtoC(self, unit):
            # F = (9/5 * C) + 32
            f = unit
            return (f - 32) * 5 / 9

    def CtoF(self,unit):
        # (xC * 5/9) + 32
        c = unit
        return (c * 5 / 9) + 2
