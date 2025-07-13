def conta_vogais(frase)->int:


    quantidade_de_vogais_na_frase = 0

    vogais_possiveis = ["a", "e", "i", "o", "u"]


    for letra in frase:

        if letra.lower() in vogais_possiveis:

            quantidade_de_vogais_na_frase += 1


    return quantidade_de_vogais_na_frase

    
        