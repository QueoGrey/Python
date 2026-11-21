import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

def ObtenerDestinatariosCorreos(tienda, rutaDestinatarios):
    tienda = tienda
    rutaDestinatarios = rutaDestinatarios


    # Aqui se realiza
    df = pd.read_excel(rutaDestinatarios, sheet_name="Hoja1", usecols="A:F")
    print(df)

    filtradoTienda = df[
        (df.iloc[:, 1].astype(str).str.strip() == tienda)
        ]
    print(filtradoTienda)

    filtradoPara = filtradoTienda[
        (filtradoTienda.iloc[:, 2].astype(str).str.strip() == "PARA")
    ]
    print(filtradoPara)
    filtradoCC = filtradoTienda[
        (filtradoTienda.iloc[:, 2].astype(str).str.strip() == "COPIA")
    ]
    print(filtradoCC)

    #Filtrar solo correo PARA
    listCorreoPara = filtradoPara.iloc[:, 5]
    print (listCorreoPara)

    #Filtrar solocorreos CC
    listCorreoCC = filtradoCC.iloc[:, 5]
    print(listCorreoCC)

    #Armar variable de correos PARA  y CC
    cadena_correos_para = ";".join(listCorreoPara.astype(str))
    cadena_correos_cc = ";".join(listCorreoCC.astype(str))
    print(cadena_correos_para)
    print(cadena_correos_cc)


    return cadena_correos_para, cadena_correos_cc

