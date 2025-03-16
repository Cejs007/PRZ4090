"""
Uživatel bude v konzoli vyzván "Zadej jméno" k zadání jména (funkce input()),
program jeho vstup uloží do proměnné {jmeno} a zobrazí pomocí funkce print().
"""
jmeno = input("Zadej jméno: ")
print(f"Bylo zadáno jméno: {jmeno}")
"""
Uživatel bude v konzoli vyzván "Zadej svoji budoucí mzdu:", 
program jeho vstup uloží do proměnné a přidá k němu 80% a vytiskne výsledek s textem: 
"Nepodceňuj se, vyděláš si minimálně {výsledná mzda}".
"""
budouci_mzda = input("Zadej svou očekávanou mzdu: ")
budouci_mzda = int(budouci_mzda) * 1.8
print(f"Nepodceňuj se, vyděláš si minimálně {budouci_mzda}")