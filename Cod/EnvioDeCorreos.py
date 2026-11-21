import win32com.client as win32
from datetime import datetime

fecha_hoy = datetime.today()

def EnviarCorreoInfo(correo_monitoreo,fecha, correo_para, correo_cc, tienda, dataHSR, dataAus, dataAtr, dataEtem, dataCCorta, dataCLarga, dataSTem, dataSAtr, dataMSTur):
    correo_monitoreo = correo_monitoreo
    fecha = fecha
    correo_para = correo_para
    correo_cc = correo_cc
    tienda = tienda
    dataHSR = dataHSR
    dataAus = dataAus
    dataAtr = dataAtr
    dataEtem = dataEtem
    dataCCorta = dataCCorta
    dataCLarga = dataCLarga
    dataSTem = dataSTem
    dataSAtr = dataSAtr
    dataMSTur = dataMSTur

    #Validar si existen correos

    if len(correo_para) == 0:
        print("Vacío correo para")
        correo_para = correo_monitoreo
    else:
        print("El DataFrame correo PARA tiene datos")

    if len(correo_cc) == 0:
        print("Vacío correo CC")
        correo_cc = correo_monitoreo
    else:
        print("El DataFrame correo CC tiene datos")





    body = f"""
    <html>
    <body style="font-family:Calibri; font-size:11pt;">

    <p><b>*Correo automático, no responder*</b></p>

    <p>-----------------------------------------------------------</p>

    <p>
    Estimados, muy buenos días,
    </p>

    <p>
    Junto con saludar envío pareo con marcajes correspondiente al
    {fecha} {tienda}.
    </p>

    <p>
    *Las entradas tempranas o salidas tardías deben ser autorizadas como horas extras por concepto de bono de asistencia y puntualidad.
    </p>

    <p>
    *Los cambios de turno deben ser entregados con 48 horas de anticipación firmados por el trabajador y jefe de departamento y no más allá de 5 días al pasado. Posterior a eso no se pueden regularizar.
    </p>

    <h3>Horas sin regularizar</h3>

    <p>
    Favor indicar si son horex de entrada y salida o cambios de turno sin ingresar, favor regularizar a la brevedad.
    </p>

    {dataHSR.to_html(index=False)}

    <br>

    <h3>Ausente (Justificar)</h3>

    {dataAus.to_html(index=False)}

    <br>

    <h3>Atrasados (¿Horas administrativas?, justificar)</h3>

    {dataAtr.to_html(index=False)}

    <br>

    <h3>Entradas tempranas (No sobrepasar la legalidad)</h3>

    {dataEtem.to_html(index=False)}

    <br>

    <h3>Colación corta (Recordar que es 1 hora de colación)</h3>

    {dataCCorta.to_html(index=False)}

    <br>

    <h3>Colación larga (Recordar que es 1 hora de colación)</h3>

    {dataCLarga.to_html(index=False)}

    <br>

    <h3>Salidas tempranas (¿Permisos?, ¿Error de marcaje?, ¿Omisión?)</h3>

    {dataSTem.to_html(index=False)}

    <br>

    <h3>Salidas atrasadas (No sobrepasar la legalidad)</h3>

    {dataSAtr.to_html(index=False)}

    <br>

    <h3>Marca sin turno (Justificar)</h3>

    {dataMSTur.to_html(index=False)}

    <br><br>

    <p>
    Recuerde enviar sus observaciones a JDR con copia a CPT.
    </p>

    <p>
    Atte.<br>
    Gerencia de Productividad
    </p>

    </body>
    </html>
    """



    outlook = win32.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)

    mail.To = correo_para
    mail.Cc = correo_cc
    mail.Subject = f'{fecha} :: {tienda}'

    mail.HTMLBody = body

    #mail.Display()   # Muestra el correo

    mail.Send()    # Envía directamente



def EnviarCorreoTerminoProcesamiento(correo_monitoreo, fecha, ruta_reporte_dia):
    correo_monitoreo = correo_monitoreo
    fecha = fecha
    ruta_reporte_dia = ruta_reporte_dia

    outlook = win32.Dispatch("Outlook.Application")
    mail = outlook.CreateItem(0)

    mail.To = correo_monitoreo
    mail.Subject = f'FIN DEL PROCESAMIENTO PAREO MARCAJE :: {fecha}'

    mail.HTMLBody = "Fin procesamiento"
    # Adjuntar archivo
    mail.Attachments.Add(ruta_reporte_dia)

    #mail.Display()  # Muestra el correo

    mail.Send()  # Envía directamente