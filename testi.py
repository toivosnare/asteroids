from entiteetti import Entiteetti
from kamera import Kamera

class Merkki(Entiteetti):
    def render(self, g):
        r = 2
        p = Kamera.muuta_koordinaatit(self.paikka)
        g.create_oval(p.x-r, p.y-r, p.x+r, p.y+r, outline="white", fill="white")

    def update(self, delta):
        pass