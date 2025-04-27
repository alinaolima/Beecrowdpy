linha1 = input()
linha2 = input()

valores1 = linha1.split() #separando os valores da linha de entrada
valores2 = linha2.split()

codigo1 = int(valores1[0]) #declarando os tipos das variaveis
quant1 = int(valores1[1])
valor1 = float(valores1[2])
codigo2 = int(valores2[0])
quant2 = int(valores2[1])
valor2 = float(valores2[2])

valorFinal = ((quant1 * valor1) + (quant2 * valor2))

print(f'VALOR A PAGAR: R$ {valorFinal:.2f}')
