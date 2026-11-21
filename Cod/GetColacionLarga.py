def ObtenerColacionLarga(data):
    data = data

    print("*****Se inicia obtencion de Colaciones Largas*****")
    filtrado = data[
        (data.iloc[:, 19].astype(str).str.strip() == "Descanso Largo")  # &
    ]
    print(filtrado)
    filtradoColacionLarga = filtrado.iloc[:, [0, 1, 2, 5, 7, 16, 17, 18, 19]]
    #print(filtradoColacionLarga)
    print(len(filtradoColacionLarga))
    return filtradoColacionLarga