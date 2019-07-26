# 1)Класс автомобиля
class Avto():
    _seats = 4
    _wheels = 4
    _color = 'red'

    def get_seats(self):
        return self._seats
    def get_wheels(self):
        return self._wheels
    def get_color(self):
        return self._color

    def ispravna(self):
        print('Машина исправна')

class Legkovoy(Avto):
    _color = "green"
    _toplevo = "газ"
    def ispravna(self):
        print('Машина не исправна')
    def get_toplevo(self):
        return self._toplevo

class Gruzovoy(Avto):
    _toplevo = "бензин"
    def get_toplevo(self):
        print("Грузовой")
        return self._toplevo

auto = Avto()
print(auto.__class__)
print(auto.get_seats())
print(auto.get_wheels())
print(auto.get_color())
auto.ispravna()
print("_____________________________")

legkovoy = Legkovoy()
print(legkovoy.__class__)
print(legkovoy.get_seats())
print(legkovoy.get_wheels())
print(legkovoy.get_color())
print(legkovoy.get_toplevo())
legkovoy.ispravna()

print("_____________________________")

gruzovoy = Gruzovoy()
print(gruzovoy.get_toplevo())
print(gruzovoy.get_color())
print(gruzovoy.ispravna())


