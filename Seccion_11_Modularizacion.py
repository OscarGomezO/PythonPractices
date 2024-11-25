#Modularización
#--1
#Proceso de dividir un programa en partes mas pequeñas llamadas modulos o paquetes.

#Beneficios.
#1 Reutilización de código
#2 Mantenimiento mas sencillo
#3 Colaboración Eficiente

#Módulos mas utilizados
# os
# sys
# math
# random
# datetime

#Módulos de terceros
# request
# pandas
# matplitlib
# numpy
# scikit-learn


#--2
#USO DE MÓDULOS
#import datetime as dt
#from datetime import date, datetime

#from datetime import date as d
#from datetime import datdatetime as dt

from datetime import *

#hoy = dt.datetime.now()
#--
#hoy = d.today()
#ahora = dt.now()
#--
hoy = date.today()
ahora = datetime.now()

print(hoy)
print(ahora)


#--3
#PAQUETES
#Los parquetes son las carpetas que contienen módulos



