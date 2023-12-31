<h2 align  = center> Análisis de Datos sobre Siniestros Viales en Buenos Aires: Reducción de Víctimas Fatales </h2>   

Los siniestros viales, son los que ocurren sobre la vía y se presenta súbita e inesperadamente, determinado por
condiciones y actos irresponsables potencialmente previsibles, atribuidos a factores humanos,
vehículos preponderantemente automotores, condiciones climatológicas, señalización y caminos,
los cuales ocasionan pérdidas prematuras de vidas humanas y/o lesiones, así como secuelas
físicas o psicológicas, perjuicios materiales y daños a terceros.  

En Argentina, los accidentes de tránsito representan una preocupación significativa debido a su impacto en la seguridad vial y la salud pública. Estos incidentes involucran una amplia gama de situaciones, como colisiones entre vehículos, atropellos a peatones, choques con objetos fijos y otras circunstancias que ocurren en las vías públicas.  

Argentina ostenta uno de los índices más altos de mortalidad producida por siniestros de tránsito y se calcula que 20 personas mueren por día, casi 7.000 fallecidos por año, y más de 120.000 heridos anuales de distinto grado, de acuerdo a un relevamiento de Luchemos por la Vida.


<img src="Imagenes/image.png">  



En otro informe publicado por Luchemos por la Vida, donde se calculó el porcentaje de disminución de muertos desde 1990 hasta 2018, Argentina no registró ningún descenso, mientras que países como España lograron reducir muertes en accidentes de tránsito por un 80 por ciento, bajando el número de 9.032 muertos en 1990 a 1.806 en 2018.    




<img src="Imagenes/image-1.png">  


