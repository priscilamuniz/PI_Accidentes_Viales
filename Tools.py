import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import random
import warnings


def ExtraerPoblacion():
    data_poblacion = {'Anio': [], 'Poblacion': []}

    lista_anios = [2016, 2017, 2018,2019,2020,2021] 

    for anio in lista_anios:
        df_poblacion = pd.read_csv(f'data/Poblacion_Arg_{anio}.csv')
        
        valor_poblacion = df_poblacion.iloc[2, 1]
        
        data_poblacion['Anio'].append(anio)
        data_poblacion['Poblacion'].append(valor_poblacion)

    df_poblacion = pd.DataFrame(data_poblacion)

    return df_poblacion
    

def PorcentajeNulos(df):
    """ 
    Devuelve un resumen del número de registros por columna en un marco de datos, y 
    el porcentaje de valores nulos de cada una. También devuelve
    devuelve el tipo de datos de cada columna.

    Argumentos: 
    df (pandas dataframe): Marco de datos a analizar
    
    """
    tipos = df.dtypes

    df_nulos = pd.DataFrame(tipos, columns=['Data_Types'])
    df_nulos['%_Null'] = round(df.isnull().sum() / len(df) * 100,2)
    df_nulos['Qty_Null'] = round(df.isnull().sum(),2)
    df_nulos['Qty_No_Null'] = round(df.count(),2)
    df_nulos['Total_Registros'] = len(df)
    
    return df_nulos


def DataType(df):
    """ 
    Devuelve
    devuelve el tipo de datos de cada columna.

    Argumentos: 
    df (pandas dataframe): Marco de datos a analizar
    
    """
    tipos = df.dtypes

    df_type = pd.DataFrame(tipos, columns=['TipoDeDato'])
    
    return df_type


def ContarRegistros(df,palabra):
    """ 
    Devuelve el número de apariciones de una palabra o frase dada en los registros de un marco de datos.
    de un marco de datos

    Argumentos:
    df (pandas dataframe): Marco de datos a analizar
    palabra (:str): Palabra a buscar
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


def BoxplotEdadAnio(df):
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(10, 5))
    sns.boxplot(ax=axes[0], x='Edad', data=df)
    axes[0].set_title('Boxplot Edad')
    axes[0].set_xlabel('Edad')

    sns.boxplot(ax=axes[1], x='Anio', data=df)
    axes[1].set_title('Boxplot Años')
    axes[1].set_xlim(2014, 2023)
    axes[1].set_xlabel('Año')

    plt.tight_layout() 
    plt.show()


def BoxplotEdadbyAnio(df):

    plt.figure(figsize=(20, 6))
    sns.boxplot(x='Anio', y='Edad', data=df)
    
    plt.title('Boxplot Edad por Año') ; plt.xlabel('Año') ; plt.ylabel('Edad')

    plt.show()

"""
def DistAnual(df):
    
     
    Devuelve un gráfico violeta de la distribución de las víctimas mortales anuales de accidentes de tráfico

    Argumentos:
    df (pandas dataframe): Dataframe a analizar

    
    sns.violinplot(data = df, x = 'Anio')
    plt.title('Distribución anual de víctimas mortales en accidentes de tráfico')
    plt.xlabel('Año')
    plt.show() 
