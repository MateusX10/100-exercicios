def calcula_mdc(n1, n2):


    resultado = 1


    while resultado != 0:

        resultado = n1 % n2

        n1 = n2

        n2 = resultado if resultado != 0 else n2


    mdc = n2

    return mdc