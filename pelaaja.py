from math import sin, cos, pi
from matikka import lerp, Vektori as V2
from inputti import Manageri
from kamera import Kamera
import tila

from entiteetti import Entiteetti
from asteroidi import Asteroidi

class Avaruusalus(Entiteetti):
    def __init__(self, paikka):
        Entiteetti.__init__(self, paikka)
        self.suunta = pi / 2
        self.nopeus = V2(0, 0)
        self.kulmanopeus = 0
        self.max_nopeus = 300
        self.max_kulmanopeus = 3
        self.kiihtyvyys = 0.2
        self.massa = 0.01
        self.pisteet = [V2(20, 0), V2(-10, 10), V2(-5, 0), V2(-10, -10)]
        self.koko = 10
        self.points = 0

    def collide(self, e):
        if type(e) == Asteroidi:
            tila.Tila.set(tila.AloitusTila())

    def update(self, delta):
        if Manageri.alhaalla_nappi(87):
            self.nopeus.x = lerp(self.nopeus.x, self.max_nopeus*cos(self.suunta), self.kiihtyvyys)
            self.nopeus.y = lerp(self.nopeus.y, self.max_nopeus*sin(self.suunta), self.kiihtyvyys)
        self.nopeus.x = lerp(self.nopeus.x, 0, self.massa)
        self.nopeus.y = lerp(self.nopeus.y, 0, self.massa)
        #if self.nopeus.x > -1 and self.nopeus.x < 1: self.nopeus.x = 0
        #if self.nopeus.y > -1 and self.nopeus.y < 1: self.nopeus.y = 0
        if Manageri.alhaalla_nappi(65):
            self.kulmanopeus = self.max_kulmanopeus
        elif Manageri.alhaalla_nappi(68):
            self.kulmanopeus = -self.max_kulmanopeus
        else:
            self.kulmanopeus = 0
        if Manageri.nyt_painettu_nappi(32):
            Kuti(self.paikka, self.suunta, self)
        self.paikka += self.nopeus * delta
        self.suunta += self.kulmanopeus * delta
        self.suunta = self.suunta % (2 * pi)

    def render(self, g):
        koordinaatit = []
        for piste in self.pisteet:
            a = piste.rotate(self.paikka, self.suunta)
            a = Kamera.muuta_koordinaatit(a)
            koordinaatit.append(a.x)
            koordinaatit.append(a.y)
        g.create_polygon(tuple(koordinaatit), outline="white")

class Kuti(Entiteetti):
    def __init__(self, paikka, suunta, o):
        Entiteetti.__init__(self, paikka)
        v = 1000
        self.koko = 1
        self.nopeus = V2(v*cos(suunta), v*sin(suunta))
        self.age = 0
        self.o = o

    def update(self, delta):
        self.age += delta
        if self.age > 5:
            self.remove()
        self.paikka += self.nopeus * delta

    def render(self, g):
        p = Kamera.muuta_koordinaatit(self.paikka)
        k = self.koko
        g.create_oval(p.x-k, p.y-k, p.x+k, p.y+k, outline="white", fill="white")
