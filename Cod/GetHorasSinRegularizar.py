def ObtenerHorasSinRegularizar(data):
    data = data
    print("Inicia obtención de horas sin regularizar")
    filtrado = data[
       # (data.iloc[:, 11].astype(str).str.strip() == "Ent. Atrasada") &
       # (data.iloc[:, 21].astype(str).str.strip() == "Sal. Atrasada")
        (data.iloc[:, 11].astype(str).str.strip() == "Ent. Atrasada") #&
        #(data.iloc[:, 3].astype(str).str.strip() == "FT")
        ]
    print(filtrado)
    print(filtrado.iloc[:, 23].to_string())
    filtrado = filtrado[
       # (data.iloc[:, 11].astype(str).str.strip() == "Ent. Atrasada") &
        (data.iloc[:, 23].astype(str).str.strip() == "Sal. Atrasada")
        #(data.iloc[:, 11].astype(str).str.strip() == "Ent. Atrasada") #&
        #(data.iloc[:, 3].astype(str).str.strip() == "FT")
        ]
    print(filtrado)

    #FiltradoHSR = filtrado.iloc[:, list(range(0, 2)) + list(range(5)) + list(range(20, 24))]
    filtradoHSR = filtrado.iloc[:, [0, 1, 2, 5, 7, 8, 9, 10, 11, 20, 21, 22, 23]]
    #print(filtradoHSR)
    print(len(filtradoHSR))
    return filtradoHSR


