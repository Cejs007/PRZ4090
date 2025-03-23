list_1 = [1, 2, 3, 4, 5]
list_2 = list_1
list_3 = list_1.copy()

# pracuji výhradně s listem 2 -> smažu 2 poslední hodnoty
list_2.pop()
list_2.pop()
list_2
# list 1 byl ovlivněn operacemi na listu 2 -> reference na stejné místo v paměti
print(list_1)
# list 3 byl neovlivněn -> vytvořena kopie v paměti pomocí metody .copy()
print(list_3)