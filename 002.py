# Tendo como dado de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# utilizando as seguintes fórmulas:
# Para homens: (72.7*h) - 58
# Para mulheres: (62.1*h) - 44.7

altura = float(input('\nQual é a sua altura? '))
sexo = input('Você é homem ou mulher? ')
peso_homem = (72.7 * altura) - 58
peso_mulher = (62.1 * altura) - 44.7

if sexo == 'homem':
    print('O peso ideal de um homem que tem {}m de altura é de {:.2f}'.format(altura, peso_homem))
elif sexo == 'mulher':
    print('O peso ideal de uma mulher que tem {}m de altura é de {:.2f}'.format(altura, peso_mulher))
else:
    print('-' * 40)
    print('ERRO: OPÇÃO INVÁLIDA\nDIGITE: homem OU mulher')
    print('-' * 40)
