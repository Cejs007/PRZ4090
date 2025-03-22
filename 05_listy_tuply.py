# neznám-li kolekce -> co hodnota to proměnná
# user-unfriendly
mesto_1 = "Praha"
mesto_2 = "Brno"
mesto_3 = "Ostrava"
mesto_4 = "Plzeň"
mesto_5 = "České Budějovice"

# list -> seřazené pole hodnot (libovolné datové typy, klidně pomíchané v 1 listu)
mesta = ["Praha", "Brno", "Ostrava", "Plzeň", "České Budějovice"]
print(f"Délka listu mesta je {len(mesta)}.")
# Indexování listů
print(mesta[2])
katastrofalni_list = [13, True, "Ahoj", [5, False, "Opava"], 0]
# jak se dostat na 'p' ve slově Opava
print(katastrofalni_list[3][2][1])
# slicing [od=0, do=len-1:krok=1] -> dej mi první 3 města
print(mesta[:3])
# poslední prvek -> indexování odzadu
print(mesta[-1])
# rozšíření listu pomocí '+'
dalsi_mesta = ["Jihlava", "Liberec"]
mesta += dalsi_mesta
# rozšíření listu pomocí extend
extra_mesta = ["Vyškov", "Pardubice"]
mesta.extend(extra_mesta)
# rozšíření listu pomocí append -> přidání nové hodnoty nakonec
mesta.append("Havířov")
# rozšíření listu pomocí insert -> přidání nové hodnoty na zadanou pozici
mesta.insert(1, "Olomouc")
# smazat poslední
mesta.pop()
print(mesta)
# prázdný list
prazdny = []
prazdny = list()

# tuple 'N-tice' -> seřazené pole hodnot, ale je to "read-only list"
mesta_tuple = ("Praha", "Brno", "Ostrava", "Plzeň", "České Budějovice")
print(mesta_tuple, type(mesta_tuple))
# zkrácený zápis
vesnice_tuple = "Soběšovice", "Žermanice", "Sedliště"
print(vesnice_tuple, type(vesnice_tuple))
# prázdný tuple
prazdny = ()
prazdny = tuple()
