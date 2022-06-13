
a = int(input('Digite o primeiro numero:'))
b = int(input('Digite o segundo número:'))
c =int(input('Digite o terceiro número:'))
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O maior número foi {}'.format(maior))
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('o menor numero foi {}'.format(menor))







