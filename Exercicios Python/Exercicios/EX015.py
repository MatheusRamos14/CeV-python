KM=float(input('Quantos quilometros vc percorreu?'))
D=int(input('Por quantos dias vc alugou o veiculo?'))
P=(60*D)+(0.15*KM)
print('O valor a ser pago pelo aluguel é de R${:.2f}'.format(P))

