import pandas as pd
import os
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

#print(os.path.exists(ruta))
#print(os.path.isfile(ruta))
def obtenerDataRegional(ruta):
    ruta = ruta
    #Aqui se realiza la lectura y obtención de información de regional
    df = pd.read_excel(ruta, sheet_name="PareoMarcajes", usecols="A:Z", skiprows=4)


    #Imprimir información
    #print(df)
    return df


#_______________________Esto se debe hacer en otra clase_________________________

#LLamar funcion
#obtenerDataRegional(r"C:\Users\josec\Documents\WORKPYTHON\PareoMarcaje\Regionales\181126\Regional 1.xlsx")
#print(obtenerDataRegional(r"C:\Users\josec\Documents\WORKPYTHON\PareoMarcaje\Regionales\181126\Regional 1.xlsx"))




