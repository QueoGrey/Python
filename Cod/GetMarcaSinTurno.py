def ObtenerMarcaSinTurno(data):
    data = data
    print("*****Se inicia obtencion de Marca sin turno*****")
    filtrado = data[
        (data.iloc[:, 11].astype(str).str.strip() == "Marca sin Turno")  # &
    ]
    print(filtrado)
    filtradoMarcaSinTurno = filtrado.iloc[:, [0, 1, 2, 5, 7, 8, 9, 10,11]]
    #print(filtradoMarcaSinTurno)
    print(len(filtradoMarcaSinTurno))
    return filtradoMarcaSinTurno
