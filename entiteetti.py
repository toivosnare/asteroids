from math import sqrt
from random import randint
from matikka import Vektori as V2
from kamera import Kamera

class Entiteetti(object):
    lista = []

    def __init__(self, paikka):
        Entiteetti.lista.append(self)
        self.paikka = paikka
        self.koko = 0

    def collide(self, e):
        pass

    def remove(self):
        Entiteetti.lista.remove(self)

    def update(self, delta):
        print(delta)

    def render(self, g):
        g.create_rectangle(self.paikka.x, self.paikka.y, self.paikka.x+20, self.paikka.y+20, fill="red")

    @classmethod
    def eupdate(cls, delta):
        for e in cls.lista:
            e.update(delta)
            for f in cls.lista:
                if sqrt((f.paikka.x - e.paikka.x)**2 + (-f.paikka.y + e.paikka.y)**2) < f.koko + e.koko and e is not f:
                    e.collide(f)

    @classmethod
    def erender(cls, g):
        for e in cls.lista:
            e.render(g)

    @classmethod
    def eclose(cls):
        cls.lista.clear()