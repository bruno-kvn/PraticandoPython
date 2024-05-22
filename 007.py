# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

num = float(input('\nDigite um número: '))

if num < 0:
    print('\033[1;34mO número {} é negativo.\033[m'.format(num))
else:
    print('\033[1;34mO número {} é positivo.\033[m'.format(num))
