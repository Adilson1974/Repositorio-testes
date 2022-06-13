sh = float(input('Quanto ganha por hora R$'))
ht = int(input('Quantas horas trabalhadas no mês:'))
salario = sh*ht
print('Seu salário bruto é de R${:.2f}'.format(salario))
print('DESCONTOS:')
ir =  (salario * 11 / 100)
inss =  (salario * 8 / 100)
sindicato = (salario * 5 / 100)
sl = salario - (salario * 24 /100)

print('IR (11%) R${:.2f}'.format(ir))
print('INSS (8%) R${:.2f}'.format(inss))
print('Sindicato (5%) R${:.2f}'.format(sindicato))
print('SALÁRIO LÍQUIDO! total de R${:.2f}'.format(sl))


