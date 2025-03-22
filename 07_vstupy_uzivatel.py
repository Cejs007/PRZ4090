# vzít přes konzoli od uživatele vstup
zadano = input("Zadej své šťastné číslo: ")
print(f"Uživatel zadal číslo '{zadano}', datový typ: {type(zadano)}")

import sys

print(sys.argv)
print(f"Argument 0 (soubor): {sys.argv[0]}")
print(f"Argument 1 (jméno): {sys.argv[1]}")
print(f"Argument 2 (příjmení): {sys.argv[2]}")
print(f"Argument 3 (bydliště): {sys.argv[3]}")
