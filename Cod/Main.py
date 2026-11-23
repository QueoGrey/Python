import ObtenerDataDeExcelRegional as odexcel
import GetHorasSinRegularizar as horasSinRegularizar
import GetAusentes as ausentes
import GetAtrasados as atrasados
import GetEntradasTempranas as entradasTempranas
import GetColacionCorta as colacionCorta
import GetColacionLarga as colacionLarga
import GetSalidasTempranas as salidasTempranas
import GetSalidasAtrasadas as salidasAtrasadas
import GetMarcaSinTurno as marcaSinTurno
import EnvioDeCorreos as envioCorreos
import GetDestinatariosCorreos as destinatariosCorreos
import json
import os
from datetime import datetime
import pandas as pd
import GetRegionalFilezilla as regionalFilezilla




##################################
#Obtención de variables externas##
##################################
print(os.getcwd())
with open("../JSON/Config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

ruta_regionales = config["ruta_regionales"]
correo_monitoreo = config["correo_monitoreo"]
fechaHoy = datetime.today().strftime("%d%m%y")
rutaArchivoRegionales = ruta_regionales + fechaHoy
rutaCorreoDestinatarios = config["ruta_destinario"]
ruta_reporte = config["ruta_reporte"]
ruta_reporte_dia = f'{ruta_reporte}\\Reporte_{fechaHoy}.xlsx'

# Crear Excel REPORTE
df = pd.DataFrame()
df.to_excel(ruta_reporte_dia, index=False)
#Agregar valor columnas
df = pd.DataFrame(columns=[
    "Tienda",
    "Status",
    "Fecha",
    "Region",
    "Detalle"
])
df.to_excel(ruta_reporte_dia, index=False)


##################################
#Crear Carpeta dia procesamiento##
##################################

os.makedirs(rutaArchivoRegionales, exist_ok=True)



##################################
###Crear Reporte día ejecución####
##################################





# Se debe iniciar el proceso obteniendo los archivos regionales en SFTP:

#regionalFilezilla.ObtenerArchivosRegionales(rutaArchivoRegionales)





############################
#Obtener lista de Regiones##
############################
archivos = os.listdir(rutaArchivoRegionales)
archivos = [
    archivo
    for archivo in os.listdir(rutaArchivoRegionales)
    if archivo.endswith(".xlsx")
    and not archivo.startswith("~$")
]


    ##############################################################
    ##############################################################
    ###############    INICIO DE PROCESAMIENTO REGIONAL   ########
    ##############################################################
    ##############################################################
for archivo in archivos:
    r_regional_actual = f'{rutaArchivoRegionales}/{archivo}'
    print(r_regional_actual)

    data = odexcel.obtenerDataRegional(r_regional_actual)
    print(data)
    #print(data.iloc[:, 2])





    #Obtener lista de Tiendas
    tiendas = data.iloc[:, 3].unique().tolist()
    print(tiendas)

    #obtener fecha de casos
    fecha = data.iloc[:, 7].unique().tolist()
    print(fecha)






    #########Se inicia filtro de datos y envío de correo de cada tienda#########
    for tienda in tiendas:
        print(tienda)

        #Obtenemos solo informacion de tienda
        dataFilter = data[
            data.iloc[:, 3].astype(str).str.strip() == tienda
            ]
        print(dataFilter)



    ##############################################################
    ##############################################################
    ###############    INICIO FILTRO DATOS     ###################
    ##############################################################
    ##############################################################


        ######### Obtenemos la horas sin regularizar #######
        dataHorasSinRegularizar = horasSinRegularizar.ObtenerHorasSinRegularizar(dataFilter)
        print(dataHorasSinRegularizar)





        ##### Obtenemos los Ausentes ####
        dataAusentes = ausentes.ObtenerAusentes(dataFilter)
        print(dataAusentes)





        ##### Obtención de casos Atrasados ######
        dataAtrasados = atrasados.ObtenerAtrasados(dataFilter)
        print(dataAtrasados)




        ##### Obtención Entradas Tempranas ######
        dataEntradasTempranas = entradasTempranas.ObtenerEntradasTempranas(dataFilter)
        print(dataEntradasTempranas)




        ###### Obtención Colación Corta ###########
        dataColacionCorta = colacionCorta.ObtenerColacionCorta(dataFilter)
        print(dataColacionCorta)



        ###### Obtención Colación Larga ###########
        dataColacionLarga = colacionLarga.ObtenerColacionLarga(dataFilter)
        print(dataColacionLarga)




        ###### Obtención Salida Temprana ##########
        dataSalTempranas = salidasTempranas.ObtenerSalidasTempranas(dataFilter)
        print(dataSalTempranas)




        ###### Obtención Salidas Atrasadas ########
        dataSalAtrasadas = salidasAtrasadas.ObtenerSalidasAtrasadas(dataFilter)
        print(dataSalAtrasadas)




        ###### Marca sin turno ####################
        dataMarcaSinTurno = marcaSinTurno.ObtenerMarcaSinTurno(dataFilter)
        print(dataMarcaSinTurno)



    ##############################################################
    ##############################################################
    ###############   INICIO ENVIO DE CORREOS  ###################
    ##############################################################



        ##### Obtención de destinatarios correos tiendas TO and CC ####
        correo_para, correo_cc = destinatariosCorreos.ObtenerDestinatariosCorreos(tienda, rutaCorreoDestinatarios)




        ##### Enviar correos tiendas ####
        envioCorreos.EnviarCorreoInfo(correo_monitoreo,fecha,correo_para, correo_cc, tienda, dataHorasSinRegularizar, dataAusentes, dataAtrasados, dataEntradasTempranas, dataColacionCorta, dataColacionLarga, dataSalTempranas, dataSalAtrasadas, dataMarcaSinTurno)



        ####################################################
        ############ Registro reporte Reporte ##############
        ####################################################
        try:

            # Procesamiento
            # Envío de correo

            df.loc[len(df)] = [
                tienda,
                "OK",
                fecha,
                archivo,
                "Correo enviado"
            ]

        except Exception as e:

            df.loc[len(df)] = [
                tienda,
                "ERROR",
                fecha,
                archivo,
                str(e)
            ]

        df.to_excel(ruta_reporte_dia, index=False)






    print("Vamos por otra regional")

#Enviar correo termino de procesamiento

envioCorreos.EnviarCorreoTerminoProcesamiento(correo_monitoreo, fechaHoy, ruta_reporte_dia)


