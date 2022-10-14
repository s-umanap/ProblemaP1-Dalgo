
def leer_P1(archivo):
    
    retorno = list(map(str,open(archivo)))
    longitud = int(retorno[0])
    retorno = retorno[1:longitud+1]
    print(retorno)
    return(retorno)
print(leer_P1("P1.in"))

##Funciones necesarias


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


def identify_letters(Chain,Subchain):
    
    different = []
    for compare in range(0,len(Chain)):
        if compare+1 < len(Chain):
            if Chain[compare]+Chain[compare+1] != Subchain:
                tupla = compare, compare+1
                different.append(tupla)
    
    return different

def all_posibilities(Chain,Subchain,moves):
    pos = identify_letters(Chain, Subchain)
    posibilities = combination(pos, moves)
    list_posibilities =[]
    for x in posibilities:
        list_posibilities.append(x)
    return list_posibilities

def individual_options(Chain,Subchain,moves):
    posibilities=all_posibilities(Chain, Subchain, moves)
    list_posibilities = []
    for x in posibilities:
        for y in x:
            for z in y:
                if z not in list_posibilities:
                    list_posibilities.append(z)
    return list_posibilities

def combinations_of_individual(Chain,Subchain,moves):
    list_options = individual_options(Chain,Subchain,moves)
    combinations = combination(list_options, moves)
    all_posible_moves = []
    for x in combinations:
        all_posible_moves.append(list(x))
    return all_posible_moves

def try_option(Chain,Subchain,hint):
    mayor = total_apariciones(Chain, Subchain)
    for x in hint:
        first= total_apariciones(change(Chain,Subchain[0],x), Subchain)
        second = total_apariciones(change(Chain,Subchain[1],x), Subchain)
        if first > mayor and (first >= second):
            mayor = first
            Chain = change(Chain,Subchain[0],x)
        elif second > mayor and (second>= first):
            mayor = second
            Chain = change(Chain,Subchain[1],x)
    return mayor

def best_option(Chain,Subchain,moves):
    all_combs = combinations_of_individual(Chain, Subchain, moves)
    mayor = 0
    for x in all_combs:
        option = try_option(Chain, Subchain, x)
        if  option > mayor:
            mayor = option
    return mayor

def change(Chain,letter,pos):
    lista = list(Chain)
    lista[pos] = letter
    final=""
    for x in lista:
        final+=x
    return final

def all_positions(Chain,Subchain):
    pos = identify_letters(Chain,Subchain)
    lista = []
    for i in pos:
        for j in i:
            lista.append(j)
    result = []
    for item in lista:
        if item not in result:
            result.append(item)
    
    return result



def combination(tuples, moves):
    pool = tuple(tuples)
    n = len(pool)
    if moves > n:
        return
    indices = list(range(moves))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(moves)):
            if indices[i] != i + n - moves:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, moves):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
