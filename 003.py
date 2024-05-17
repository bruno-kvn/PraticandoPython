# João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
# Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
# (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a
# variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite
# e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

print('\nPeso limite de peixes: 50 quilos')
print('Multa por quilo excedente: R$4,00')

peso = float(input('\nQual é o peso total de peixes em Kg? '))
excesso = peso - 50
multa = excesso * 4

if peso <= 50:
    print('Não houve excesso de peso, no entanto, não se aplica multa.')
else:
    print('Houve um excesso de peso de {:.2f}Kg, no entando, se aplica uma multa de R${:,.2f}'.format(excesso, multa))
