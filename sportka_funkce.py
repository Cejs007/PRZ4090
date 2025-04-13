from random import sample

def losuj_cisla(od=1, do=49, pocet=6) -> list:
    '''
    Funkce vrátí náhodně vygenerovanou sekvenci 'pocet' čísel z intervalu 'od'- 'do'.
    Defaultně je interval 1-49 a počet čísel 6.
    '''
    # pomocí range vyrobíme sekvenci čísel od 1 do 49
    sekvence_cisel = range(od, do + 1)
    # vracíme náhodně vybraných 6 čísel z této sekvence
    return sorted(sample(sekvence_cisel, pocet))

def vsad_cisla(od=1, do=49, pocet=6) -> list:
    '''
    Funkce vrátí list s 'pocet' zadanými čísly uživatelem z intervalu 'od'- 'do'.
    '''
    vsazena_cisla = []
    while len(vsazena_cisla) < pocet:
        # vstup od uživatele
        inp = input(f"Zadej číslo od nové {od}-{do}: ")
        # kontrola, zda uživatel zadal číslo
        if inp.isnumeric():
            # pokud ano, přetypujeme na int
            cislo = int(inp)
        else:
            # pokud ne, vypíšeme chybovou hlášku a pokračujeme na další iteraci cyklu
            print(f"Zadaný vstup '{inp}' není číslo!")
            continue
        # kontrola, zda je číslo v intervalu 1-49
        if not od <= cislo <= do:
            print(f"Zadané číslo '{cislo}' není v intervalu {od}-{do}!")
            continue
        # kontrola, zda už bylo číslo zadáno
        if cislo not in vsazena_cisla:
            # pokud ne, přidáme ho do seznamu vsazených čísel
            vsazena_cisla.append(cislo)
        else:
            print(f"Číslo '{cislo}' už bylo zadáno!")
    # vracíme seřazený seznam vsazených čísel
    return sorted(vsazena_cisla)