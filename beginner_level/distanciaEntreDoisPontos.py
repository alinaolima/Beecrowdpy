# Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e 
# calcule a distância entre eles, mostrando 4 casas decimais.

import math # Importando biblioteca

x1, y1 = map(float, input().split()) # Lendo duas variáveis utilizando map e split
x2, y2 = map(float, input().split())

distancia = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2)) # Cálculo da distancia entre os pontos

print(f'{distancia:.4f}')

# input() lê a linha como string.
# map(float, ...) converte cada elemento da lista para float
# .split() divide a string em uma lista de substrings com base nos espaços
