"""
2)Airplane
Создайте новый класс Airplane. Создайте следующие характеристики (полей)
объекAта:
● make (марка)
● model
● year
● max_speed
● odometer
● is_flying
и методы имитирующих поведение самолета take off (взлет), fly (летать), land
приземление). Метод take off должен изменить is_flying на True, а land на False. По
умолчанию поле is_flying = False. Метод fly должен принимать расстояние полета и
изменять показания одометра (километраж). Создайте 1 объект класса и используйте
все методы класса.
"""

class Airplane():
    """ Класс описанния Самолета """
    def __init__(self, make, model, bort_number, year, max_speed, is_flying = False):
        self.make = make
        self.model = model
        self.bort_number = bort_number
        self.year = year
        self.max_speed = max_speed
        self.odometer = 0
        self.is_flying = is_flying
    
    
    def __str__(self):
        return f"Общая информация о самолёте: \n Марка: {self.make} \n Модель: {self.model} \n Борт-номер: {self.bort_number}  "
    
    
    def take_off(self):
        print(f"Самолет борт-номер {self.bort_number} марки {self.make.title()}, пошёл на взлёт")
        self.is_flying = True
        print(f"is_flying = {self.is_flying}")
    
    
    def fly(self, rasstoyanie):
        """полёт самолета, при вызове ф-ции необходимо указать расстояние
        rasstoyanie ==> int
         """
        self.odometer += rasstoyanie
        print(f"Самолёт находится в полете, пройденное расстояние {self.odometer}км. ")

    
    def land(self):
        print(f"Самолёт борт-номер:{self.bort_number} пошел на посадку, общее расстояние которое пролетел самолёт: {self.odometer} км.")
        self.is_flying = False
        print(f"is_flying = {self.is_flying}")


plane_1 = Airplane('Boing', 737, 'Na12345', 2015, 900, 0 )
print(plane_1)


plane_1.take_off()
plane_1.fly(6)
plane_1.fly(100)
plane_1.fly(333)
plane_1.land()