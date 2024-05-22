# Faça um Programa que peça dois números e imprima o maior deles.

n1 = float(input('\nPrimeiro número: '))
n2 = float(input('Segundo número: '))

if n1 > n2:
    print('\033[1;34mO maior número digitado foi {}\033[m'.format(n1))
else:
    print('\033[1;34mO maior número digitado foi {}\033[m'.format(n2))
