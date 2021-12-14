import random

fichas_v='V'
fichas_r='R'

tablero=[]

def pintar_el_tablero(contador):
    print(str(contador),end='')
    print(" Tablero:")
    for i in range(n):
        print()
        for j in range(n):
            print(tablero[j][i],end='')
        print()
