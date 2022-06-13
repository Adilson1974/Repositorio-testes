s1 = float(input('Valor do salário: R$'))
aum1 = s1 + (s1 * 20 / 100)
aumreal1 = (s1* 20 / 100)
aum2 = s1 + (s1 * 15 / 100)
aumreal2 = (s1 * 15 / 100)
aum3 = s1 + (s1 * 10 / 100)
aumreal3 = (s1 * 10 / 100)
aum4 = s1 + (s1 * 5 / 100)
aumreal4 = (s1 * 5 / 100)
if s1 < 280.00:
    print('Seu salário atual de R${:.2f} teve um reajuste de 20% (R${:.2f}) e passa a valer R${:.2f}'.format(s1,aumreal1, aum1))
elif s1 < 700.00:
    print('Seu salário de R${:.2f} teve um reajuste de 15% (R${:.2f}) e passa a valer R${:.2f}'.format(s1, aumreal2, aum2))
elif s1 < 1500.00:
    print('Seu salário de R${:.2f} teve um reajuste de 10% (R${:.2f}) e passa a valer R${:.2f}'.format(s1, aumreal3, aum3))
else:
    print('Seu salário de R${:.2f} teve um reajuste de 5% (R${:.2f}) e passa a valer R${:.2f}'.format(s1,aumreal4,  aum4))


