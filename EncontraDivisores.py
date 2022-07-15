import os

def limpar():
    os.system("cls")

limpar()
#tratamento de erro
while True:
    try:
        #recebe o numero que deseja achar as raizes primas
        numero=input("Digite o número obtido pela multiplicação de dois primos:")
        #transforma o numero recebido em inteiro
        numero=int(numero)
        break
    except:
        print(f"Valor {numero} não é valido")

#define o tamanho maximo do primo que será feito o teste
tamanho_numero=len(str(numero))
tamanho_numero="9"*tamanho_numero
tamanho_numero=int(tamanho_numero)+1

#lista de primos inicializada
lista_primos=[2]
proximo=3

#adiciona primos a lista enquanto não chegar ao ultimo numero de n digitos
while proximo<tamanho_numero:
    
    #algoritmo para melhor eficienci na hora encontrar os primos
    quantidade=int(len(lista_primos)/2)
    for n in lista_primos[1:quantidade]:

        if(proximo%n==0):
            break
    else:
        lista_primos.append(proximo)
    proximo+=2
    
limpar()
#verifica se o numero pertence aos primos
if numero not in lista_primos:
    
    for n in lista_primos:
        #divisões consecutivas até achar o primeiro divisor
        if numero%n==0:
            #faz verificações com base no resultado da divisão
            if int(numero/n) not in  lista_primos:
                #não é produto de dois primos pois o resultado da divisão não é primo
                print(f"O nuemero {numero} não é produto de dois primos")                                                  
            else:
                #verifica se o resultado da divisão é o proprio n ou outro primo
                if (numero/n) == n:
                    #numero é n^2
                    print(f"O número {numero} é produto de {n} por ele mesmo")
                else:
                    #numero é n*m
                    print(f"O primeiro divisor de {numero} é {n} e o segundo é {numero/n:.0f}")
            
            break   
else:
    print(f"O número {numero} é primo")
