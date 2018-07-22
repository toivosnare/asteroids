from matikka import Vektori as V2
from inputti import Manageri

class Kamera:
    paikka = V2(0, 0)
    suunta = 0
    nopeus = V2(0, 0)
    kulmanopeus = 0
    max_nopeus = 100
    max_kulmanopeus = 10
    zoom = 1
    zoomnopeus = 0
    max_zoomnopeus = 0.1
    koko = V2(640, 480)

    @classmethod
    def update(cls, delta):
        if Manageri.alhaalla_nappi(37):
            cls.nopeus.x = -cls.max_nopeus
        elif Manageri.alhaalla_nappi(39):
            cls.nopeus.x = cls.max_nopeus
        else:
            cls.nopeus.x = 0
        if Manageri.alhaalla_nappi(38):
            cls.nopeus.y = cls.max_nopeus
        elif Manageri.alhaalla_nappi(40):
            cls.nopeus.y = -cls.max_nopeus
        else:
            cls.nopeus.y = 0
        if Manageri.alhaalla_nappi(33):
            cls.zoomnopeus = cls.max_zoomnopeus
        elif Manageri.alhaalla_nappi(34):
            cls.zoomnopeus = -cls.max_zoomnopeus
        else:
            cls.zoomnopeus = 0

        cls.paikka += cls.nopeus * delta
        cls.suunta += cls.kulmanopeus * delta
        cls.zoom += cls.zoomnopeus * delta
        #print(str(cls.paikka))

    @classmethod
    def vanha_muuta_koordinaatit(cls, toinen):
        return V2(cls.paikka.x + cls.zoom*toinen.x, cls.paikka.y + cls.zoom*toinen.y)
        #return cls.paikka - toinen

    @classmethod
    def muuta_koordinaatit(cls, toinen):
        return V2(toinen.x - cls.paikka.x + cls.koko.x/2, -toinen.y + cls.paikka.y + cls.koko.y/2)