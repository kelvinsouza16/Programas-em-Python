# Escreva um programa para ler uma temperatura em graus Celsius, calcular e escrever o valor correspondente em graus Fahrenheit.


C=float (input('Informe a temperatura em graus celsius:'))

if C:
    F = (C * 1.8 + 32)
    print('A convercao de ',C,' graus celsius para graus fahrenheit e ',F,'F!')
else:
   print('A convercao de ',0,' graus celsius para graus fahrenheit e ',32,'F!')

