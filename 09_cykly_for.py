# ukázka -> programování méně user-friendly jazyky
'''
mesta = ["Praha", "Brno", "Ostrava"]
# iterátor - začínám na nule, protože indexujeme od nuly v Pythonu
i = 0
# i z sekvence čísel od 0 - délka-1 -> pseudokód, není funkční
for i in len(mesta)-1:
    # vezmeme prvek na indexu i
    print(mesta[i])
    # přičteme 1, abychom v příští iteraci vzali další prvek
    i += 1
'''

for mesto in ["Praha", "Brno", "Ostrava"]:
    print(mesto)

for body_zkouska in [78, 56, 92]:
    print(body_zkouska)

# Úloha 3: Počet samohlásek
# Požádejte uživatele o zadání slova. Program spočítá a vypíše, kolik samohlásek (a, e, i, o, u, y) slovo obsahuje.

# zadaný text od uživatele
text = input("Zadej text: ")
# znaky, které budu hledat a počítat v textu
samohlasky = ("a", "e", "i", "o", "u", "y")
# verze 1
# nachystám si čítač samohlásek -> začínám na nule
pocet_samohlasek = 0
# pro každou samohlásku proveď
for samohlaska in samohlasky:
    # vytiskni aktuální samohlásku a počet, kolikrát se v textu vyskytuje
    print(f"Počet samohlásky '{samohlaska}': {text.count(samohlaska)}")
    # připočti do čítače počet, kolikrát se aktuální samohláska nachází v textu
    pocet_samohlasek += text.count(samohlaska)
# po provedení smyčky, ukaž kolik jsi napočítal samohlásek
print(f"Nalezeno '{pocet_samohlasek}' samohlásek v textu '{text}'.")

# verze 2
# nachystám si čítač samohlásek -> začínám na nule
pocet_samohlasek = 0
# pro každý znak z textu
for pismeno in text:
    # zkontroluj, jestli aktuální písmeno je samohláska, pokud ano -> přičti 1 do čítače
    if pismeno == "a":
        pocet_samohlasek += 1
    elif pismeno == "e":
        pocet_samohlasek += 1
    elif pismeno == "i":
        pocet_samohlasek += 1
    elif pismeno == "o":
        pocet_samohlasek += 1
    elif pismeno == "u":
        pocet_samohlasek += 1
    elif pismeno == "y":
        pocet_samohlasek += 1

# po provedení smyčky, ukaž kolik jsi napočítal samohlásek
print(f"Nalezeno '{pocet_samohlasek}' samohlásek v textu '{text}'.")

# verze 3
# nachystám si čítač samohlásek -> začínám na nule
pocet_samohlasek = 0
# pro každý znak z textu
for pismeno in text:
    # zkontroluj, jestli aktuálnmí písmeno je v tuplu samohlásky, pokud ano, přičti 1
    if pismeno in samohlasky:
        pocet_samohlasek += 1

# po provedení smyčky, ukaž kolik jsi napočítal samohlásek
print(f"Nalezeno '{pocet_samohlasek}' samohlásek v textu '{text}'.")
