class Mobile:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
m1 = Mobile("Xiaomi", 27500)
m2 = Mobile("Samsung", 36000)

print(m1.brand,"\t",m2.brand)
print(m1.price,"\t",m2.price)
