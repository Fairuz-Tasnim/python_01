class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def getA(self):
        return self.a
    
    def getB(self):
        return self.b

    def getC(self):
        return self.c

    def getD(self):
        return self.d

    def getE(self):
        return self.e

    def getF(self):
        return self.f
    
    def isSolvable(self):
        return self.a * self.d - self.b * self.c != 0
    
    def getX(self):
        if self.isSolvable():
            return (self.e*self.d - self.b*self.f)/(self.a*self.d - self.b*self.c)
        else:
            return ("The equation has no solution.")
        
    def getY(self):
        if self.isSolvable():
            return (self.a * self.f - self.e * self.c) / (self.a * self.d - self.b * self.c)
        else:
            return("The equation has no solution.")

EL= LinearEquation(4,5,6,8,9,7)

# Check if the system is solvable
if EL.isSolvable():
    print("x =", EL.getX())
    print("y =", EL.getY())
else:
    print("The equation system has no solution.")

