alc = float(input('Preço do litro do alcool:'))
gas = float(input('Preço do litro da gasolina:'))
soma = alc / gas
print('A diferença é de {:.1f} %'.format(soma))
if soma < 0.7:
    print('Melhor custo beneficio é abastecer com alcool')
elif soma > 0.7:
    print('O melhor custo beneficio é abastecer com gasolina')
else:
    print('Tanto faz abastecer com um ou outro')
mens = str(input('Deseja efetuar um novo cálculo? Digite S / N:'))
if mens == 's':
    print('Entre com um novo cálculo')
else:
    print('Programa encerrado')




