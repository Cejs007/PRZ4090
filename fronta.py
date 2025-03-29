class Fronta:
    """
    Třída pro implementaci FIFO fronty.
    """

    def __init__(self, kapacita: int, nazev_bufferu="fronta"):
        """
        Inicializuje frontu s danou kapacitou a názvem.
        Prozatím obsah jako prázdný list
        """
        self.nazev_bufferu = nazev_bufferu
        self.kapacita = kapacita
        self.obsah = []

    def zobraz(self) -> None:
        """
        Zobrazí aktuální obsah fronty.
        """
        print(f"Aktuálně je v '{self.nazev_bufferu}': '{self.obsah}'")

    def zaskladni(self, co: str) -> None:
        """
        Přidá položku 'co' do fronty, pokud není plná.
        """
        # kontrola, jestli je v bufferu ještě místo
        if len(self.obsah) < self.kapacita:
            self.obsah.insert(0, co)
        else:
            print(f"Kapacita '{self.nazev_bufferu}' je plná, nelze přidat '{co}'.")

    def vyskladni(self) -> str:
        """
        Odebere položku z fronty, pokud není prázdná a vrací smazanou položku.
        """
        # Pokud v obsahu něco je -> přetypování na boolean - prázdný list = False, jinak True
        if self.obsah:
            # smaž poslední a smazaný ulož do vyskladneno
            vyskladneno = self.obsah.pop()
            print(f"Vyskladněno: {vyskladneno}")
            return vyskladneno
        else:
            print(f"Kapacita '{self.nazev_bufferu}' je prázdná, nelze vyskladnit.")
            return None

    def hromadne_vyskladni(self, kolik: int) -> None:
        """
        Zavolá metodu vyskladni přesně tolikrát, jaký je argument kolik.
        """
        # zopakuj 'kolik'rát
        for i in range(kolik):
            self.vyskladni()