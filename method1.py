# define class
class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print(self.name, self.price)

# create instance x
x = Food('milk', 150)
x.show()

# create instance y
y = Food('egg', 200)
y.show()

