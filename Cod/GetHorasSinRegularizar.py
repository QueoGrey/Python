def ObtenerHorasSinRegularizar(data):
    data = data
    print("Inicia obtención de horas sin regularizar")
    filtrado = data[
        (data.iloc[:, 11].astype(str).str.strip() == "Ent. Atrasada") #&
        ]
    print(filtrado)
    print(filtrado.iloc[:, 23].to_string())
    filtrado = filtrado[
        (data.iloc[:, 23].astype(str).str.strip() == "Sal. Atrasada")
        ]
    print(filtrado)

    print("Antes:", len(filtrado))
    #Se excluyen los casos que contengan externo en la columna nombre
    filtrado = filtrado[
        ~filtrado.iloc[:, 1].astype(str).str.contains("Externo", case=False, na=False)
    ]
    print("Despues:", len(filtrado))
    print(filtrado)
    #FiltradoHSR = filtrado.iloc[:, list(range(0, 2)) + list(range(5)) + list(range(20, 24))]
    filtradoHSR = filtrado.iloc[:, [0, 1, 2, 5, 7, 8, 9, 10, 11, 20, 21, 22, 23]]
    #print(filtradoHSR)
    print(len(filtradoHSR))
    return filtradoHSR


