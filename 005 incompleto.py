# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
# Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

print('\nPrecisa de ajuda para calcular a área quadrada?')
print('(1) Sim\n(2) Não')
opcao = input('>>> ')

if opcao == '1':
    c1 = float(input('Primeiro comprimento em metros: '))
    c2 = float(input('Segundo comprimento em metros: '))
    area = c1 * c2
    print('A aréa em metros quadrados é igual a {:.2f}'.format(area))
    tinta = area / 3
    print('Considerando que cada lata de tinta tem 18 litros,')
    print('e que a cobertura da tinta é de 1 litro para cada 3 metros quadrados')
else:
    area = float(input('Qual o tamanho em metros quadrados da área a ser pintada? >> '))
    tinta = area / 3
    print('Considerando que cada lata de tinta tem 18 litros,')
    print('e que a cobertura da tinta é de 1 litro para cada 3 metros quadrados')
