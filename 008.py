# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.

sexo = str(input('\nInforme o sexo: F ou M.\n>>> ')).upper().strip()

if sexo == 'F':
    print('\033[1;35mF - Feminino.\033[m')
elif sexo == 'M':
    print('\033[1;34mM - Masculino.\033[m')
else:
    print('\033[1;31mSexo Inválido.\033[m')
