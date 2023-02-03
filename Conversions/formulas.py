class Formula:
    mk = 0

    def __init__(self, mk):
        self.mk = mk

    def FtoC(self, mk):
        # F = (9/5 * C) + 32
        return float((mk - 32) * 5 / 9)

    def CtoF(self, mk):
        # (xC * 5/9) + 32
        f = (mk - 32) * (5 / 9)
        return (mk - 32) * (5 / 9)

    def MiToKm(self, mk):
        # 1km = 0.621371192237334Mi
        return mk * 0.621371192237334

    def KmToMi(self, mk):
        # 1mi = .621371192237
        return mk * 0.621371192237

    def ItoM(self, mk):
        # 1 in = 25.4 mm
        return mk * 25.4

    def MtoI(self, mk):
        # 1 mm = 0.03937007874 in 3/64
        return mk * 0.03937007874

    def CentToInch(self, mk):
        # 1 cent = 0.39 inch
        return float(mk) * 0.39

    def InchToCent(self, mk):
        # 1 inch = 2.54 centimeters
        return float(mk) * 2.54

    def FtToMt(self, mk):
        # 1 foot = 0.3048
        return mk * 0.3048

    def MtToFt(self, mk):
        # 1 meter = 3.28083
        return mk * 3.28083