Fuente: "Mortalidad en Argentina: comparación con otros países", [Luchemos por la vida.](https://www.luchemos.org.ar/es/estadisticas/internacionales/comparacion-de-argentina-con-otros-paises)   




Actualmente, según el censo poblacional realizado en el año 2022, la población de CABA es de 3,120,612 de habitantes en una superficie de 200 km2, lo que implica una densidad de aproximadamente 15,603 hab/km2 [(Fuente)](https://www.argentina.gob.ar/caba#:~:text=Poblaci%C3%B3n%3A%203.120.612%20habitantes%20(Censo%202022)). Sumado a esto, el Julio de 2023 se registraron 12,437,735 de vehículos transitando por los peajes de las autopistas de acceso a CABA [(Fuente)](https://www.estadisticaciudad.gob.ar/eyc/?p=41995). Por lo que la prevención de siniestros viales y la implementación de políticas efectivas son esenciales para abordar este problema de manera adecuada.

# Objetivo  
Elaboración de un proyecto de análisis de datos, con el fin de generar información que le permita tomar medidas necesarias para disminuir la cantidad de victimas ftales de los sinestros viales.


Para ello se pone a disposición datos sobre siniestros viales acontecidos en la Ciudad de Buenos Aires del 2016 al 2021. 

En esta misma línea de pensamiento, se propone implementar KPIs para:
* Reducir en un 10% la tasa de homicidios en siniestros viales de los úlitmos 6 meses, en comparación con la tasa del semestre anterior.
* Reducir en un 7% la cantidad de accidentes mortales de motociclistas en el último año en CABA, con respecto al año anterior.



## Datos y Herramientas  

En el presente proyecto se utilizaron los siguientes datasets, que se obtuvieron de la página web de Buenos Aires:
* Homicidios.xls: Información de los siniestros registrados de 2016 a 2021 en la Ciudad de Buenos Aires, [(Fuente).](https://data.buenosaires.gob.ar/dataset/victimas-siniestros-viales)
* Poblacion_Arg_201X.xls: Datos de los censos de población de los años 2016 a 2021 [(Fuente).](https://data.buenosaires.gob.ar/dataset/estructura-poblacion)
* Semaforos.xls: Información de semáforos, con ubicación geográfica y tipo de luminaria Ciudad de Buenos Aires [(Fuente).](https://data.buenosaires.gob.ar/dataset/semaforos)
* Cámaras-fijas-de-control-vehicular.xls: Listado con ubicación geográfica de las cámaras de control vehicular ubicadas en la Ciudad de Buenos Aires. [(Fuente).](https://data.buenosaires.gob.ar/dataset/camaras-fijas-control-vehicular)



Además, se utilizaron datos poblacionales del INDEC y artículos periodísticos e informativos para tener un conocimiento del contexto.

A su vez, se trabajó con Pyhton Pandas, Matplotlib, Seaborn y SummaryTools para el trabajo de extracción, limpieza, carga y análisis de los datasets.

Finalmente se elaboró un dashboard para facilitar su visualización con la ayuda de PowerBi.  

# Proyecto

## Estructura del repositorio

* data: Carpeta con los datasets trabajados 
* Imagenes: Carpeta con las imagenes utilizadas en los notebooks. 
* 01_ETL: Notebook con la extracción de los datasets y transformaciones. [Ir](01_ETL.ipynb)
* 02_EDA: Notebook con los análisis y transformaciones adicionales al ETL. [Ir](02_EDA.ipynb)
* Tools.py: Contiene las funciones y gráficas utilizadas en las notebooks. [Ir](Tools.py)

## ETL y EDA  

El proyecto se inició con la extracción de los conjuntos de datos de los archivos Excel. El archivo de Homicidios constaba de dos hojas: una con información sobre las Víctimas y otra sobre los Hechos; ambas fueron convertidas en dataframes de pandas. Posteriormente, se procedió a normalizar los nombres de las columnas en ambos dataframes, eliminar aquellas columnas que no se consideraron relevantes para el análisis y realizar una revisión en busca de valores nulos, errores tipográficos e imputación de valores faltantes, en caso de ser necesario. Tras finalizar estas transformaciones (puedes consultar los detalles [aquí](01_ETL.ipynb)), se fusionaron ambas tablas en una única entidad para continuar con el Análisis Exploratorio de Datos (EDA).

En este proceso, se llevó a cabo la validación de los tipos de datos presentes en cada columna de la tabla recién creada y, cuando fue necesario, se realizaron modificaciones pertinentes. Se procedió a la búsqueda y manejo de valores nulos o faltantes (que no necesariamente eran nulos), eliminando registros o imputando valores según el caso. Luego, se identificaron y gestionaron valores atípicos en las variables, así como registros duplicados.


Posteriormente, se generaron varios gráficos (disponibles para su visualización [aquí](02_EDA.ipynb)) con el fin de comprender mejor los datos y comenzar a identificar patrones y tendencias:

Inicialmente se analizó el total de víctimas mortales a lo largo de los años, destacando que el año 2018 fue el año con mayor número de homicidios viales.

Se procedió a examinar las muertes por mes, día de la semana y por hora, observando que los sábados, el mes de diciembre y el horario entre las 5 y 7 am registraron la mayor cantidad de muertes.

Se exploró el perfil de las víctimas, evidenciando que aproximadamente el 70% de las víctimas mortales de los accidentes viales son hombres de entre 20 y 40 años de edad.

Se observó que la Comuna 1 presenta la mayor cantidad de accidentes con resultados mortales por año, aunque esta diferencia no es significativa en comparación con la comuna que ocupa el segundo lugar (Comuna 1 con 25 muertes en 2017 y la Comuna 4 con 18). No obstante, se apreció un descenso en los fallecimientos a partir del año 2018 en todas las comunas, posiblemente influenciado por la Alerta Mundial por el Covid-19 y los meses de cuarentena, los cuales aún impactan en la sociedad.

Se identificó que las víctimas, principalmente, se desplazaban en motocicleta en su rol de conductores, seguidas por los peatones. Además, se notó que los responsables de los accidentes mayormente se desplazaban en automóvil.

Las avenidas fueron identificadas como el lugar principal donde ocurren los accidentes, siendo estos los más frecuentes y no involucrando cruces con otras calles.


## KPIs

En función a lo mencionado anteriormente en el objetivo del proyecto, se plantearon dos objetivos en relación a la disminución de la cantidad de víctimas fatales de los siniestros viales:  

* Reducir en un 10% la tasa de homicidios en siniestros viales de los úlitmos 6 meses, en comparación con la tasa del semestre anterior. Esto calculandose de la siguiente forma:



$Tasa Homicidios en Siniestros Viales = \frac{Hommicidios Último Semestre}{Población Total} * 100,000$ 


En este caso, para el primer semestre del año 2019, la Tasa de homicidios en siniestros viales fue de 1.82 lo que significa que, durante los primeros 6 meses del año 2019, hubo aproximadamente 1.82 homicidios en accidentes de tránsito por cada 100,000 habitantes. Ahora, el objetivo planteado es reducir esta tasa para el siguiente semestre de 2019 en un 10%, esto es 1.60. Cuando se calcula el KPI para este período se obtiene que la Tasa de homicidios en siniestros viales fue de 1.53, lo que significa que para el segundo semestre de 2019 se cumple con el objetivo propuesto.


* Reducir en un 7% la cantidad de accidentes mortales de motociclistas en el último año en CABA, con respecto al año anterior.  


$Tasa homicidios viales en moto = \frac{Homicidios en Moto Año Anterior - Homicidios en Moto Año Actual}{Población Total} * 100$

Para este caso, se toma como año actual al año 2019 y como año anterior al año 2018. En primer lugar, se calculó la Cantidad de accidentes mortales de motociclistas para el año 2018, el cual resultó de -8.00, de esta manera el objetivo a cumplir es de -7.4 (es decir, la reducción del 7% de la cantidad de accidentes para 2018). El calcular la Cantidad de accidentes mortales de motociclistas para el año 2021 resultó de 11.11 lo que significa que cumplió y excedió el objetivo y disminuyó la cantidad de muertes de conductores de motociclistas respecto del 2018.


# Conclusiones

* El año 2018 ha sido el que mayor cantidad de victimas mortales ha registrado representando 18.5% de los fallecimientos totales, seguido por un decenso en el 2019 y 2020.
* Los siniestros sucedieron con mayor frencuencia el mes de Diciembre, los días sábados y domingos por la mañana (5-7am).

* Las victimas mortales son un 76% masculinos, de entre 20 y 40 años.

* El 42% de las victimas son personas que iban en moto, el 37% eran peatones y un 4% eran conductores de un auto. 

* Por parte del acusado, el 30% de las victimas fallecieron al accidentarse contra un auto, un 25% con vehiculos de pasajeros y un 21% con cargas.

* La comuna con más victimas mortales es la Comuna 1 con un 9.6%, lo cual podría ser esperado ya que es donde se reunen tanto Argentinos como turistas y por ende tiende a haber un mayor tráfico vial y peatonal. Sin embargo la comuna 4 no está muy lejos del primer lugar con un 8.3%.

* Las avenidas representan un 61% de los lugares donde ocurren los siniestros mortales, siendo la principal Avenida Gral Paz con un 8.75%.


## Recomiendaciones

Todo lo ya mencionado es coherente con la investigación realizada para el reporte:

Según la Asociación Luchemos por la Vida, en su investigación de [Los comportamientos de los motociclistas](https://www.luchemos.org.ar/es/investigaciones/los-comportamientos-de-los-motociclistas-2 ):
* El 27% de los motociclistas no respeta el semáforo rojo
* El 31% no aminora la velocidad en las esquinas en las cuales pueden encontrarse con otros vehículos y/o peatones.
* El 74% no señaliza sus maniobras de giro.
* El 75% no cede el paso en las sendas peatonales
* El 51% invade las sendas peatonales

Aunque en la ciudad de Buenos Aires el uso de casco alcanza el 82% de los motociclistas, la educación vial de los conductores y el incremento de controles y sanciones a tanto a este grupo como a los automovilistas resultan medidas urgentes para revertir estas pérdidas de vidas y salud, absolutamente evitables.


Por el lado de las victimas peatonales, la recomendación es la siguiente:

Según la Asociación Luchemos por la Vida, en su investigación de [Peatones en riesgo: estudio sobre sendas peatonales](https://www.luchemos.org.ar/es/investigaciones/peatones-en-riesgo-estudio-sobre-sendas-peatonales) y [Peatones en riesgo: estudio faltan semáforos peatonales en la Ciudad de Buenos Aires](https://www.luchemos.org.ar/es/investigaciones/peatones-en-riesgo-estudio-faltan-semaforos-peatonales-en-ciudad-de-buenos-aires):

* El 20% de las sendas peatonales en la Ciudad de Buenos Aires estan incompletas y un 13% No existen.
* El 82% de los semáforos peatonales está incompleto (no están las 16 luces completas) y en el 3% de los cruces no hay semáforo peatonal.

# Contacto
Si tienes preguntas, comentarios o sugerencias, no dudes en ponerte en contacto con nosotros a través de las siguientes vías:

Correo Electrónico: ep.munizc@gmail.com    


¡Gracias!


