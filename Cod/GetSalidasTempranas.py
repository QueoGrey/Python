def ObtenerSalidasTempranas(data):
    data = data

    print("*****Se inicia obtencion de Salidas Tempranas*****")
    filtrado = data[
        (data.iloc[:, 23].astype(str).str.strip() == "Sal. Temprana")  # &
    ]
    print(filtrado)
    filtradoSalTemprana = filtrado.iloc[:, [0, 1, 2, 5, 7, 20, 21, 22, 23]]
    #print(filtradoSalTemprana)
    print(len(filtradoSalTemprana))
    return filtradoSalTemprana