# Escreva um programa para ler o raio de um círculo, calcular e escrever a sua área.


import math

raio=float (input('Informe o raio:'))

if raio>=0:
    area=math.pi*raio**2
    print('A area do circulo é ',area,'cemtimetros quadrados!')
else:
    print('O raio informado nao e correto!')