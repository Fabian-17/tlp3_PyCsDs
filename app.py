import pandas as pd
from calculos import calcular_Fi, calcular_ri, calcular_Ri, calcular_pi, calcular_Pi 

# se declaro la lista
lista_edades = [19,29,19,22,23,19,30,19,19,19,20,20,20,18,22,19,34,34,21,21,22,28,29,19,20,19,25,28,21,22]


def calcular_fi(lista_edades):
    # Convertir la lista de edades en una Serie de pandas
    serie_edades = pd.Series(lista_edades)
    # Calcular la frecuencia absoluta
    fi = serie_edades.value_counts()
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
    
    # Devolver el DataFrame
    return df


# Realizar el análisis estadístico
resultados_estadisticos = analisis_estadistico(lista_edades)

# Imprimir los resultados sin el índice
print(resultados_estadisticos.to_string(index=False))