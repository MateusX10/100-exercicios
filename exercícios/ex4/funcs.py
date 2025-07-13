def verifica_se_um_ano_e_bissexto(ano: int)->bool:

    if ano % 4 == 0 and ano % 400 == 0 or ano % 100 != 0:

        return True
    
    else:

        return False
