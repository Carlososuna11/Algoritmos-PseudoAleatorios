from tabulate import tabulate
from math import gcd  

def cuadradosMedios(digitos:int,semilla:int,n:int):
    """
    Algoritmo de Cuadrados medios
    :param digitos: cantidad de digitos
    :param semilla: semilla del generador
    :param n: Cantidad de números a generar
    """
    sol = []
    for i in range(n):
        yaux = str(semilla**2)
        if len(yaux)%2!=0:
            yaux='0'+yaux
        pos = (len(yaux)-digitos)//2
        semilla=yaux[pos:pos+digitos]
        sol.append([yaux,semilla,f'0.{semilla}'])
        semilla=int(semilla)
    print(f"{tabulate(sol,headers=['Y','X','R'],tablefmt='fancy_grid',disable_numparse=True)}")

def productosMedios(digitos:int,semillaA:int,semillaB:int,n:int):
    """
    Algoritmo de Productos medios
    :param digitos: cantidad de digitos
    :param semillaA: semilla A
    :param semillaB: semilla B
    :param n: Cantidad de números a generar
    """
    sol = []
    for i in range(n):
        y = str(semillaA*semillaB)
        if len(y)%2!=0:
            y='0'+y
        pos = (len(y)-digitos)//2
        semillaA=int(semillaB)
        semillaB=y[pos:pos+digitos]
        sol.append([y,semillaB,f'0.{semillaB}'])
        semillaB=int(semillaB)
    print(f"{tabulate(sol,headers=['Y','X','R'],tablefmt='fancy_grid',disable_numparse=True)}")

def multiplicadroConstante(digitos:int,constanteA:int,semilla:int,n:int):
    """
    Algoritmo de Multiplicador Constante
    :param digitos: cantidad de digitos
    :param constanteA: constante A (con la misma cantidad de digitos que la solicitada)
    :param semilla: semilla (con la misma cantidad de digitos que la solicitada)
    :param n: Cantidad de números a generar
    """
    sol = []
    for i in range(n):
        y = str(constanteA*semilla)
        if len(y)%2!=0:
            y='0'+y
        pos = (len(y)-digitos)//2
        semilla=y[pos:pos+digitos]
        sol.append([y,semilla,f'0.{semilla}'])
        semilla=int(semilla)
    print(f"{tabulate(sol,headers=['Y','X','R'],tablefmt='fancy_grid',disable_numparse=True)}")

def lineal(semilla:int,a:int,c:int,m:int,n:int):
    """
    Algoritmo Lineal
    :param semilla: semilla del generador
    :param a: constante multiplicativa
    :param c: constante aditiva 
    :param m: modulo
    :param n: Cantidad de números a generar
    """
    sol = []
    for i in range(n):
        y = (a*semilla+c)%m
        r = y/(m-1)
        semilla=y
        sol.append([y,r])
    print(f"{tabulate(sol,headers=['Y','R'],tablefmt='fancy_grid',disable_numparse=True)}")

def linealMaxPeriodoVida(semilla:int,k:int,c:int,g:int):
    """
    Algoritmo Lineal Maximo periodo de vida
    :param semilla: semilla del generador
    :param k: entero -> a= 1+4k
    :param c: constante aditiva, relativamente primo a m (MCD = 1) 
    :param g: entero -> m = 2^g
    """
    a = 1+4*k
    m= 2**g
    n = 2**g
    if gcd(m,c)==1:
        sol = []
        for i in range(n):
            y = (a*semilla+c)%m
            r = y/(m-1)
            semilla=y
            sol.append([y,r])
        print(f"{tabulate(sol,headers=['Y','R'],tablefmt='fancy_grid',disable_numparse=True)}")
    else:
        print(f'm y c no son relativamente primos = {gcd(m,c)}')

def congruencialMultiplicativo(semilla:int,k:int,g:int):
    """
    Algoritmo Congruencial Multiplicativo
    :param semilla: semilla del generador , debe ser impar
    :param k: entero -> a= 3+8k o 5+8k
    :param g: entero -> m = 2^g , n=2^(g-2)
    """
    if semilla%2!=0:
        a = 5+8*k
        # a = 3+8*k
        m = 2**g
        n = 2**(g-2)
        sol = []
        for i in range(n):
            y = (a*semilla)%m
            r = y/(m-1)
            semilla=y
            sol.append([y,r])
        print(f"{tabulate(sol,headers=['Y','R'],tablefmt='fancy_grid',disable_numparse=True)}")
    else:
        print('la semilla debe ser impar')

def congruencialCuadratico(semilla:int,g:int,a:int,c:int,b:int):
    """
    Algoritmo Congruencial Cuadratico
    :param semilla: semilla del generador
    :param g: entero -> m = 2^g
    :param a: entero
    :param c: entero
    :param b: entero
    """
    sol = []
    m=2**g
    for i in range(m):
        y = (a*(semilla**2)+b*semilla+c)%m
        r = y/(m-1)
        semilla=y
        sol.append([y,r])
    print(f"{tabulate(sol,headers=['Y','R'],tablefmt='fancy_grid',disable_numparse=True)}")

def congruencialCuadraticoMaximo(semilla:int,g:int,a:int,c:int,b:int):
    """
    Algoritmo Congruencial Cuadratico
    :param semilla: semilla del generador
    :param g: entero -> m = 2^g
    :param a: entero par
    :param c: entero impar
    :param b: entero (b-1) mod 4 != 1
    """
    if a%2==0 and c%2!=0 and (b-1)%4!=1:
        sol = []
        m=2**g
        for i in range(m):
            y = (a*(semilla**2)+b*semilla+c)%m
            r = y/(m-1)
            semilla=y
            sol.append([y,r])
        print(f"{tabulate(sol,headers=['Y','R'],tablefmt='fancy_grid',disable_numparse=True)}")
    else:
        print(f'a%2==0? {a%2==0}, c%2!=0? {c%2!=0}, (b-1)%4!=1? {(b-1)%4!=1}')