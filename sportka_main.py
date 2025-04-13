from sportka_funkce import losuj_cisla, vsad_cisla

# sázka uživatel
vsazena = vsad_cisla()
# první losování
losovana = losuj_cisla()
# čítač počtu losování
pocet_losovani = 0
# losuj dokud nevyhraju (vsazena == losovana)
while vsazena != losovana:
    # nové losování
    losovana = losuj_cisla()
    # přičteme 1 k počtu losování
    pocet_losovani += 1
    # každé 1 000 000 losování vypíšeme počet losování -> abychom viděli, že program běží
    if pocet_losovani % 1000000 == 0:
        print(f"Počet losování: {pocet_losovani}")
# vypíšeme výsledek
print(f"Prosázeno do výhry: {pocet_losovani * 20/1000000} mil Kč")
pocet_sazek_rok = 3 * 2 * 8 * 52
print(f"Prosázeno do výhry: {pocet_losovani / pocet_sazek_rok} let.")