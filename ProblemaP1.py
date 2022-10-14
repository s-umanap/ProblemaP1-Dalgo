#
#
from os import strerror

try:
    ccnt = lcnt = 0
    stream = open("P1.in", "rt", encoding = "utf-8")
    line = stream.readline()
    while line != '':
        lcnt += 1
        for ch in line:
            print(ch, end='')
            ccnt += 1
        line = stream.readline()
    stream.close()
    print("\n\nCharacters in file:", ccnt)
    print("Lines in file:     ", lcnt)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
    
    
    
    
##opcion 2

def leer_P1(archivo):
    
    retorno = list(map(str,open(archivo)))
    longitud = int(retorno[0])
    retorno = retorno[1:longitud+1]
    return(retorno)
print(leer_P1("P1.in"))

## funciones útiles
def chain_and_subchain(Chain,Subchain):
    len_chain = len(Chain); #longitud de la cadena
    len_subchain = len(Subchain); #longitud de la subcadena
     
    apariciones = 0
    if (len_chain == 0 or len_chain < len_subchain):# Caso base 
        apariciones = 0;
        return apariciones;

    if (Chain[0 : len_subchain] == Subchain):#caso recursivo donde se compara slices con la subcadena
        apariciones = chain_and_subchain(Chain[1:],Subchain) + 1; #se va contando la aparición en el caso
        return apariciones;
 
    return chain_and_subchain(Chain[1:],Subchain);#Caso:ya no hay más iteraciones contables, se obtiene el total


def interlaved(Chain,Subchain,posicion):
    
    len_chain = len(Chain);#longitud de la cadena
    occ = 0 #contador de ocurrencias 
    for compare in range(posicion+2,len_chain):#se miran todas las posiciones sin contar la que está pegada, es decir que, 0 y 1 no se comparan
        temporal_chain_pair = Chain[posicion]+Chain[compare] #se crea una subcadena de los chars intercalados
            
        if temporal_chain_pair == Subchain: #se compara la subcadena creada con la original
            occ +=1 #si se cumple el condicional, se suma 1 aparición
    return occ

def all_interlaved(Chain,Subchain):
    total = 0 #total de apariciones de la subcadena en el intercalado
    
    for posicion in range(len(Chain)): #se recorre la cadena y se va reduciendo
        total += interlaved(Chain, Subchain, posicion) #se usa recursivamente la funcion anterior
        #como se va reduciendo,la chain gracias a que vamos avanzando de posiciones, es recurrente
    return total

def total_apariciones(Chain,Subchain): #funcion para sacar el total llamando funciones auxiliares
    cadena_sin_modificaciones = chain_and_subchain(Chain,Subchain)#se mira la cadena recursivamente 1 a 1
    interlaved_total = all_interlaved(Chain,Subchain)#se miran las apariciones de que no se encuentren cercanos
    
    return(cadena_sin_modificaciones + interlaved_total) #total de apariciones sumando lo encontrado por las dos funciones
