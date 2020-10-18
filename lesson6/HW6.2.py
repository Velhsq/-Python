class Road:

    def __init__(self, height, weight):
        if type(height) == int and type(weight) == int:
            self._height = height
            self._weight = weight
        else:
            raise TypeError('параметры должны быть типа int')
        self._centimeter_asphalt_mass = 25
        self._asphalt_thickness = 5

    def asphalt_mass_calculation(self):
        self.asphalt_mass = self._height * \
                            self._weight * \
                            self._centimeter_asphalt_mass * \
                            self._asphalt_thickness
        return self.asphalt_mass


ap = Road(1000, 10)
print(ap.asphalt_mass_calculation())