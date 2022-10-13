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
    len_chain = len(Chain);
    len_subchain = len(Subchain);  
    apariciones = 0
    
    if (len_chain == 0 or len_chain < len_subchain):# Caso base 
        apariciones = 0;
        return apariciones;

    if (Chain[0 : len_subchain] == Subchain):#caso recursivo donde se compara slices con la subcadena
        apariciones = chain_and_subchain(Chain[1:],Subchain) + 1; #se va contando la aparición en el caso
        return apariciones;
 
    return chain_and_subchain(Chain[1:],Subchain);#Caso:ya no hay más iteraciones contables, se obtiene el total

def first_last(Chain,Subchain):
    
    slic = Chain[0]+Chain[-1] #se hace slice del primer caracter y el último
    inverted = slic[::-1] #se invierte el slice hecho anteriormente
    apariciones = 0
    if (Subchain == slic) or (Subchain == inverted): #se compara con el subchain los dos casos
        apariciones = 1
    return(apariciones)


def total_apariciones(Chain,Subchain): #funcion para sacar el total
    cadena_sin_modificaciones = chain_and_subchain(Chain,Subchain)
    primera_ultima = first_last(Chain,Subchain)
    
    return(cadena_sin_modificaciones + primera_ultima) #llamar a las funciones que se encargan de contar las apariciones de Y en X.

