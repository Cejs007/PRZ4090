Jmeno = "Michal"

text_cs = "Nejednoznačná vize srdce, která dává přednost miskám kiwi před gulášem."

print("Ahoj" + "\t" + Jmeno + "\n" + text_cs)

# Format and display (older solution)
title = "General"
name = "Kenobi"
print("Hello there, %s %s" % (title, name))

# Format and display (newer solution)
title = "General"
name = "Kenobi"
print("Hello there, {} {}".format(title, name))

print(f"Hello there, {title} {name}")

cesta = r"C:\Users\cejs0\OneDrive\Desktop\PY4090"
nazev = "operatory.py"

plna_cesta = f"{cesta}\\{nazev}"
print(plna_cesta)

emoji = "\U0001F600"
print(emoji)

cislo_1 = 13
cislo_2 = 7
print(f"Spočítej:\n{"-"*30}\n{cislo_1}*{cislo_2}={cislo_1*cislo_2}")

print(f"'Opravdu' je {cislo_1}*{cislo_2}=0 \"špatně\"")

n = 109.2345654324
print(f"{n: .0f}")