#Executável das funções do escritor de 0 a 999, criado por Allan Martins Melquiades.

from module_0to999writer import *

valor = user_input()
nums = n_algs(valor)

if nums == 1:
    print(one_alg(valor)+'\n')

elif nums == 2:
    print(two_algs(valor)+'\n')

elif nums == 3:
    print(three_algs(valor)+'\n')

else:
    pass
