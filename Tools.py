import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

def PorcentajeNulos(df):
    
    porcentaje_nulos = round(df.isnull().sum() / len(df) * 100,2)
    df_nulos = pd.DataFrame(porcentaje_nulos, columns=['%_valores_nulos'])
    df_nulos['Cantidad_Nulos'] = round(df.isnull().sum(),2)
    df_nulos['Cantidad_NO_Nulos'] = round(df.count(),2)
    df_nulos['Total_Registros'] = len(df)
    
    return df_nulos

def ContarRegistros(df,palabra):
    """ 
    Devuelve la cantidad de veces que está cierta palabra o frase en los registros
    de un dataframe

    Argumentos:
    df (Dataframe de pandas): Dataframe sobre el cual se quiere la información
    palabra (:str): Palabra a buscar
 
    """
    cantidad = (df == palabra).sum()
    nombre_columna = f"Cantidad de {palabra}"
    df_SD = pd.DataFrame(cantidad, columns=[nombre_columna])
    df_SD[f'%_de_{palabra}'] = round(cantidad / len(df) *100,2)
    df_SD['Total_Registros'] = len(df)
    
    return df_SD

def Pareto(df, dato_analizar):
    """
    Es una función que devuelve una gráfica de Pareto tomando un dataframe y la columna a analizar
    """

    counts = df[dato_analizar].value_counts()
    df_counts = pd.DataFrame({dato_analizar: counts.index, 'count': counts.values})                                 # Generamos un df con la cuenta de cada categoria a analizar
    df_counts['acumulado'] = df_counts['count'].cumsum() / df_counts['count'].sum() * 100
    df_counts = df_counts.sort_values(by='count', ascending=False)

    fig, ax = plt.subplots(figsize=(12, 6))                                                                         # Crear la figura y los ejes

    sns.barplot(data=df_counts, x=dato_analizar, y='count', ax=ax, palette='coolwarm_r')                            # Graficamos el barplot de la categoria
    plt.xticks(rotation=90)
    plt.title(label='Pareto')
    plt.xlabel(dato_analizar)
    plt.ylabel('Cantidad')

    ax2 = ax.twinx()                                                                                                # Agregamos la gráfica de línea para el acumulado
    ax2.plot(df_counts[dato_analizar], df_counts['acumulado'], color='red', marker='o', linestyle='-', linewidth=2.5)
    ax2.set_ylabel('Porcentaje acumulado')

    plt.show()

def Proporcion(df, dato_analizar):
    counts = df[dato_analizar].value_counts()
    df_counts = pd.DataFrame({dato_analizar: counts.index, 'count': counts.values})                                  
    df_counts['porcentaje_acumulado'] = round(df_counts['count'].cumsum() / len(df) * 100,2)
    df_counts = df_counts.sort_values(by='count', ascending=False)

    return df_counts

def FatalVictimsperyear(df):
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(30, 8))
    
    victimas_mes_anio = df.groupby(['Anio','Mes'])['NumVictimas'].sum().reset_index()    
    years = df['Anio'].unique()
    
    for i, year in enumerate(years):
        df_year = victimas_mes_anio[victimas_mes_anio['Anio'] == year]  # Convertir 'year' a cadena para coincidir con el tipo de datos
        sns.lineplot(data=df_year, x='Mes', y='NumVictimas', ax=axes[i//3, i%3])
        axes[i//3, i%3].set_title(str(year))
        axes[i//3, i%3].set_xlabel('Month')
        axes[i//3, i%3].set_ylabel('Fatal victims')

    plt.suptitle('Monthly Deaths per Year', fontsize=16)
    plt.tight_layout() 
    plt.show()

def YearlyAccidentDist(df):
    sns.violinplot( x='Anio', data=df)
    plt.title('Yearly Accident Distribution')
    plt.xlim(2014, 2023)
    plt.xlabel('Age')
    plt.show()