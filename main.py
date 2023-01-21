
class AutoMobile:
    def __init__(self, nov):
        self.nov = nov
        #print("----Inside Automobile++")

    def m1():
        print('-----inside Automobile---')


class Bike(AutoMobile):

    def __init__(self):
        super().__init__()

    def m2():
        print("------inside Bike")

class Auto(AutoMobile):

    def __init__(self):
        super().__init__()

    def m2():
        print("------inside Bike")

class Car(AutoMobile):

    def __init__(self, nov, roof):
        super().__init__(nov)
        self.roof = roof
        #print("----inside Car=====")

    def m3():
        print('-----inside Car')




car = Car(4, False)
car2 = Car(6, True)

print(car.nov, car.roof)
print(car2.nov, car2.roof)

car2.