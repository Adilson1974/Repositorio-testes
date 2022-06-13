print('-=-=-=-=' * 5)
print('\033[1;0;1;31mQUADR0 DE NOTAS''\033[m')
print('-=-=-=-=' * 5)
mat = str(input('Escolha a materia:'))
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
media = n1 + n2 / 2
print('Sua média final referente a materia de {} foi de {}'.format(mat, media))
if media >= 7:
    print('PARABÉNS! Vc foi aprovado')
else:
    print('REPROVADO! Vc precisa fazer prova de recuperção!')




