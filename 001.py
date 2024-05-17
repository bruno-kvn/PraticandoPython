# Desenvolva um programa que realize cálculos simples, como a soma, subtração, multiplicação e divisão de dois
# números inseridos pelo usuário.

print('\n(1) Soma\n(2) Subtração\n(3) Multiplicação\n(4) Divisão\n')
op = input('Qual operação deseja realizar: ')

if op == '1':
    n1 = int(input('Informe o primeiro número: '))
    n2 = int(input('Informe o segundo número: '))
    soma = n1 + n2
    print('A soma de {} + {} é igual a {}'.format(n1, n2, soma))
elif op == '2':
    n1 = int(input('Informe o primeiro número: '))
    n2 = int(input('Informe o segundo número: '))
    subt = n1 - n2
    print('A subtração de {} - {} é igual a {}'.format(n1, n2, subt))
elif op == '3':
    n1 = int(input('Informe o primeiro número: '))
    n2 = int(input('Informe o segundo número: '))
    mult = n1 * n2
    print('A multiplicação de {} x {} é igual a {}'.format(n1, n2, mult))
elif op == '4':
    n1 = int(input('Informe o primeiro número: '))
    n2 = int(input('Informe o segundo número: '))
    divs = n1 / n2
    print('A divisão de {} / {} é igual a {}'.format(n1, n2, divs))
else:
    print('-' * 40)
    print('          ERRO: OPÇÃO INVÁLIDA          ')
    print('-' * 40)
