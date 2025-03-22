'''
Uživatel bude v konzoli vyzván "Zadej jméno" k zadání jména (funkce input()). 
Vytiskněte datový typ zadaného vstupu pomocí funkce type(). 
Zkontrolujte, že uživatel nezanechal prázdné pole pomocí if struktury. 
Pokud nebylo zadáno jméno, vypište "Jméno nezadáno", pokud ano vypište ("Zadané jméno: {jméno}")
'''
# výzva pro input -> co uživatel uvidí za popis, když má zadávat hodnotu
vyzva = "Zadej jméno: "
# získat od uživatele jméno pomocí input
zadane_jmeno = input(vyzva)
# kontrola, jestli je zadaný string prázdný
if zadane_jmeno: # odpovídá 'zadane_jmeno != ""'
    # pokud ne, tiskneme zadané jméno
    print(f"Zadané jméno: {zadane_jmeno}")
else:
    # nebylo zadáno
    print("Jméno nezadáno")

'''
Vyzvěte uživatele, aby zadal text, zkontrolujte, že má alespoň 5 znaků pomocí funkce len() 
a pokud ano, tak vypište, jestli má sudý nebo lichý počet znaků.
'''
# získat vstup od uživatele
nejaky_text = input("Zadej text: ")
# má alespoň 5 znaků?
if len(nejaky_text) >= 5:
    # ano - zbytek po celočíselném dělení 0 -> sudé
    if len(nejaky_text) % 2 == 0:
        print(f"Text '{nejaky_text}' má sudý počet znaků.")
    else:
        # jinak liché
        print(f"Text '{nejaky_text}' má lichý počet znaků.")
else:
    print(f"Text '{nejaky_text}' je příliš krátký.")