import math

#lendo todos os valores em uma só linha
valores = input ()

#separando os valores
numeros = valores.split()

#atribuindo cada separação a variável
A = float(numeros[0])
B = float(numeros[1])
C = float(numeros[2])

areaTriangulo = (A * C) / 2.0
areaCirculo = 3.14159 * pow(C, 2)
areaTrapezio = ((A + B) * C) / 2.0
areaQuadrado = pow(B,2)
areaRetangulo = A * B

print(f'TRIANGULO: {areaTriangulo:.3f}')
print(f'CIRCULO: {areaCirculo:.3f}')
print(f'TRAPEZIO: {areaTrapezio:.3f}')
print(f'QUADRADO: {areaQuadrado:.3f}')
print(f'RETANGULO: {areaRetangulo:.3f}')

#outra forma de fazer a leitura e atribuição
#numeros = list(map(float,input().split()))
#A = numeros[0]
#B = numeros[1]
#C = numeros[2]
