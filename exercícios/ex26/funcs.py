def converte_numero_romano_para_inteiro(numero):


    dicionario = {"I": "1", "V": "5", "X": "10",
                  "L": "50", "C": "100", "D": "500", "M": "1000"}
    

    return dicionario[numero]