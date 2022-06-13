peso = float(input('Quantos kilos de peixe foi pescado?'))
excesso = (peso - 50)
multa = (excesso *4)
print('Para cada kg de peixe acima de 50kg terá uma multa de R$4.00 por kg')
if peso <= 50:
    print('Vc pescou {:.0f}kg de peixe! esta dentro do limite estabelicido!'.format(peso))
elif peso > 50:
    print('vc pescou {:.0f}kg e excedeu {:.0f}kg a mais, por isso tera uma multa no valor de R${:.2f}'.format(peso,excesso,multa))

