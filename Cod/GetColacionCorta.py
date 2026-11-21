def ObtenerColacionCorta(data):
    data = data

    print("*****Se inicia obtencion de Colaciones cortas*****")
    filtrado = data[
        (data.iloc[:, 19].astype(str).str.strip() == "Descanso Corto")  # &
    ]
    print(filtrado)
    filtradoColacionCorta = filtrado.iloc[:, [0, 1, 2, 5, 7, 16, 17, 18, 19]]
    print(filtradoColacionCorta)
    print(len(filtradoColacionCorta))
    return filtradoColacionCorta