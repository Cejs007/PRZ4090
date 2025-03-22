cislo_1 = 13
cislo_2 = 7
text_1 = "ahoj"
text_2 = "čau"
# aritmetické operátory
print(cislo_1 // cislo_2)
print(cislo_1 ** 2)
# porovnávací operátory -> výsledek je bool datový typ True/False
print(cislo_1 >= cislo_2)
print(text_1 == text_2)
print(text_1 != "ahoj")
# operátory přiřazení
cislo = 10
cislo = cislo + 5
print(cislo)
cislo += 5
print(cislo)
cislo_2 %= cislo_1
print(cislo_2)
#TODO operátory identity
pass
# logické operátory
print(cislo_1 > cislo_2 or text_1 == "svět")
# operátory členství
print("o" in text_1)
print("o" in text_2)
# bitové operátory  
print(cislo_1 & cislo_2)
"""
proč 5 -> bit po bitu aplikuje and
00001101
00000111
00000101
"""