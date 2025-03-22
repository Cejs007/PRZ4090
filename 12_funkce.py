def vytiskni_pozdrav(nekoho):
    print(f"Dobrý den {nekoho}!")

vytiskni_pozdrav("Zuzana")

def spocitej_podil(cislo_1: float, cislo_2: float) -> float:
    '''
    Funkce vezme na vstupu 2 čísla a první číslo podělí druhým číslem.
    Vrací podíl jako výsledek.
    '''
    vysledek = cislo_1 / cislo_2
    print(vysledek)
    return vysledek

vysledek = spocitej_podil(6, 10)

def vytvor_vizitku(jmeno, prijmeni, bydliste="ČR"):
    return {"jmeno": jmeno, "prijmeni": prijmeni, "bydliste": bydliste}

# zkihovny random naimportovat funkci pro náhodnmý výběr
from random import sample

# range vygeneruje sekvenci čísel od 35 do 101 -> sample z nich vybere náhodně 15 hodnot
body = sample(range(35, 101), 15)
body

def vyhodnot_zkousku(body: int, kriterium=50) -> None:
    '''
    Posoudí dosažené body studenta u zkoušky proti kritériu.
    Tiskne, zda student u zkoušky uspěl nebo ne.
    '''
    if body >= kriterium:
        print(f"Úspěch, '{body}' stačí, limit byl {kriterium} bodů.")
    else:
        print(f"Neúspěch, '{body}' nestačí, limit byl {kriterium} bodů.")

vyhodnot_zkousku(body[0], 70)