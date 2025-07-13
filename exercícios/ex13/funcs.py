def determina_triangulo(comprimento_lado1, comprimento_lado2, comprimento_lado3)->str:

    if comprimento_lado1 == comprimento_lado2 == comprimento_lado3:

        return "Equilátero" 
    
    elif comprimento_lado1 != comprimento_lado2 != comprimento_lado3 != comprimento_lado1:

        return "Escaleno"
    
    else:

        return "isósceles"