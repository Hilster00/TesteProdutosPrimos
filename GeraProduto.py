from random import randint
import os

def limpar():
    os.system("cls")

limpar()

#tratamento de erro
while True:
    try:
        #recebe o numero que deseja achar as raizes primas
        numero=input("Digite o a quantidade de digitos dos primos:")
        #transforma o numero recebido em inteiro
        numero=int(numero)
        break
    except:
        limpar()
        print(f"Valor {numero} não é valido")

#define o tamanho maximo do primo que será feito o teste
tamanho_numero="9"*numero
tamanho_numero=int(tamanho_numero)+1

#lista de primos inicializada
lista_primos=[2]
proximo=3

comeco=0
verificador=0
#adiciona primos a lista enquanto não chegar ao ultimo numero de n digitos
while proximo<tamanho_numero:
    
    #algoritmo para melhor eficienci na hora encontrar os primos
    quantidade=int(len(lista_primos)/2)
    if quantidade < len(lista_primos)/2:
        quantidade+=1
    for n in lista_primos[1:verificador]:
        if(proximo%n==0):
            break
    else:
        lista_primos.append(proximo)
        verificador+=1
        #comeco dos numeros com a quantidade de digitos definido

        if comeco == 0:
            #if alinhado para evitar comparacao e cast desnecessario 
            if(len(str(proximo)) ==numero):
                comeco=len(lista_primos)-1

    proximo+=2
    
limpar()

produto=lista_primos[randint(comeco,len(lista_primos))]*lista_primos[randint(comeco,len(lista_primos))]
print(f"Produto de dois primos {produto}")
