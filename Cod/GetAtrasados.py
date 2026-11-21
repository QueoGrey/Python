def ObtenerAtrasados(data):
    data = data
    print("*****Se inicia obtencion de Atrasados*****")
    filtrado = data[
        (data.iloc[:, 11].astype(str).str.strip() == "Ent. Atrasada")  # &
    ]
    print(filtrado)
    filtradoAtrasados = filtrado.iloc[:, [0, 1, 2, 5, 7, 8, 9, 10, 11]]
    print(filtradoAtrasados)
    print(len(filtradoAtrasados))
    return filtradoAtrasados