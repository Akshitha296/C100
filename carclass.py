class Car(object):
    def __init__(self, model, creationYear, colour, speed, mileage, month):
        self.model = model
        self.creationYear = creationYear
        self.colour = colour
        self.speed = speed
        self.mileage = mileage
        self.month = month or {}

    def getTireType(self, month):
        if (month == "January" or month == "February" or month == "March" or month == "April" or month == "December"):
            season = "Winter"
        else:
            season = "Normal"
        return season


car_1 = Car("Honda Civic", 2008, "Cherry Red", "Max 180 kmph", "20 kmpl", "March")

print(car_1.getTireType("March"))