class Mobile:
    def __init__ (self,brand,battery,ram,price):
        self.brand=brand
        self.battery=battery
        self.ram=ram
        self.price=price
    def display(self):
        print("brand:", self.brand)
        print("battery:",self.battery)
        print("ram:", self.ram)
        print("price:", self.price)
        print("-------------------")
for i in range(5):     # this line to use more number of time to ittrate or print
    object = Mobile("apple",'400mbh','8gb','15000') 
    object.display()   