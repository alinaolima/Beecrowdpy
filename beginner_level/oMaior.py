import math

numeros = list(map(int, input().split()))

a = numeros[0]
b = numeros[1]
c = numeros[2]

maiorAB = (a + b + abs(a-b)) / 2
ehmaior = (maiorAB + c + abs(maiorAB-c)) / 2

print(f'{ehmaior:.0f} eh o maior')
