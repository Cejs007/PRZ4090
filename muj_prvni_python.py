'''
tohle je první .py soubor
používáme PyCharm
moc ho nemám rád
'''

# datové typy
cislo = 10
text = "deset"
boolean = True
cislo_des = 3.14
print(cislo, text, boolean, cislo_des)
print(type(cislo), type(text), type(boolean), type(cislo_des))
# boolean -> pro provnávání
print("Ahoj" == "ahoj")

# ukázka diakritika
hrozne_slovo = "řeřicha"
print(hrozne_slovo)

# dynamické datové typy
number: int = 13
print(number, type(number))
number = "pes"
print(number, type(number))

NUMBER = 12 # konstanta jako konvence, můžu přepisovat jako každou jinou proměnnou
print(NUMBER, type(NUMBER))
NUMBER = "klobasa"
print(NUMBER, type(NUMBER))

