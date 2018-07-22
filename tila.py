from random import randint
from math import pi
from matikka import Vektori as V2
from gkl import GKL, Teksti, Nappi
from inputti import Manageri
from kamera import Kamera
from testi import Merkki
import peli
import pelaaja
from entiteetti import Entiteetti
from asteroidi import Asteroidi

class Tila:
    nykyinen_tila = None

    @classmethod
    def set(cls, uusi_tila):
        vanha_tila = cls.nykyinen_tila
        if vanha_tila is not None:
            vanha_tila.close(uusi_tila)
        cls.nykyinen_tila = uusi_tila
        cls.nykyinen_tila.open(vanha_tila)

    @classmethod
    def tupdate(cls, delta):
        cls.nykyinen_tila.update(delta)

    @classmethod
    def trender(cls, g):
        cls.nykyinen_tila.render(g)

    @classmethod
    def tclose(cls):
        cls.nykyinen_tila.close(None)

    def open(self, vanha_tila):
        print("Avataan tila: " + str(type(self)))

    def update(self, delta):
        pass

    def render(self, g):
        pass

    def close(self, uusi_tila):
        print("Suljetaan tila: " + str(type(self)))

class PeliTila(Tila):
    def open(self, vanha_tila):
        Merkki(V2(0, 0))
        Asteroidi(V2(randint(-320, 320), randint(-240, 240)), Asteroidi.suurin_koko, V2(0, 0))
        self.a = pelaaja.Avaruusalus(V2(0, 0))
        #self.t1 = Teksti(V2(0, 0), "", "Arial 12", "white", "nw")
        #self.t2 = Teksti(V2(peli.Peli.koko.x, 0), "", "Arial 12", "white", "ne")
        Kamera.koko = peli.Peli.koko
        Kamera.paikka = V2(0, 0)

    def update(self, delta):
        Kamera.update(delta)
        Entiteetti.eupdate(delta)
        Kamera.paikka = self.a.paikka
        #self.t1.set("(" + "%.0f" % self.a.paikka.x + ", " + "%.0f" % self.a.paikka.y + "), (" + "%.0f" % (self.a.suunta * 180 / pi) + ")")
        #self.t2.set("%.2f" % Kamera.zoom + ", (" + "%.0f" % Kamera.paikka.x + ", " + "%.0f" % Kamera.paikka.y + ")")
        #GKL.gupdate(delta)

    def render(self, g):
        Entiteetti.erender(g)
        #GKL.grender(g)

    def close(self, uusi_tila):
        Entiteetti.eclose()
        #GKL.gclose()

class ValikkoTila(Tila):
    def update(self, delta):
        GKL.gupdate(delta)

    def render(self, g):
        GKL.grender(g)

    def close(self, uusi_tila):
        GKL.gclose()

class AloitusTila(ValikkoTila):
    def open(self, vanha_tila):
        Teksti(V2(peli.Peli.koko.x/2, 100), peli.Peli.nimi, "Arial 48", "white", "center")
        GKL.fokus = Nappi(V2(peli.Peli.koko.x/2, 200), "Pelaa", V2(120, 40), lambda: Tila.set(PeliTila()))
        Nappi(V2(peli.Peli.koko.x/2, 250), "Asetukset", V2(120, 40), lambda: Tila.set(AsetuksetTila()))
        Nappi(V2(peli.Peli.koko.x/2, 300), "Lopeta", V2(120, 40), peli.Peli.close)

class AsetuksetTila(ValikkoTila):
    def open(self, vanha_tila):
        Teksti(V2(peli.Peli.koko.x/2, 100), "Asetukset", "Arial 36", "white", "center")
        GKL.fokus = Nappi(V2(peli.Peli.koko.x/2, peli.Peli.koko.y-60), "Takaisin", V2(100, 40), lambda: Tila.set(AloitusTila()))

class TestiTila(Tila):
    def open(self, vanha_tila):
        peli.Peli.close()