class Manageri:
    painetut_napit = []
    nyt_painetut_napit = []
    odotuslista = []

    @classmethod
    def update(cls):
        cls.odotuslista += cls.nyt_painetut_napit
        cls.nyt_painetut_napit = []

    @classmethod
    def down(cls, event):
        k = event.keycode
        if k not in cls.painetut_napit:
            cls.painetut_napit.append(k)
        if k not in cls.odotuslista:
            cls.nyt_painetut_napit.append(k)
        #print("alas: " + str(k))

    @classmethod
    def up(cls, event):
        k = event.keycode
        if k in cls.painetut_napit:
            cls.painetut_napit.remove(k)
        if k in cls.odotuslista:
            cls.odotuslista.remove(k)
        #print("ylös: " + str(k))

    @classmethod
    def alhaalla_nappi(cls, keycode):
        if keycode in cls.painetut_napit:
            return True
        return False

    @classmethod
    def nyt_painettu_nappi(cls, keycode):
        if keycode in cls.nyt_painetut_napit:
            return True
        return False
