# set 'množiny' -> neindexovaná množina -> bez opakování
jidla = {"burger", "hot-dog", "pizza"}
print(jidla)
# využití - zbavit se duplicit
list_1 = ["a", "b", "c", "a", "b", "a"]
print(f"Unikátní hodnoty v listu_1 jsou {set(list_1)}")
# množinové operace -> co mám v jednom a nemám ve druhém - porovnávání
list_2 = ["d", "e", "c", "d", "e", "d"]
print(f"List 1 má navíc oproti listu 2: {set(list_1) - set(list_2)}")
print(f"List 2 má navíc oproti listu 1: {set(list_2) - set(list_1)}")
# průnik množin
print(f"Listy 1 a 2 mají společné: {set(list_1) & set(list_2)}")

# dictionaries 'slovníky' -> neindexované dvojice klíč: hodnota
vizitka = ["Michal", "Maliszewski", 32, "ČR", "SDA"]
print(vizitka[3])
vizitka_slovnik = {"jmeno": "Michal",
                   "prijmeni": "Maliszewski",
                   "vek": 32,
                   "bydliste": "ČR",
                   "prace": "SDA"}
print(vizitka_slovnik["prace"])
populace = {"Praha":1100000, "Brno": 450000, "Ostrava": 350000}
mesto = "Brno"
print(f"Populace města '{mesto}' je {populace[mesto]}.")