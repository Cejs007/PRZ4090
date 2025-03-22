'''
vytvořte list s 5 městy, kdy města budou napsána malým písmem, 
upravte v druhém kroku list tak, 
že první písmeno každého města bude velké - nápověda "abc".capitalize()
'''
# sem budu ukládat města
mesta = []
# 5x zopakuj
for i in range(5):
    # uživatel zadá město a zadané město je uloženo do listu mesta
    mesta.append(input("Zadej město: "))
# sem budeme ukládat města s prvním velkým písmenem
mesta_capitalize = []
# pro každé město z měst
for mesto in mesta:
    # ulož do listu mesto, po tom co jsme upravili první písmeno na velké
    mesta_capitalize.append(mesto.capitalize())

print(mesta)
print(mesta_capitalize)