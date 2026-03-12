class SmartPhone:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def call(self, phone_number):
        print(f"{self.color} {self.brand} phone, calling {phone_number}")

my_phone = SmartPhone("Apple", "black")
my_phone.call("110")