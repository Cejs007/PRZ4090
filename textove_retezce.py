text = "Značnou pozornost budí balkon jednoho z bytů v ostravské čtvrti Mariánské Hory. Prostor je plný neuvěřitelného a důmyslně naskládaného harampádí přivezeného z Rakouska. Byt občas k přespání využívá rakouský obchodník s použitými věcmi, který kuriózní výzdobou nejspíš demonstruje svůj patriotismus."
text_lower_case = text.lower()
index = text.index("R")
print(f"Písmeno '{text[index]}' se nachází na pozici {index}.")
print(f"Text je dlouhý {len(text)} znaků!")
opakujici_se_znak = input("Zadej znak: ")
print(f"Písmeno '{opakujici_se_znak}' se v textu objevilo {text.count(opakujici_se_znak)}.")

hledane_slovo = "důmyslně"
zacatek = text.index(hledane_slovo)
delka = len(hledane_slovo)
konec = zacatek + delka

print(f"Délka: {delka}")
print(f"Snad by mělo slovo '{hledane_slovo}' začínat na pozici {zacatek} a končit na {konec}.")
print(text[zacatek:konec])

# slicing [od=0:do=len-1:krok=1]
# od začátku do konce s krokem 10
print(text[::10])
# od začátku do indexu 20, s krokem 2
print(text[:20:2])

ukazka = "Ostrava"
print(ukazka[::-1])
print(f"Výchozí text: {ukazka}\nCaps: {ukazka.upper()}\nMalým: {ukazka.lower()}")