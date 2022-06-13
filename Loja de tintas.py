metros = float(input('Qual a metragem em m²:'))
'''1 litro 6 metros lata de 18lt R$80.00 galao 3.6lt R$ 25.00 '''
uso = metros / 6
galao = 25.00 / 3.6 * uso
gasto1 = uso / 3.6
latas = 80.00 / 18 * uso
gasto2 = uso / 18

if uso <= 17.99:
    print('Para pintar {:.2f}m² vai se ultilizado {:.1f}lts de tinta com um custo de R${:.2f} comprar {:.2f}galões de R$25.00'.format(metros,uso,galao,gasto1))
elif uso > 18.00:
    print('Para pintar {:.2f}m² vai se ultilizado {:.1f}lts de tinta com um custo de R${:.2f} comprar {:.2f}latas de 18lts de R$80.00'.format(metros,uso,galao,gasto2))




