from math import sin, cos

def lerp(a, b, t):
    return a * (1 - t) + (b * t)


class Vektori:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)"%(self.x, self.y)

    def __add__(a, b):
        return Vektori(a.x + b.x, a.y + b.y)

    def __sub__(a, b):
        return Vektori(a.x - b.x, a.y - b.y)

    def __mul__(a, b):
        if type(b) == int or type(b) == float:
            return Vektori(a.x * b, a.y * b)

    def __truediv__(a, b):
        if type(b) == int or type(b) == float:
            return Vektori(a.x / b, a.y / b)

    def __floordiv__(a, b):
        if type(b) == int or type(b) == float:
            return Vektori(a.x / b, a.y / b)

    def rotate(self, piste, kulma):
        #return Vektori(self.x * cos(kulma) - self.y * sin(kulma), self.y * cos(kulma) + self.x * sin(kulma))
        return Vektori(self.x * cos(kulma) - self.y * sin(kulma) + piste.x, self.x * sin(kulma) + self.y * cos(kulma) + piste.y)
