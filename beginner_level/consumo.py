# Calcule o consumo médio de um automóvel sendo fornecidos a distância total percorrida (em Km) e o total de combustível gasto (em litros).
# Apresente o valor que representa o consumo médio do automóvel com 3 casas após a vírgula, seguido da mensagem "km/l".

X = int(input()) # Distância total percorrida em km
Y = float(input()) # Total de combustível gasto

consumo = X / Y # Cálculo de consumo médio do automóvel

print(f'{consumo:.3f} km/l')
