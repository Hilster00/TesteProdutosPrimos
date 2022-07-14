from random import choice

#tratamento de erro
while True:
    try:
        #recebe o numero que deseja achar as raizes primas
        numero=input("Digite o a quantidade de digitos dos primos:")
        #transforma o numero recebido em inteiro
        numero=int(numero)
        break
    except:
        print(f"Valor {numero} não é valido")

#define o tamanho maximo do primo que será feito o teste
tamanho_numero="9"*numero
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
        #comeco dos numeros com a quantidade de digitos definido
        if(len(str(proximo)) ==numero):
            comeco=len(lista_primos)-1
    proximo+=2
    

produto=choice(lista_primos[comeco:len(lista_primos)])*choice(lista_primos[comeco:len(lista_primos)])
print(f"Produto de dois primos {produto}")
