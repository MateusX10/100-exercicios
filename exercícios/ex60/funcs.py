def calcula_o_tempo_entre_duas_datas(data1, data2):

    from datetime import timedelta, date


    ano_data1 = int(data1[-4:])

    mes_data1 = int(data1[-7:-5])


    dia_data1 =  int(data1[0:2])


    data1_em_data = date(ano_data1, mes_data1, dia_data1)


    ano_data2 = int(data2[-4:])

    mes_data2 = int(data2[-7:-5])

    dia_data2 = int(data2[0:2])

    data2_em_data = date(ano_data2, mes_data2, dia_data2)

 
    diferenca_das_duas_datas = data2_em_data - data1_em_data


    print(f"Diferença entre as datas {data1} e {data2}: {diferenca_das_duas_datas.days} dias")

    #print(f"{ano_data1}-{mes_data1}-{dia_data1}")