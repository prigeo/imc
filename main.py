print('Olá, seja bem vindo a calculadora de Saúde do SENAI!')
nome = input('Como você se chama? ')
peso = str(input(f'{nome}, me diz seu peso em kg: '))
altura = str(input('E qual é a sua altura em metros: ')).replace(',', '.')

# ou pode ser feito assim
peso = peso.replace(',', '.')
altura =  altura.replace(',', '.')

try:
    #converte para float
    peso = float(peso)
    altura = float(altura)

    # calcula o imc
    imc = peso/(altura**2)

    #exibir o imc na tela
    print(f'{nome} o valor do seu IMC é {imc:,.2f}.')

    # verifica a saúde do usuário
    if imc < 17:
        print(f'{nome} está muito abaixo do peso')
    elif imc < 18.5:
        print(f'{nome} está abaixo do peso')
    elif imc < 25:
        print(f'{nome} está no seu peso ideal.')
    elif imc < 30:
        print(f'{nome} está acima do peso.')
    elif imc < 35:
        print(f'{nome} está obeso.')
    elif imc < 40:
        print(f'{nome} está com obesidade grau II.')
    else:
        print(f'{nome} está com obesidade mórbida')
except:
    print('Não foi possível calcular o IMC.')
