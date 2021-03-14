N1 = int(input('\033[41mDigite um numero:'))
N2 = int(input('\033[45mDigite outro numero:\033[m'))
R = N1+N2
print('A soma entre \033[35m{}\033[m e \033[31m{}\033[m é igual a \033[1;36m{}'.format(N1, N2, R))
