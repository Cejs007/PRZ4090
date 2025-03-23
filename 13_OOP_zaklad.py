class Uzivatel:

    def __init__(self, jmeno, prijmeni, email, telefon):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.email = email
        self.telefon = telefon

    def udaje_zakaznika(self):
        print(f"Jméno: {self.jmeno}")
        print(f"Příjmení: {self.prijmeni}")

zakaznik_1 = Uzivatel("Michal", "Maliszewski", "mm@seznam.cz", 123456789)
print(zakaznik_1.email)
zakaznik_1.udaje_zakaznika()

zakaznik_2 = Uzivatel("Petr", "Fiala", "pf@seznam.cz", 123456789)
print(zakaznik_1.email)
zakaznik_2.udaje_zakaznika()

zakaznik_3 = Uzivatel("Andrej", "Babiš", "ab@seznam.cz", 123456789)
print(zakaznik_1.email)
zakaznik_3.udaje_zakaznika()

class Auto:

    def __init__(self, znacka, model, rok_vyroby, vykon, stav_tachometru, celkovy_stav, cena):
        self.znacka = znacka
        self.model = model
        self.vykon = vykon
        self.rok_vyroby = rok_vyroby
        self.stav_tachometru = stav_tachometru
        self.celkovy_stav = celkovy_stav
        self.cena = cena

    def nastartuj(self):
        if self.vykon < 100:
            print("Vrrm")
        elif self.vykon < 200:
            print("Vrrrrrrm")
        else:
            print("Vrrrrrrrrrrrrrrrm")

    def zmen_cenu(self, nova_cena):
        self.cena = nova_cena

auto_1 = Auto("Škoda", "Fabia", 2005, 50, 250000, "dobrý", 50000)
auto_1.nastartuj()
auto_2 = Auto("Ford", "Focus", 2010, 100, 150000, "velmi dobrý", 100000)
auto_2.nastartuj()
auto_3 = Auto("BMW", "M5", 2015, 300, 50000, "velmi dobrý", 500000)
auto_3.nastartuj()

