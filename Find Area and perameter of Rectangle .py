class Rectangle:
    def __init__(self, width=1, height=2):
        self.width=width
        self.height=height
    def getArea(self):
        return self.width * self.height
    def getPerameter(self):
        return 2*(self.width+self.height)
R1= Rectangle(4,40)
R2=Rectangle(3.5,35.7)
print("First rectagle's area:")
print(R1.getArea())
print("First rectangle's perameter:")
print(R1.getPerameter())
print("Second rectangle's area:")
print(R2.getArea())
print("Second rectangle's perameter:")
print(R2.getPerameter())
    