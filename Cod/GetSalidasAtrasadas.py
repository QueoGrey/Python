def ObtenerSalidasAtrasadas(data):
    data = data

    print("*****Se inicia obtencion de Salidas Atrasadas*****")
    filtrado = data[
        (data.iloc[:, 23].astype(str).str.strip() == "Sal. Atrasada")  # &
    ]
    print(filtrado)
    filtradoSalAtrasada = filtrado.iloc[:, [0, 1, 2, 5, 7, 20, 21, 22, 23]]
    #print(filtradoSalAtrasada)
    print(len(filtradoSalAtrasada))
    return filtradoSalAtrasada