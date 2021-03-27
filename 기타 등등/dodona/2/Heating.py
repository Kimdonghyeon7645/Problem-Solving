# https://dodona.ugent.be/en/activities/1745983456/

class Heater:
    def __init__(self, name, temperature=10.0, minimum=0.0, maximum=100.0):
        # 인자=값 : 디폴트 인자라고 해서, 함수 호출시 인자값을 넘겨주지 않으면 여기서 대입해준 값으로 변수의 값을 저장할 수 있습니다.
        # -> 말그대로 매개변수에 값을 넘겨주지 않았을 때 가지고 있게될, '매개변수의 기본값' 입니다.
        self.name = name
        self.temp = float(temperature)
        self.minimum = float(minimum)
        self.maximum = float(maximum)

    # f string : f"" 와 같이 문자열 앞에 f를 붙이면, {} 안에 변수명을 넣어 변수의 값을 문자열에 포함시킬 수 있습니다.
    def __str__(self): return f"{self.name}: current temperature: {round(self.temp, 1)}; allowed min: {self.minimum}; allowed max: {self.maximum}"
    def __repr__(self): return f"Heater('{self.name}', {self.temp}, {self.minimum}, {self.maximum})"
    def temperature(self): return self.temp

    def change_temperature(self, num):
        self.temp = self.temp+num if self.minimum < self.temp+num < self.maximum else (self.minimum if self.temp+num < self.minimum else self.maximum)


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
