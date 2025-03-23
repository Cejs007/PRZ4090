def secti_vse(*args):
    '''
    Sečte všechny vstupní argumenty (libovolný počet) pomocí + operátoru.
    '''
    if isinstance(args[0], str):
        zaklad = ""
    else:
        zaklad = 0

    for prvek in args:
        zaklad += prvek
    return zaklad

def posbirej_argumenty(**kwargs):
    for nazev, hodnota in kwargs.items():
        print(f"Pod klíčem '{nazev}' je hodnota '{hodnota}'.")
    return kwargs