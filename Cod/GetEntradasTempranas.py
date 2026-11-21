def ObtenerEntradasTempranas(data):
    data = data

    print("*****Se inicia obtencion de Entradas tempranas*****")
    filtrado = data[
        (data.iloc[:, 11].astype(str).str.strip() == "Ent. Temprana")  # &
    ]
    print(filtrado)
    filtradoEntradasTempranas = filtrado.iloc[:, [0, 1, 2, 5, 7, 8, 9, 10, 11]]
    print(filtradoEntradasTempranas)
    print(len(filtradoEntradasTempranas))
    return filtradoEntradasTempranas