class RegularPolygon:
    def __init__(self, n=3, side=1.0, x=0.0, y=0.0):
        self.n = n
        self.side = side
        self.x = x
        self.y = y

    def get_n(self):
        return self.n

    def get_side(self):
        return self.side

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_n(self, n):
        self.n = n

    def set_side(self, side):
        self.side = side

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y
    def getPerimeter(self):
        return self.n * self.side

    def getArea(self):
        # Area formula: (n * side^2) / (4*tan(pi/n))
        pi = 3.141592653589793
        angle = pi/self.n
        tan_value = angle+(angle**3)/3  #aproximatly
        return (self.n*self.side**2)/(4 * tan_value)
    
p1 = RegularPolygon()
p2= RegularPolygon(6,4)
p3= RegularPolygon(10,4,5.6,7.8)

print("Number of sides:", p1.get_n())
print("Length of a side:", p1.get_side())
print("Perimeter:", p1.getPerimeter())
print("Area:", p1.getArea())

print("Number of sides:", p2.get_n())
print("Length of a side:", p2.get_side())
print("Perimeter:", p2.getPerimeter())
print("Area:", p2.getArea())

print("Number of sides:", p3.get_n())
print("Length of a side:", p3.get_side())
print("X-coordinate of center:", p3.get_x())
print("Y-coordinate of center:", p3.get_y())
print("Perimeter:", p3.getPerimeter())
print("Area:",p3.getArea())