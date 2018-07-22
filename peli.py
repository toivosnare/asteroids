from tkinter import Tk, Canvas, BOTH
from time import time, sleep
from inputti import Manageri
import tila
from kamera import Kamera
from matikka import Vektori as V2

class Peli:
    nimi = "Asteroids"
    versio = 0.1
    koko = V2(640, 480)
    f = 30
    stop = False
    #muuttuja = "ei toimi"

    @classmethod
    def start(cls):
        cls.ikkuna = Tk()
        cls.ikkuna.protocol("WM_DELETE_WINDOW", cls.close)
        cls.ikkuna.title(cls.nimi + " " + str(cls.versio))
        cls.ikkuna.bind("<KeyPress>", Manageri.down)
        cls.ikkuna.bind("<KeyRelease>", Manageri.up)
        cls.g = Canvas(cls.ikkuna, width=cls.koko.x, height=cls.koko.y, bg="black")
        cls.g.pack(fill=BOTH, expand=1)
        #Peli.muuttuja = "toimii"
        tila.Tila.set(tila.AloitusTila())

        viime = time()
        while not cls.stop:
            nyt = time()
            delta = nyt - viime
            viime = nyt
            cls.update(delta)
            if not cls.stop:
                cls.render(cls.g)
                sleep(1 / cls.f)
            #print(delta)
        cls.ikkuna.destroy()
        tila.Tila.tclose()
        

    @classmethod
    def close(cls):
        cls.stop = True
        #print(Peli.muuttuja)

    @classmethod
    def update(cls, delta):
        Manageri.update()
        cls.ikkuna.update()
        tila.Tila.tupdate(delta)

    @classmethod
    def render(cls, g):
        g.delete("all")
        tila.Tila.trender(g)

if __name__ == '__main__':
    Peli.start()
