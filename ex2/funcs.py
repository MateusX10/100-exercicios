def calcula_a_media_de_varios_valores(*valores):
    
    soma_dos_valores = sum(valores)

    quantidade_de_valores = len(valores)

    media = soma_dos_valores / quantidade_de_valores 

    return media