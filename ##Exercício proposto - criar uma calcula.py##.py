##Exercício proposto - criar uma calculadora-imc, utilizando o IMC = peso (kg) / altura(m) x altura(m)##
##Devendo preencher os dados de peso e altura, nas respectivas linhas 4 e 5. O resultado, mostrará se a pessoa está dentro do peso ideal, abaixo ou acima do peso##

peso = float(input('Informe o seu peso:'))
altura = float(input('Informe a sua altura:'))
imc = peso / (pow(altura, 2))

print(f'Seu índice de massa corporal é: {imc:.2f}')

if imc < 18.5:
    print('Você está Abaixo do Peso')
elif imc >=18.5 and imc <=24.9:
    print('Você está com Peso Ideal')
elif imc >=25 and imc <=29.9:
    print('Você está Acima do Peso')
elif imc > 29.9:
    print ('Você está com Obesidade')

    




