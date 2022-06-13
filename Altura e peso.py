sexo= str(input('digite o sexo M para masculino e F para feminino:')).upper()
alt = float(input('digite sua altura:'))
pesoM = (72.7*alt)-58
pesoF = (62.1*alt)-44.7
if sexo =='M':
    print('seu peso ideal é de {:.2f}KG'.format(pesoM))
else:

    print('Seu peso ideal é de {:.2f}KG'.format(pesoF))
