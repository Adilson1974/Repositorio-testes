print('''LISTA DE COMPRAS:
[ 1 ] 1 kg de arroz tipo 1 e 2 kg de feijão preto
[ 2 ] 3 kg de arroz tipo 2 e 1 kg de feijão branco
[ 3 ] 2 kg de lentilha e 1 kg de linguiça defumada''')
opção = float(input('Qual é a sua opção?'))
compra1 = 30.50 + (9.80 * 2)
compra2 = 20.75 * 3 + 7.50
compra3 = 6.80 * 2 + 5.50
if opção == 1:
    print('Sua compra teve um total de R${:.2f}'.format(compra1))
elif opção == 2:
    print('Sua compra teve um total de R${:.2f}'.format(compra2))
elif opção ==3:
    print('sua compra teve um total de R${:.2f}'.format(compra3))
