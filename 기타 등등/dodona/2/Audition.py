# https://dodona.ugent.be/en/activities/1745983456/

class Heater:
    def __init__(self, name, temperature=10.0, minimum=0.0, maximum=100.0):
        self.name = name
        self.temp = float(temperature)
        self.minimum = float(minimum)
        self.maximum = float(maximum)

    def __str__(self):
        return f"{self.name}: current temperature: {round(self.temp, 1)}; allowed min: {self.minimum}; allowed max: {self.maximum}"

    def __repr__(self):
        return f"Heater('{self.name}', {self.temp}, {self.minimum}, {self.maximum})"

    def change_temperature(self, num):
        self.temp = self.temp+num if self.minimum < self.temp+num < self.maximum else (self.minimum if 1 else self.maximum)

    def temperature(self): return self.temp


if __name__ == '__main__':
    machine1 = Heater('radiator kitchen', temperature=20)
    machine2 = Heater('radiator living', minimum=15, temperature=18)
    machine3 = Heater('radiator bathroom', temperature=22, minimum=18, maximum=28)
    print(machine1)
    print(machine2.__repr__())
    machine2.change_temperature(8)
    machine2.temperature()
    machine3.change_temperature(-5)
    print(machine3.__repr__())
