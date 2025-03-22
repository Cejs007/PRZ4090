# while zastavení pomocí podmínky
i = 0
while i < 10:
    print("a")
    i += 1

# while zastavení pomocí flag
faktury = ["faktura za počítač"
           "faktura za auto",
           "faktura za mobil",
           "faktura za lego",
           "faktura za lednice",
           "faktura za kabát"]
# flag -> dokud bude True, tak smyčka jede dál
zatim_nemam = True
# iterátor/index -> abych mohl prohledávat podle indexu faktury
i = 0
# sleduji proměnnou zatim_nemam a iteruji
while zatim_nemam:
    # pokud najdu slovo lednice ve faktuře
    if "lednice" in faktury[i]:
        print(f"Nalezeno! {faktury[i]}")
        # přenastavím flag na False -> zastaví to smyčku
        zatim_nemam = False
    else:
        # pokud lednici nenajdu, jedu dál
        print("Hledám dál!")
    # po každé iteraci zvednu index
    i += 1

# while zastavení pomocí break
# iterátor/index -> abych mohl prohledávat podle indexu faktury
i = 0
# nekonečná smyčka -> True jako konstanta
while True:
    # pokud najdu slovo lednice ve faktuře
    if "lednice" in faktury[i]:
        print(f"Nalezeno! {faktury[i]}")
        # obecně zastav smyčku
        break
    else:
        # pokud lednici nenajdu, jedu dál
        print("Hledám dál!")
    # po každé iteraci zvednu index
    i += 1

faktury = {"faktura za počítač": 25000,
           "faktura za auto": 300000,
           "faktura za mobil": 8000,
           "faktura za lego": 2000,
           "faktura za lednice": 15000,
           "faktura za kabát": 2500}


# na dozaz ohledně dict -> rozhodně vhodnější for smyčka
# pro klíč, hodnota ze slovníku.items()
for nazev, castka in faktury.items():
    if castka > 10000:
        # pokud najdu slovo lednice ve faktuře
        if "lednice" in nazev:
            print(f"Nalezeno! {nazev}")
            # obecně zastav smyčku
            break
        else:
            # pokud lednici nenajdu, jedu dál
            print("Hledám dál!")
    else:
        continue