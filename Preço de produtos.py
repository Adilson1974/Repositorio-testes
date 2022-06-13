p1 = float(input('Digite o valor do primeiro produto:R$'))
p2 = float(input('Digite o valor do segundo produto:R$'))
p3 = float(input('Digite o valor do terceiro produto:R$'))
menor = p1
if p2<p1 and p2<p3:
    menor = p2
if p3<p1 and p3<p2:
    menor = p3
print('Vc deve comprar o produto no valor de R${:.2f} pois é mais barato!'.format(menor))
