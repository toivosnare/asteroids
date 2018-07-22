from inputti import Manageri

class GKL:
    gkl_lista = []
    fokus = None

    def __init__(self, voi_fokus):
        self.voi_fokus = voi_fokus
        GKL.gkl_lista.append(self)

    def remove(self):
        GKL.gkl_lista.remove(self)

    def update(self, delta):
        pass

    def render(self, g):
        pass

    @classmethod
    def gupdate(cls, delta):
        if Manageri.nyt_painettu_nappi(40):
            cls.muuta_fokus(False)
        if Manageri.nyt_painettu_nappi(38):
            cls.muuta_fokus(True)
        for gkl in cls.gkl_lista:
            gkl.update(delta)

    @classmethod
    def muuta_fokus(cls, takaperin):
        if cls.fokus:
            index = cls.gkl_lista.index(cls.fokus)
            lista = cls.gkl_lista[index+1:] + cls.gkl_lista[:index]
        else:
            lista = cls.gkl_lista
        if takaperin:
            lista = reversed(lista)
        for gkl in lista:
            if gkl.voi_fokus:
                cls.fokus = gkl
                return
        print("ei fokusoitavaa")

    @classmethod
    def grender(cls, g):
        for gkl in cls.gkl_lista:
            gkl.render(g)

    @classmethod
    def gclose(cls):
        cls.fokus = 0
        cls.gkl_lista.clear()

class Teksti(GKL):
    def __init__(self, paikka, teksti, fontti, color, anchor):
        GKL.__init__(self, False)
        self.paikka = paikka
        self.teksti = teksti
        self.fontti = fontti
        self.color = color
        self.anchor = anchor

    def set(self, teksti):
        self.teksti = teksti

    def render(self, g):
        g.create_text((self.paikka.x, self.paikka.y), text=self.teksti, font=self.fontti, fill=self.color, anchor=self.anchor)

class Nappi(GKL):
    def __init__(self, paikka, teksti, koko, funktio):
        GKL.__init__(self, True)
        self.paikka = paikka
        self.teksti = teksti
        self.koko = koko
        self.funktio = funktio

    def update(self, delta):
        if GKL.fokus == self and Manageri.nyt_painettu_nappi(13):
            self.paina()

    def render(self, g):
        if GKL.fokus == self:
            fill = "white"
            text = "black"
        else:
            fill = ""
            text = "white"
        g.create_rectangle(self.paikka.x-self.koko.x/2, self.paikka.y+self.koko.y/2, self.paikka.x+self.koko.x/2, self.paikka.y-self.koko.y/2, fill=fill, outline="white")
        g.create_text((self.paikka.x, self.paikka.y), text=self.teksti, font="Arial 16", fill=text, anchor="center")

    def paina(self):
        self.funktio()