# %%
#INSTALAR LIBRERIAS
!pip install pandas
!pip install numpy
!pip install matplotlib
!pip install seaborn
!pip install openpyxl

# %%
#Importamos librerías requeridas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %%
##convertir archivo de excel a csv 
df.to_csv("DatosFacturación.csv")

# %%
#Convertir en dataframe
df= pd.read_csv('Datos_Facturación.csv')
df

# %%
df.info()

# %%


# %%
#conversion de la columna 

df['CVE_CLPV'] = df['CVE_CLPV'].astype(int)

# %%
##eliminar un signo de la columna 


df['CVE_CLPV']=df['CVE_CLPV'].str.replace('0 0 0 0 0 0 030902060','0')

# %%
#Filtro por objeto
filtro1=df[(df["CVE_CLPV"] > 1000) & (df["CVE_CLPV"] <2000)]
filtro1




# %%
#Convertir archivo filtrado a CSV
filtro1.to_csv("ACTIVIDAD2EJERCICIO1.csv")

# %%

##patra comprobr que sean los datos que dije 
filtro2=filtro1.groupby(['CVE_CLPV'])['CVE_CLPV'].count()
filtro2

# %%
## para excluir 

filtro3=df[ ~((df["CVE_VEND"]==5)& (df["CVE_VEND"]==4) )]

filtro3

# %%
filtro3.to_csv("ACTIVIDAD2EJERCICIO2.csv")

# %%
filtro4=filtro3.groupby(['CVE_VEND'])['CVE_VEND'].count()
filtro4

# %%
##3-FECHA_ENT   (Fechas de “28/02/2022”)

filtro5=df[df["FECHA_ENT"]=="28/02/2022 00:00:00"]

filtro5


# %%
filtro5.to_csv("ACTIVIDAD2EJERCICIO3.csv")

# %%
filtro7=(df[(df["CAN_TOT"] >5951.7) | (df["STATUS"]=="E")])
filtro7

# %%
filtro7.to_csv("ACTIVIDAD2EJERCICIO4.csv")

# %%

#Filtro 
filtro9=df[["CVE_DOC", "FECHA_ENT", "FECHA_VEN", "CAN_TOT"]]
filtro9



# %%
filtro9.to_csv("ACTIVIDAD2EJERCICIO5.csv")

# %%
##6-Solo las filas de 7001-7099
filtro10=df.iloc[7001:7099,:]


filtro10


# %%
filtro10.to_csv("ACTIVIDAD2EJERCICIO6.csv")

# %%
##7-Index


df11= pd.read_csv('Datos_Facturación.csv', index_col=4)
df11
filtro11=df11.loc[[2,1], ["FECHAELAB"]]
filtro11

# %%
filtro11.to_csv("ACTIVIDAD2EJERCICIO7.csv")


