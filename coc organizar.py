numeros = int(input("Digite os numeros sorteados: "))
lista = []
#Separa o numero grande de 2 em 2 digitos
while(numeros > 0):
    #Separa os 2 ultimos digitos pelo resto do numero todo por 100
    addlista = ((numeros) % 100)
    #Retira os 2 ultimos numeros
    numeros = int((numeros)//100)
    #Adiciona a lista
    lista.append(addlista)
#Printa a lista de numeros
print("Numeros não organizados: {}".format(lista))
#Organiza em ordem crescente
lista.sort(key=int)
#Printa a lista em ordem crescente
print("Numeros organizados: {}".format(lista))
input("Digite qualquer coisa para fechar")        
        
