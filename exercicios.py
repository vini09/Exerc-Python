#Faça um programa em linguagem Python que converta metros para centímetros



metro = int(input("Informe o metro: "))

metro = metro*100

print("O metro em centimetros eh: ", metro)



#  Faça um programa em Python que leia um valor inteiro e mostre a tabuada de 1 a 10 do valor lido.



numero = int(input("Informe um numero: "))

print('\n Tabuada de', numero, ':')

for i in range(1, 11):

    print(numero, 'x', i, '=', (numero * i))


#Faça um algoritmo em linguagem Python que receba duas notas e calcule a média aritmética e mostre o resultado.

Nota1 = int(input("Informe a primeira nota: "))
Nota2 = int(input("Informe a segunda nota: "))

media = (Nota1 + Nota2)/2

print("A média aritmética é: ", media)

