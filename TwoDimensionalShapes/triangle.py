import math
from GeometricFigures import TwoDimensionalShape

class Triangle(TwoDimensionalShape):
    def __init__(self, a, b, c):
        if not all([a+b > c, a+c > b, b+c > a]):
            raise Exception("NOT A TRIANGLE. Please provide valid triangle sides.")
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        half_perimeter = self.get_perimeter()/2
        return math.sqrt(half_perimeter*(half_perimeter-self.a)*(half_perimeter-self.b)*(half_perimeter-self.c))

    def get_perimeter(self):
        return self.a+self.b+self.c