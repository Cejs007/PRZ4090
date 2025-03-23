from random import randint

class Postava:

    def __init__(self, jmeno, zivoty=100, utok_min=5, utok_max=10, stit=2):
        self.jmeno = jmeno
        self.zivoty = zivoty
        self.utok_min = utok_min
        self.utok_max = utok_max
        self.stit = stit
        self.mrtev = False

    def ukaz_zivoty(self):
        print(f"{self.jmeno} má {self.zivoty} životů.")

    def utok(self):
        return randint(self.utok_min, self.utok_max)

    def obrana(self, poskozeni):
        # kontrola, jestli poškození projde štítem
        if poskozeni > self.stit:
            self.zivoty = self.zivoty - (poskozeni - self.stit)
            if self.zivoty < 1:
                self.mrtev = True
                print(f"{self.jmeno} je mrtev.")
        else:
            # pokud bychom provedli výpočet -> životy by vzrůstaly -> nedělám nic
            print(f"Útok '{poskozeni}' neprorazil štít.")


def mortal_combat(zastupce_dobro: Postava, zastupce_zlo: Postava) -> str:
    '''
    Vezme jednoho bojovníka za dobro a jednoho za zlo vytvořené pomocí třídy Postava
    a nechá je proti sobě bojovat na život a na smrt.
    Vrací jméno vítězného bojovníka.
    '''
    # dokud jsou oba na živu
    while not zastupce_dobro.mrtev and not zastupce_zlo.mrtev:
        # hodíme si mincí -> rozhodujeme náhodně, kdo bude v daném kole útočit a kdo se bránit
        if randint(0, 1):
            # padne-li 1 -> útočí dobro
            zastupce_zlo.obrana(zastupce_dobro.utok())
        else:
            # padne-li 0 -> útočí zlo
            zastupce_dobro.obrana(zastupce_zlo.utok())
    # po ukončení smyčky, pokud zastupce dobro padl -> vracíme jméno bojovníka za zlo a naopak
    return zastupce_zlo.jmeno if zastupce_dobro.mrtev else zastupce_dobro.jmeno