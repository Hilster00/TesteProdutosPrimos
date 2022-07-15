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
        limpar()
        print(f"Valor {numero} não é valido")
        

#define o tamanho maximo do primo que será feito o teste
tamanho_numero=len(str(numero))
tamanho_numero="9"*tamanho_numero
tamanho_numero=int(tamanho_numero)+1

#lista de primos inicializada
lista_primos=[2]
proximo=3

#adiciona primos a lista enquanto não chegar ao ultimo numero de n digitos
while True:
    
    #algoritmo para melhor eficienci na hora encontrar os primos
    quantidade=(int(len(lista_primos)/2))
    for n in lista_primos[1:quantidade]:

        if(proximo%n==0):
            break
    else:
        if numero%proximo == 0:
            limpar()
            resultado=int(numero/proximo)
            if resultado== proximo:
                print(f"O número {numero} é produto de {resultado} por ele mesmo")
            else:
               
                for n in range(2,(int(resultado/2))):
                    if resultado%n == 0:
                        print(f"O nuemero {numero} não é produto de dois primos")
                        break
                else:
                    print(f"O primeiro divisor de {numero} é {proximo} e o segundo é {resultado}")
            break
        lista_primos.append(proximo)
    proximo+=2
