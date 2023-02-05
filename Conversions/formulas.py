class Formula:
    mk = 0

    def __init__(self, mk):
        self.mk = mk

    # Feet to Cebtimeters
    def FtoC(self, mk):
        # F = (9/5 * C) + 32
        return float((mk - 32) * 5 / 9)

    # Centimeters to feet
    def CtoF(self, mk):
        # (xC * 5/9) + 32
        f = (mk - 32) * (5 / 9)
        return (mk - 32) * (5 / 9)

    # Miles to Kiometers
    def MiToKm(self, mk):
        # 1km = 0.621371192237334Mi
        return mk * 0.621371192237334

    # Killometers to Miles
    def KmToMi(self, mk):
        # 1mi = .621371192237
        return mk * 0.621371192237

    # Inch to Meters
    def ItoM(self, mk):
        # 1 in = 25.4 mm
        return mk * 25.4

    # Meters to Inch
    def MtoI(self, mk):
        # 1 mm = 0.03937007874 in 3/64
        return mk * 0.03937007874

    # Centimeters to Inch
    def CentToInch(self, mk):
        # 1 cent = 0.39 inch
        return float(mk) * 0.39

    # Inch to Centimeters
    def InchToCent(self, mk):
        # 1 inch = 2.54 centimeters
        return float(mk) * 2.54

    # Feet to Meters
    def FtToMt(self, mk):
        # 1 foot = 0.3048
        return mk * 0.3048

    # Meters to feet
    def MtToFt(self, mk):
        # 1 meter = 3.28083
        return mk * 3.28083

    # Millimeter to inch
    # 1mm/ 25.4 (3/64th) = 0.03937007874 in 3/6 inches
    def MilToInch(self, mk):
        return mk / 25.04

    # Inch to Millimeter
    def InchToMil(self, mk):
        return mk * 25.4

    # Kilograms to Pounds
    def kgToPound(self, mk):
        return mk * 0.45359237

    # Pounds to Kilograms
    def PoundToKg(self, mk):
        return mk / 0.45359237


class BMICalc:


    def __init__(self):
        self.wt = 0.00
        self.ht = 0.00

    def BMI(self, wt, ht, ht2):

        self.wt = wt
        self.ht = ht/0.0453595
        self.ht2 = ht2/0.0453595

        return (self.wt / self.ht**2) * 703
