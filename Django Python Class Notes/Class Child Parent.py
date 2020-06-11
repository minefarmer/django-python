# continuing  lesson 54 with code from from Class Cars.py  line 40
#               changes start on line 69
#  continuing  lesson 55 with code from from Class Cars.py  line 90
#      
# 
# 
# 
# 
# 
# 
class Test():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_info(self):
        full_name = self.name + ' ' + str(self.age)
        print(full_name.title())
    
    
# class Test2(Test):
#     def __init__(self, name, age):
#         super().__init__(name, age)



# m = Test('ali', 33)
# m.print_info()  # Ali 33

# t2 = Test2('carl', 81)
# t2.print_info()  # carl 81









# continuing with code from from Class Cars.py
# class Car():
#     """ info car """
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.km_reading = 400
       
        
#     def get_des(self):
#         """ printing info in the output """
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
#         return long_name.title()
    
    
#     def read_km(self):
#         """ print info about km """
#         print('this car has ' + str(self.km_reading) + ' km on it.')  # this car has 400 km on it.
        
        
        
#     def update_km(self, km):
#         """update km """
#         if km >= self.km_reading:
#             self.km_reading = km
#         else:
#             print('you can\'t roll back on km')
        
# class  ElectricCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = 70
        
#     def des_battery(self):
#         """printing info about the battery"""
#         print('this car has ' + str(self.battery) + " kwh battery.")
#     def fill_gas(self):
#         print('this car doesn't need gas.)
        
# my_car = ElectricCar('tesla', 'model s', 2019)
# my_car.des_battery()  # this car has 70 kwh battery.
# # print(my_car.get_des())  # 2019 Tesla Model S







#   continuing  lesson 55 with code from from Class Cars.py
class Car():
    """ info car """
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.km_reading = 400
       
        
    def get_des(self):
        """ printing info in the output """
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model 
        return long_name.title()
    
    
    def read_km(self):
        """ print info about km """
        print('this car has ' + str(self.km_reading) + ' km on it.')  # this car has 400 km on it.
        
        
        
    def update_km(self, km):
        """update km """
        if km >= self.km_reading:
            self.km_reading = km
        else:
            print('you can\'t roll back on km')
        
class  ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()
        
    def des_battery(self):
        """printing info about the battery"""
        print('this car has ' + str(self.battery) + " kwh battery.")
    def fill_gas(self):
        print('this car doesn\'t need gas.')
        
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        """printing info about battery"""
        print('this car has a ' + str(self.battery_size) + ' kwh battery.')
my_car = ElectricCar('tesla', 'model s', 2016)
# my_car.battery.describe_battery()  #this car has a 70 kwh battery. 
# my_car.fill_gas()  # this car doesn't need gas.
test = Battery(80)
test.describe_battery()  # this car has a 80 kwh battery.