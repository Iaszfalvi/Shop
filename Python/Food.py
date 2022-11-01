class MyFood(object):

    def __init__(self, name, amount, calories, price, rating):
        self.name = name
        self.amount = amount
        self.calories = calories
        self.price = price
        self.rating = rating

    def getName(self):
        return self.name



    def wasthishealthy(self):

        if self.calories  > 1000:
            print("No")