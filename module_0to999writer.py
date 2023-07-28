
## Funções para o escritor de 0 a 999, código em python feito por Allan Martins Melquiades.

ZEROTOTWN = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez',
            'Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito',
            'Dezenove')

CENTS = ('0','1','Vinte','Trinta','Quarenta','Cinquenta','Sessenta','Setenta','Oitenta','Noventa')

HUNDREDS = ('0','Cento','Duzentos','Trezentos','Quatrocentos','Quinhentos','Seiscentos','Setecentos',
            'Oitocentos','Novecentos')

JUNC = " e "

def user_input():
    try:
     value = int(input("Digite um numero entre 0 e 999: "))
     if value < 0 or value >999:
        print("\nValor fora do escopo(0-999), digite novamente:\n")
        value = int(input("Digite um numero entre 0 e 999: "))

    except ValueError:
        print("Valor fora do escopo(0-999), digite novamente: ")
        value = int(input())

    return value
            
def n_algs(num):
    return len(str(num))

def one_alg(num):
    return ZEROTOTWN[num]

def two_algs(num):
    num_str = str(num)

    if num_str[0] == '1':
        return ZEROTOTWN[int(num_str)]
    
    elif num_str[1] == '0':
        return CENTS[int(num_str[0])]
    
    else:
        return CENTS[int(num_str[0])] + JUNC + ZEROTOTWN[int(num_str[1])]
    
def three_algs(num):
    num_str = str(num)

    if num_str == '100':
        return 'Cem'
   
    elif num_str[1:3] == '00':
        return HUNDREDS[int(num_str[0])]
    
    elif num_str[1] == '1':
        return HUNDREDS[int(num_str[0])]+ JUNC + ZEROTOTWN[int(num_str[1:3])]
    
    elif num_str[1] == '0':
        return HUNDREDS[int(num_str[0])] + JUNC + ZEROTOTWN[int(num_str[2])]
    
    elif num_str[2] == '0':
        return HUNDREDS[int(num_str[0])]+ JUNC + CENTS[int(num_str[1])]
    
    else:
        return HUNDREDS[int(num_str[0])] + JUNC + CENTS[int(num_str[1])] + JUNC + ZEROTOTWN[int(num_str[2])]
    
    
        