# Realiza el calculo para la frecuencia absoluta Acumulada
def calcular_Fi(df):
    df['Fi'] = df['fi'].cumsum()
    
    return df

# Realiza el calculo para la frecuencia relativa Simple
def calcular_ri(df):
    df['ri'] = (df['fi'] / df['fi'].sum()).round(4)

    return df

# Realiza el calculo para la frecuencia relativa Acumulada
def calcular_Ri(df):
    df['Ri'] = df['ri'].cumsum()

    return df

# Realiza el calculo para la frecuencia porcentual Simple
def calcular_pi(df):
    df['pi%'] = (df['ri'] * 100).round(2)

    return df

# Realiza el calculo para la frecuencia porcentual Acumulada
def calcular_Pi(df):
    df['Pi%'] = (df['Ri'] * 100).round(2)

    return df
