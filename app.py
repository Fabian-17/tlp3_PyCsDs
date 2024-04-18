import pandas as pd

def obtener_csv_como_lista():
    # Leer el archivo CSV y almacenar las edades en una lista
    with open('edades.csv', encoding='utf-8') as archivo:
        next(archivo) # Ignorar la primera línea (encabezado)
        edades = [] # Lista para almacenar las edades
        for linea in archivo:
            linea = linea.rstrip("\n") # Eliminar el salto de línea
            edades.append(int(linea)) # Convertir la edad a entero y agregarla a la lista
        return edades

def analisis_estadistico(lista_edades):
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
    df = pd.DataFrame(list(fi_ordenado.items()), columns=['Edad', 'fi'])
    
    # realiza automanticamente la Frecuencia Absoluta Acumulada (Fi)
    df['Fi'] = df['fi'].cumsum()

    # realiza automanticamente la Frecuencia Relativa Simple (ri)
    df['ri'] = (df['fi'] / df['fi'].sum()).round(4)

    # realiza automanticamente la Frecuencia Relativa Acumulada (Ri)
    df['Ri'] = df['ri'].cumsum()

    # realiza automanticamente la Frecuencia Porcentual (pi%)
    df['pi%'] = (df['ri'] * 100).round(2)

    # realiza automanticamente la Frecuencia Porcentual Acumulada (Pi%)
    df['Pi%'] = (df['Ri'] * 100).round(2)
    
    return df

# Obtener la lista de edades del archivo CSV
lista_edades = obtener_csv_como_lista()

# Realizar el análisis estadístico
resultados_estadisticos = analisis_estadistico(lista_edades)

print(resultados_estadisticos)

# Guardar los resultados en el portapapeles
resultados_estadisticos.to_clipboard(index=False)