import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random
import warnings

def PorcentajeNulos(df):
    """ 
    Returns a summary of the number of records per column in a dataframe, and 
    the percentage of null values for each. It also returns
    returns the data type of each column.

    Arguments: 
    df (pandas dataframe): Data frame to analyse
    
    """
    tipos = df.dtypes

    df_nulos = pd.DataFrame(tipos, columns=['Data_Types'])
    df_nulos['%_Null'] = round(df.isnull().sum() / len(df) * 100,2)
    df_nulos['Qty_Null'] = round(df.isnull().sum(),2)
    df_nulos['Qty_Not_Null'] = round(df.count(),2)
    df_nulos['Total_Records'] = len(df)
    
    return df_nulos

def ContarRegistros(df,palabra):
    """ 
    Returns the number of occurrences of a given word or phrase in the records of a dataframe.
    of a dataframe

    Arguments:
    df (pandas dataframe): Data frame to analyse
    palabra (:str): Word to search for
 
    """
    cantidad = (df == palabra).sum()
    nombre_columna = f"Qty '{palabra}' "
    df_SD = pd.DataFrame(cantidad, columns=[nombre_columna])
    df_SD[f'%_of_{palabra}'] = round(cantidad / len(df) *100,2)
    df_SD['Total_Records'] = len(df)
    
    return df_SD

def Pareto(df, dato_analizar):
    """
    It is a function that returns a Pareto plot.

    Arguments:
    df (pandas dataframe) : Data frame to analyse
    data_analyse (str) : Column to analyse

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
    plt.ylabel('Qty')

    ax2 = ax.twinx()                                                                                                # Agregamos la gráfica de línea para el acumulado
    ax2.plot(df_counts[dato_analizar], df_counts['acumulado'], color='red', marker='o', linestyle='-', linewidth=2.5)
    ax2.set_ylabel('Cumulative percentage')

    plt.show()

def Proporcion(df, dato_analizar):
    counts = df[dato_analizar].value_counts()
    df_counts = pd.DataFrame({dato_analizar: counts.index, 'count': counts.values})                                  
    df_counts['Cumulative percentage'] = round(df_counts['count'].cumsum() / len(df) * 100,2)
    df_counts = df_counts.sort_values(by='count', ascending=False)

    return df_counts

def FatalVictimsperyear(df):
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(30, 8))
    
    victimas_mes_anio = df.groupby(['Anio','Mes'])['NumVictimas'].sum().reset_index()    
    years = df['Anio'].unique()
    
    for i, year in enumerate(years):
        df_year = victimas_mes_anio[victimas_mes_anio['Anio'] == year] 
        sns.lineplot(data=df_year, x='Mes', y='NumVictimas', ax=axes[i//3, i%3])
        axes[i//3, i%3].set_title(str(year))
        axes[i//3, i%3].set_xlabel('Month')
        axes[i//3, i%3].set_ylabel('Fatal victims')

    plt.suptitle('Monthly Deaths per Year', fontsize=16)
    plt.tight_layout() 
    plt.show()

def FatalVictimsperyearWeekday(df):
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(30, 8))
    
    victimas_mes_anio = df.groupby(['Anio','DiaSemana'])['NumVictimas'].sum().reset_index()    
    years = df['Anio'].unique()
    
    for i, year in enumerate(years):
        df_year = victimas_mes_anio[victimas_mes_anio['Anio'] == year] 
        sns.lineplot(data=df_year, x='DiaSemana', y='NumVictimas', ax=axes[i//3, i%3])
        axes[i//3, i%3].set_title(str(year))
        axes[i//3, i%3].set_xlabel('Weekday')
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

def AnnualDistribution(df):
    
    """ 
    Returns a vioin plot of Distribution of annual road accident fatalities

    Arguments:
    df (pandas dataframe): Dataframe to analyse
    """
    sns.violinplot(data = df, x = 'Anio')
    plt.title('Distribution of annual road accident fatalities')
    plt.xlabel('Year')
    plt.show() 


def AgeHistogram(df):
    plt.figure(figsize = (10,4))
    plt.hist(x = df['Edad'], bins = 20)
    plt.xlabel('Age')
    plt.ylabel('Fatal Victims')
    plt.title('Histogram of Victim Ages 2016-2021')
    plt.show()



def FatalitiesbyWeekdayNYear(df):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 6))
    weekday = df.groupby('DiaSemana')['NumVictimas'].sum().reset_index()
    sns.lineplot(data = weekday, x = 'DiaSemana', y = 'NumVictimas', ax = axes[0])
    axes[0].set_title('Fatal victims by Weekday')
    axes[0].set_xlabel('Weekday')
    axes[0].set_ylabel('Fatal victims')
    plt.xticks(rotation=45) 
        
        
    victimas_anio_weekday = df.groupby(['Anio','DiaSemana'])['NumVictimas'].sum().reset_index()   

    anio = victimas_anio_weekday['Anio'].unique()
    cant_anio = len(anio)
    colores = ['#' + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]) for i in range(cant_anio)]

    for i, year in enumerate(anio):

        data_year = victimas_anio_weekday[victimas_anio_weekday['Anio'] == year]
        x = data_year['DiaSemana']
        y = data_year['NumVictimas']
        
        axes[1].plot(x, y, label=year, color=colores[i], marker='o')

    axes[1].set_title('Fatal victims by Weekday by Year')
    axes[1].set_xlabel('Weekday')
    axes[1].set_ylabel('Fatal victims')
    axes[1].legend()
    plt.tight_layout() 
    plt.show()


def VictimsAndGender(df):
    grouped = df.groupby(['Victima', 'Sexo'])['NumVictimas'].sum().unstack()
    sorted_grouped = grouped.sum(axis=1).sort_values(ascending=False).index
    grouped = grouped.loc[sorted_grouped]

    grouped.plot(kind='bar', stacked=True, figsize=(10, 6))

    plt.title('Number of Victims by Type of Victim and Gender')
    plt.xlabel('Victim "Vehicle"')
    plt.ylabel('Fatal Victims')
    plt.legend(title='Sexo', labels=['Female', 'Male'])
    plt.show()

def VictimsbyAcusedAndGender(df):
    grouped = df.groupby(['Acusado', 'Sexo'])['NumVictimas'].sum().unstack()
    sorted_grouped = grouped.sum(axis=1).sort_values(ascending=False).index
    grouped = grouped.loc[sorted_grouped]

    grouped.plot(kind='bar', stacked=True, figsize=(10, 6))

    plt.title('Number of Victims by Type of Victim and Gender')
    plt.xlabel('Acused "Vehicle"')
    plt.ylabel('Fatal Victims')
    plt.legend(title='Sexo', labels=['Female', 'Male'])
    plt.show()