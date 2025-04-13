class Zamestnanec:

    koeficient_plat = 1.05

    def __init__(self, jmeno, prijmeni, vek, plat):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.plat = plat
        self.vek = vek

    def __str__(self):
        return f"Zaměstanec: {self.prijmeni}"
    
    def __repr__(self):
        return f"Zaměstanec: {self.prijmeni}"
    
    def pridej_plat(self, zmena_platu=0):
        self.plat = self.plat * self.koeficient_plat + zmena_platu

class DatovyVedec(Zamestnanec):

    koeficient_plat = 1.07

    def vytvor_AI_model(self):
        print("AI model vytvořen.")

class Manazer(Zamestnanec):

    def __init__(self, jmeno, prijmeni, vek, plat, podrizeni=[]):
        super().__init__(jmeno, prijmeni, vek, plat)
        self.podrizeni = podrizeni if podrizeni else []

    def pridej_podrizeneho(self, zamestnanec):
        self.podrizeni.append(zamestnanec)

    def vytiskni_podrizene(self):
        for zamestnanec in self.podrizeni:
            print(zamestnanec.jmeno, zamestnanec.prijmeni)