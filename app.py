import pandas as pd
from calculos import calcular_Fi, calcular_ri, calcular_Ri, calcular_pi, calcular_Pi 

def obtener_csv_como_lista():
    # Leer el archivo CSV y almacenar las edades en una lista
    with open('edades.csv', encoding='utf-8') as archivo:
        next(archivo) # Ignorar la primera línea (encabezado)
        edades = [] # Lista para almacenar las edades
        for linea in archivo:
            linea = linea.rstrip("\n") # Eliminar el salto de línea
            edades.append(int(linea)) # Convertir la línea a entero y añadir a la lista
        return edades


# Obtener la lista de edades del archivo CSV
lista_edades = obtener_csv_como_lista()


def calcular_fi(lista_edades):
    fi = {} # Diccionario para almacenar las frecuencias absolutas simples
    # Calcular las frecuencias absolutas simples
    for i in lista_edades:
        if i in fi:
            fi[i] += 1
        else:
            fi[i] = 1
    # Ordenar el diccionario por las claves (edades) de menor a mayor
    fi_ordenado = dict(sorted(fi.items()))
    
    # Crear DataFrame con las frecuencias absolutas
    df = pd.DataFrame(list(fi_ordenado.items()), columns=['Edades', 'fi'])
    
    return df

def analisis_estadistico(lista_edades):
    # Verifica si la lista de edades esta vacia o no es una lista
    if not isinstance(lista_edades, list) or not lista_edades:
        return "La lista de edades proporcionada no es válida."

    # Calcular las frecuencias
    df = calcular_fi(lista_edades)
    
    # Realizar los cálculos adicionales
    df = calcular_Fi(df)
    df = calcular_ri(df)
    df = calcular_Ri(df)
    df = calcular_pi(df)
    df = calcular_Pi(df)
    
    # Devolver el DataFrame como un diccionario
    return df.to_dict(orient='list')


# Realizar el análisis estadístico
resultados_estadisticos = analisis_estadistico(lista_edades)

print(resultados_estadisticos)