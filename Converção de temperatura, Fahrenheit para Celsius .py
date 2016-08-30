#Escreva um programa para ler uma temperatura em graus Fahrenheit, calcular e escrever o valor correspondente em graus Celsius.


F=float (input('Informe a temperatura em Fahrenheit:'))

if F:
    C=(F-32)/1.8
    print('A convercao de ',F,'graus fahrenheit para graus celsius e',C,'C!')
else:
    print('A convercao de ', 0, 'graus fahrenheit para graus celsius e', -17.7778, 'C!')
