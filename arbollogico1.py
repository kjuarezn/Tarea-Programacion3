
# Pablo René López Monzón 0910-18-10621
# Kevin Juarez Nieto 0910-13-4579
# William Armando Ovando Melgar 0910-18-157
# Diego Enrique Minerva 1290-14-11947
# Pablo Cesar umul 0910-18-6864
# Marvin Arnoldo Villatoro 0910-18-1261
#array = ["A","(","B","(","E","(K","L"),"C","(","G",")"(","H","("M","),"I","J",")",")",")"]#SI FUNCIONA

import math
array = str (input("Ingrese una cadena: "))  
arbol = list(array)
tamaño = len(array)
nivelop = array.count("(")
nivelcls = array.count(")")
fila = 0
j = 0
aux = 0
aux1 = 0
c = []
imprimiraux = []
imporden = []
print("Cadena: ",arbol,"\n")
print("     Valor       |       Fila        |       Token")
print("-------------------------------------------------------------------------------")
for i in range(tamaño):
    if arbol[i] == "(":            
        aux1 = fila 
        fila += 1 
        if aux1 < fila:
            c.append(fila)
        aux1 = fila 
        print("     ",arbol[i],"                  ",fila,"              Símbolo de agrupación")
    if arbol[i] == ")":
        print("     ", arbol[i],"                  ",aux1,"             Símbolo de agrupación")
        fila -= 1
        aux1 = fila
    if arbol[i] != "(" and arbol[i] != ")" and arbol[i] != "," and arbol[i] != "." and arbol[i] != " ":
        j += 1
        imprimiraux.append(arbol[i])
        imporden.append(aux1) 
        print("     ", arbol[i], "                  ",aux1 ,"             ID:", j,"")
profi = max(c)
print("")
print("Profundidad:   ",profi+1)
print("")
print("")
for x in range(profi+1):
    variables =len(imporden)
    for y in range(variables):
        if imporden[y] == x:
            #print('fila:',x,end="")
            print(' ',imprimiraux[y],' ',end="")
    print("\t fila:",x)
print("")