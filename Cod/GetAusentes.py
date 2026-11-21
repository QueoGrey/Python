def ObtenerAusentes(data):
    data = data
    print("*****Se inicia obtencion de Ausentes*****")
    filtrado = data[
        (data.iloc[:, 11].astype(str).str.strip() == "Ausencia")  # &
    ]
    print(filtrado)
    filtradoAusentes = filtrado.iloc[:, [0, 1, 2, 5, 7, 8, 9, 10,11]]
    #print(filtradoAusentes)
    print(len(filtradoAusentes))
    return filtradoAusentes


