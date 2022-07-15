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
        if numero >= 2:
            break
    except:
        ...
    limpar()
    print(f"Valor '{numero}' não é valido")
        

#define o tamanho maximo do primo que será feito o teste
tamanho_numero=len(str(numero))
tamanho_numero="9"*tamanho_numero
tamanho_numero=int(tamanho_numero)+1

#lista de primos inicializada
lista_primos=[2]
proximo=3

verificador=0
#adiciona primos a lista enquanto não chegar ao ultimo numero de n digitos
while numero%2!=0:
    
    #algoritmo para melhor eficienci na hora encontrar os primos
    quantidade=(int(len(lista_primos)/2))
    for n in lista_primos[1:verificador]:
        if(proximo%n==0):
            break
    else:
        lista_primos.append(proximo)
        verificador+=1
        if numero%proximo == 0:
            limpar()
            resultado=int(numero/proximo)
            if resultado== proximo:
                # numero/n = n
                print(f"O número {numero} é produto de {resultado}^2")
            elif resultado==1:
                # numero/n == 1
                print(f"O número {numero} é primo")
            else:
                # numero/n == m
                for n in lista_primos[1:verificador]:
                    if(resultado%n==0):
                        # m/n2 == m2
                        print(f"O nuemero {numero} não é produto de dois primos")
                        break
                else:
                    
                    for n in range(lista_primos[verificador],(int(resultado/2)+1)):
                        if resultado%n == 0:
                            # m/n2 == m2
                            print(f"O nuemero {numero} não é produto de dois primos")
                            break
                    
                    else:
                        # m/n2 == 1
                        print(f"O primeiro divisor de {numero} é {proximo} e o segundo é {resultado}")
            break
    proximo+=2

else:
    proximo=2
    limpar()
    if numero == 4:
        print("O número 4 é produto de 2^2")
    elif numero==2:
        print("O número 2 é primo")
    else:
        resultado=int(numero/2)
        for n in range(2,(int(resultado/2)+1)):
            if resultado%n == 0:
                print(f"O nuemero {numero} não é produto de dois primos")
                break
        else:
            print(f"O primeiro divisor de {numero} é {proximo} e o segundo é {resultado}")
