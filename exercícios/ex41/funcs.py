def conta_palavras_unicas_em_um_texto(texto):


    quantidade_palavras_unicas = 0

    palavras_unicas = []

    texto_dividido_em_palavras = texto.split()

    for palavra in texto_dividido_em_palavras:

        if texto.count(palavra) == 1:

            quantidade_palavras_unicas += 1

            palavras_unicas.append(palavra)


    return [quantidade_palavras_unicas, palavras_unicas]