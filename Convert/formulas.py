class Formula:
    def __init__(self):
        self.unit = 6500

    def FtoC(self):
        # F = (9/5 * C) + 32
        f = self.unit
        return (f - 32) * 5 / 9

    def CtoF(self):
        # (xC * 5/9) + 32
        c = self.unit
        return (c * 5 / 9) + 2


frm1 = Formula()
print(frm1.FtoC())
print(frm1.CtoF())