"""

def VictimaDiaAnio(df):

    # First graph:  
    fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(24, 6))
    orden_meses = [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ]
    df['Mes'] = pd.Categorical(df['Mes'], categories=orden_meses, ordered=True)
    

    month = df.groupby('Mes')['NumVictimas'].sum().reset_index()
    sns.lineplot(data = month, x = 'Mes', y = 'NumVictimas', ax = axes[0])
    axes[0].set_title('Victimas por Mes')
    axes[0].set_xlabel('Mes')
    axes[0].set_ylabel('Victimas')
    axes[0].set_xticklabels(axes[0].get_xticklabels(), rotation=45)


    # Second graph: FatalVictimsByWeeday

    weekday = df.groupby('DiaSemana')['NumVictimas'].sum().reset_index()
    sns.lineplot(data = weekday, x = 'DiaSemana', y = 'NumVictimas', ax = axes[1])
    axes[1].set_title('Victimas por Dia')
    axes[1].set_xlabel('Dia de la semana')
    axes[1].set_ylabel('Victimas')
    plt.xticks(rotation=45) 
        



    # Third graph: FrecuentTimesReported
    groupH = df.groupby('RangoHorario')['NumVictimas'].sum()
    sorted_H = groupH.index.sort_values()

    sns.countplot(data=df, x='RangoHorario', order= sorted_H, ax = axes[2])
    axes[2].set_xlabel('Hora del día')
    axes[2].set_ylabel('Victimas')
    axes[2].set_title('Frecuencia de horas')


    plt.tight_layout() 
    plt.show()



def VictimasAnio(df):
    fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(30, 8))

    orden_meses = [
        'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
        'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'
    ]
    df['Mes'] = pd.Categorical(df['Mes'], categories=orden_meses, ordered=True)

    victimas_mes_anio = df.groupby(['Anio','Mes'])['NumVictimas'].sum().reset_index()    
    years = df['Anio'].unique()

    for i, year in enumerate(years):
        df_year = victimas_mes_anio[victimas_mes_anio['Anio'] == year] 
        sns.lineplot(data=df_year, x='Mes', y='NumVictimas', ax=axes[i//3, i%3])
        axes[i//3, i%3].set_title(str(year))
        axes[i//3, i%3].set_xlabel('Mes')
        axes[i//3, i%3].set_ylabel('Victimas')

    plt.suptitle('Muertes Mensuales por Año', fontsize=16)
    plt.tight_layout() 
    plt.show()



def EdadySexo(df):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))
        
    sns.histplot(x = df['Edad'], kde = True, bins = 20, ax = axes[0])
    axes[0].set_xlabel('Edad')
    axes[0].set_ylabel('Victimas')
    axes[0].set_title('Histogram de Edad 2016-2021')


    conteo_cruce = df['Sexo'].value_counts()
    axes[1].pie(conteo_cruce, labels=conteo_cruce.index, autopct='%1.1f%%')
    axes[1].set_title('Distribución Sexo')

    plt.tight_layout()    
    plt.show()   


def VictimaporAnioporComuna(df):
    plt.figure(figsize = (22,6))
    comuna = df['Comuna'].unique()

    for comuna in df['Comuna'].unique():
        group = df[df['Comuna'] == comuna].groupby(['Anio', 'Comuna'])['NumVictimas'].sum()
        df_group = pd.DataFrame(group)
        sns.lineplot(data=df_group, x='Anio', y='NumVictimas', label=str(comuna))

    plt.title('Victimas por Año y Comuna')
    plt.xlabel('Año')
    plt.ylabel('Victimas')
    plt.legend(title='Comuna')
    plt.show()



def NVictimaporAcusadoNVictimaTypeNRol(df):
    fig, axes = plt.subplots(nrows=1, ncols=3)

    # First graph: Number of Victims by Type of Victim and Gender
    grouped_victims = df.groupby(['Victima', 'Cruce'])['NumVictimas'].sum().unstack()
    sorted_grouped_victims = grouped_victims.sum(axis=1).sort_values(ascending=False).index
    grouped_victims = grouped_victims.loc[sorted_grouped_victims]

    grouped_victims.plot(kind='bar', stacked=True, figsize=(20, 6), ax=axes[0])
    axes[0].set_title('Victimas por Vehiculo Victima y Cruce')
    axes[0].set_xlabel('Vehículo Victima')
    axes[0].set_ylabel('Victimas')
    axes[0].legend(title='Cruce', labels=['Con cruce', 'Sin cruce'])

    # Second graph: VictimsbyAcusedAndGender
    grouped_acused = df.groupby(['Acusado', 'Cruce'])['NumVictimas'].sum().unstack()
    sorted_grouped_acused = grouped_acused.sum(axis=1).sort_values(ascending=False).index
    grouped_acused = grouped_acused.loc[sorted_grouped_acused]

    grouped_acused.plot(kind='bar', stacked=True, figsize=(20, 6), ax=axes[1])
    axes[1].set_title('Victimas por Vehiculo Acusado y Cruce')
    axes[1].set_xlabel('Vehiculo Acusado')
    axes[1].set_ylabel('Victimas')
    axes[1].legend(title='Cruce', labels=['Con cruce', 'Sin cruce'])


    # Third graph:
    grouped_acused = df.groupby(['Rol', 'Cruce'])['NumVictimas'].sum().unstack()
    sorted_grouped_acused = grouped_acused.sum(axis=1).sort_values(ascending=False).index
    grouped_acused = grouped_acused.loc[sorted_grouped_acused]

    grouped_acused.plot(kind='bar', stacked=True, figsize=(20, 6), ax=axes[2])
    labels = grouped_acused.index.tolist()  
    axes[2].set_xticks(range(len(labels))) 
    axes[2].set_xticklabels(labels, rotation=45) 
    axes[2].set_title('Victimas por Rol y Cruce')
    axes[2].set_xlabel('Rol')
    axes[2].set_ylabel('Victimas')
    axes[2].legend(title='Cruce', labels=['Con cruce', 'Sin cruce'])


plt.tight_layout()
plt.show()


def CalleNCruce(df):
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(18, 6))
    sns.countplot(data = df, x = 'TipoDeCalle', ax = axes[0])
    axes[0].set_title('Tipo de calle')
    axes[0].set_ylabel('Victimas')
    axes[0].set_xlabel('Tipo de calle')

    conteo_cruce = df['Cruce'].value_counts()
    axes[1].pie(conteo_cruce, labels=conteo_cruce.index, autopct='%1.1f%%')
    axes[1].set_title('Gráfico de Pastel - Cruce')
    plt.tight_layout()
    plt.show()


def VictimasporParticipante(df):
    group = df.groupby('Participantes')['NumVictimas'].sum().reset_index()
    sort = group.sort_values('NumVictimas', ascending=False)
    plt.figure(figsize = (20,6))
    sns.barplot(x = 'Participantes', y = 'NumVictimas', data = sort)
    plt.xticks(rotation = 45)
    plt.xlabel('Participantes')
    plt.ylabel('Victima')
    plt.title('Victimas por Participantes')
    plt.show()

def VictimasAnioporMes(df):
    plt.figure(figsize=(22, 6))
    comunas = df['Mes'].unique()

    # Paleta personalizada con colores únicos
    colores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#00ffff', '#ff00ff']

    for i, comuna in enumerate(comunas):
        df_group = df[df['Mes'] == comuna].groupby(['Anio', 'Mes'])['NumVictimas'].sum().reset_index()
        sns.lineplot(data=df_group, x='Anio', y='NumVictimas', label=str(comuna), ci=None, color=colores[i])

    plt.title('Víctimas por Año y Mes')
    plt.xlabel('Año')
    plt.ylabel('Víctimas')
    plt.legend(title='Mes')
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



def Semestre(mes):
    primer_semestre = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio']
    return 1 if mes.lower() in primer_semestre else 2


def Pareto_calle(df, dato_analizar):
    """
    Function that returns a Pareto plot.

    Arguments:
    df (pandas dataframe): Data frame to analyze
    dato_analizar (str): Column to analyze
    """

    counts = df[dato_analizar].value_counts()
    df_counts = pd.DataFrame({dato_analizar: counts.index, 'count': counts.values})
    df_counts = df_counts.sort_values(by='count', ascending=False)

    total = df_counts['count'].sum()
    df_counts['porcentaje'] = (df_counts['count'] / total) * 100
    df_counts['acumulado'] = df_counts['porcentaje'].cumsum()

    # Filtrar datos donde el porcentaje acumulado sea menor al 80%
    df_filtered = df_counts[df_counts['acumulado'] < 65]

    fig, ax = plt.subplots(figsize=(12, 6))

    sns.barplot(data=df_filtered, x=dato_analizar, y='count', ax=ax, palette='coolwarm_r')
    plt.xticks(rotation=90)
    plt.title(label='Pareto')
    plt.xlabel(dato_analizar)
    plt.ylabel('Qty')

    ax2 = ax.twinx()
    ax2.plot(df_filtered[dato_analizar], df_filtered['acumulado'], color='red', linestyle='-', linewidth=2.5)
    ax2.set_ylabel('Porcentaje Acumulado')

    #plt.axhline(y=65, color='green', linestyle='--')

    plt.show()


def RangoHorario(valor):
    if 0 <= valor < 6:
        return 'Madrugada'
    elif 6 <= valor < 12:
        return 'Mañana'
    elif 12 <= valor < 18:
        return 'Tarde'
    else:
        return 'Noche'

def RelDiaSemyHora(df):
    plt.figure(figsize=(12, 6))
    sns.countplot(data=df, x='DiaSemana', hue='RangoHorario')
    plt.title('Relación entre Hora y Día de la Semana en Accidentes')
    plt.xlabel('Hora')
    plt.ylabel('Cantidad de Accidentes')
    plt.legend(title='Día de la Semana')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def RelDiaSemyHoraHeatmap(df):
    tabla_frecuencia = df.pivot_table(index='RangoHorario', columns='DiaSemana', aggfunc='size', fill_value=0)

    plt.figure(figsize=(12, 6))
    sns.heatmap(tabla_frecuencia, cmap='viridis')
    plt.title('Relación entre Hora y Día de la Semana en Accidentes')
    plt.xlabel('Día de la Semana')
    plt.ylabel('Hora')
    plt.tight_layout()
    plt.show()