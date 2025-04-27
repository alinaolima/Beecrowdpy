nome = input()
salario = float(input())
totalVendas = float(input()) #em dinheiro

salarioFinal = (salario + (totalVendas * (15/100)))

print(f'TOTAL = R$ {salarioFinal:.2f}')
