#Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e que o FGTS corresponde a 11% do
# Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto
# menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#Desconto do IR:
#Salário Bruto até 900 (inclusive) - isento
#Salário Bruto até 1500 (inclusive) - desconto de 5%
#Salário Bruto até 2500 (inclusive) - desconto de 10%
#Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.

ganha = float(input('\nQuanto o funcionário ganha por hora trabalhada? R$'))
hora = int(input('Quantas horas o funcionário trabalha por mês? '))
salario_bruto = ganha * hora
inss = salario_bruto * 0.10

print('\033[1m-\033[m' * 40)
print('\033[1;33mSalário bruto:          R${:,.2f}\033[m'.format(salario_bruto))

if salario_bruto <= 900:
    ir = 0
    print('\033[1;31m(-) 0% IR:              R$0.00\033[m')
elif salario_bruto <= 1500:
    ir = salario_bruto * 0.05
    print('\033[1;31m(-) 5% IR:              R${:,.2f}\033[m'.format(ir))
elif salario_bruto <= 2500:
    ir = salario_bruto * 0.10
    print('\033[1;31m(-) 10% IR:             R${:,.2f}\033[m'.format(ir))
else:
    ir = salario_bruto * 0.20
    print('\033[1;31m(-) 20% IR:             R${:,.2f}\033[m'.format(ir))

print('\033[1;31m(-) 10% INSS:           R${:,.2f}\033[m'.format(inss))
print('\033[1;34m( ) 11% FGTS:           R${:,.2f}\033[m'.format(salario_bruto * 0.11))
print('\033[1;31mTotal de descontos:     R${:,.2f}\033[m'.format(ir + inss))

salario_liquido = salario_bruto - (ir + inss)
print('\033[1;32mSalário Líquido:        R${:,.2f}\033[m'.format(salario_liquido))
print('\033[1m-\033[m' * 40)
