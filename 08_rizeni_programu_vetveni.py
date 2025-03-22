# samozřejmě Python umí pracovat s daty -> místo int, float použijeme datetime formát
from datetime import datetime
print(datetime.now())

aktualni_cas = input("Zadej, kolik je hodin: ")
aktualni_cas = float(aktualni_cas)
if aktualni_cas < 6:
    print(f"Noc")
elif aktualni_cas < 9:
    print("Ráno")
elif aktualni_cas < 11:
    print("Dopoledne")
elif aktualni_cas < 13:
    print("Poledne")
elif aktualni_cas < 17:
    print("Odpoledne")
elif aktualni_cas < 22:
    print("Večer")
else:
    print(f"Noc")

# může být jenom celé číslo, např. 42 nebo 38
velikost_nohy = input("Zadej svoji velikost nohy: ")

# zjistit, jestli jsem dostal číslo
if velikost_nohy.isnumeric():
    velikost_nohy = int(velikost_nohy)
    print(f"Budu filtrovat boty velikosti {velikost_nohy}.")
else:
    print(f"Zadaná velikost '{velikost_nohy}' není číslo!")