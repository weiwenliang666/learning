class Car():
    def __init__(self,make,model,year):
        """初始化car的类"""
        self.make = make
        self.model = model
        self.year = year



    def infomation(self):
        """返回整洁的信息"""
        long_name = str(self.year) + ' ' + self.make + self.model
        return long_name.title()


my_car = Car('BMW','X5',2016)
print (my_car.infomation())

