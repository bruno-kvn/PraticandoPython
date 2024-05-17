# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
# salário bruto.
# quanto pagou de IR.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.

ganha_hora = float(input('\nQuanto você ganha por hora trabalhada? R$'))
horas = int(input('Quantas horas você trabalha por mês? '))

salario_bruto = ganha_hora * horas
ir = salario_bruto * 11 / 100
inss = salario_bruto * 8 / 100
sind = salario_bruto * 5 / 100
salario_liquido = salario_bruto - (ir + inss + sind)

print('\nSalário bruto: R${:,.2f}'.format(salario_bruto))
print('11% cobrado de imposto de renda: R${:,.2f}'.format(ir))
print('8% cobrado pelo INSS: R${:,.2f}'.format(inss))
print('5% cobrado pelo sindicato: R${:,.2f}'.format(sind))
print('Salário líquido igual a: R${:,.2f}'.format(salario_liquido))
