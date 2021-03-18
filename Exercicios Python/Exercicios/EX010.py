R = float(input('Quantos reais vc tem? R$'))
D = 3.27
C = R//D
RT = R % D
print('Com {}R$, vc pode comprar até {:.2f}US$ e ainda lhe sobram R${:.2f}'.format(R, C, RT))
