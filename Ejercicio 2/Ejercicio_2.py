import random

fichas_v='V'
fichas_r='R'

n=0

tablero=[]

def pintar_el_tablero(contador):
    global n

    
    print(str(contador),end='')
    print(" Tablero:")
    for i in range(int(n)):
        print()
        for j in range(int(n)):
            print(tablero[j][i],end='')
        print()

def colocar_fichas_ini():
    global tablero
    global fichas_v
    global fichas_r
    global n
    
    colocadas=0
    
    while(colocadas<n):
        ale=random.randint(0, (n-1))
        if(tablero[ale][i]==' '):
            tablero[ale][i]=fichas_v
            colocadas=colocadas+1
    

def main():
    global n
    global tablero

    i=2

    n=input('Elige numero de casillas de largo: ')
    pintar_el_tablero(i)

if __name__=="__main__":
    main()