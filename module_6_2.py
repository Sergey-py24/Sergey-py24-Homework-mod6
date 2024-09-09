
class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black']
    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power} л.с.'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def set_color(self, new_color: str):
        if new_color.lower() in self.__COLOR_VARIANTS:
            self.__color == new_color
        else:
            print(f'Нельзя перекрасить на {new_color}')

    def print_info(self):
        print (self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print (f'Владелец: {self.owner}')

class Sedan(Vehicle):
    _PASSENGER_lIMIT = 3



vehicle1 = Sedan('Ст.пр-к Иванов', 'Т-14 Армата', 1000, 'green')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Рядовой Петров'
vehicle1.print_info()