# - Cuantos numeros negativos hay?, indicar la cantidad y enumerarlos
# - cuanto es la suma de los numeros negativos?
# - cuanto es la suma de los numeros pares?
# - cual es el promedio de los numeros pares
# - cuanto es la suma de los numeros netagivos e impares?

numbers = [2, -5, 28, 33, 7, -8, 57, 88, -13, 0, 9, 14]
numeros_negativos = []
suma_numeros_negativos = 0
suma_numeros_pares = 0
contador_pares = 0
suma_numeros_negativos_e_impares = 0
lista_numeros_impares = []


#usamos un bucle for para recorrer la lista de numeros y poder hacer todos los calculos
for numero in numbers:
    #verificamos si el numero es negativo
    if numero < 0:
        numeros_negativos.append(numero)
        suma_numeros_negativos = suma_numeros_negativos + numero
        
    #verificamos si el numero es par
    if numero % 2 == 0 and numero > 0:
        suma_numeros_pares = suma_numeros_pares + numero  
        # contamos cantidad de numeros pares  para hallar el promedio 
        if numero > 0:
            contador_pares = contador_pares + 1 
    #verificamos si un numero es impar y positivo        
    if numero % 2 != 0 and numero > 0:
        lista_numeros_impares.append(numero)
               
print(f"estos son los numeros negativos : {numeros_negativos} y hay {len(numeros_negativos)}")       
print(f"la suma de los numeros negativos es : {suma_numeros_negativos}")               
print(f"la suma de los numeros pares es : {suma_numeros_pares}")    
print(f"el promedio de los numeros pares es : {suma_numeros_pares // contador_pares}")
suma_numeros_negativos_e_impares = sum(lista_numeros_impares) + sum(numeros_negativos)
print(lista_numeros_impares)
print(f"suma de numeros negativos e impares : {suma_numeros_negativos_e_impares}")
