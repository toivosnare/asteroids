from random import randint
from matikka import Vektori as V2
from kamera import Kamera
from entiteetti import Entiteetti
import pelaaja


class Asteroidi(Entiteetti):
    pienin_koko = 20
    suurin_koko = 80

    def __init__(self, paikka, koko, nopeus):
        Entiteetti.__init__(self, paikka)
        self.koko = koko
        self.nopeus = nopeus
        self.color = "white"

    def collide(self, e):
        if type(e) == pelaaja.Kuti:
            e.o.points += 1
            e.remove()
            uusi_koko = self.koko/2
            if uusi_koko >= Asteroidi.pienin_koko:
                Asteroidi(self.paikka, uusi_koko, self.nopeus)
            else:
                Asteroidi(V2(randint(-320, 320), randint(-240, 240)), Asteroidi.suurin_koko, V2(0, 0))
            self.remove()

    def update(self, delta):
        self.paikka += self.nopeus * delta

    def render(self, g):
        p = Kamera.muuta_koordinaatit(self.paikka)
        g.create_oval(p.x-self.koko, p.y-self.koko, p.x+self.koko, p.y+self.koko, outline=self.color)