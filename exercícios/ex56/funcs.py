def valida_cpf(cpf):

    numeros_lidos, numeros_necessarios = 0, 11

    posicao, posicao_final = 0, len(cpf) - 1

    numeros_possiveis = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


    tamanho_de_um_cpf_normal = 11

    cpf_sem_numeros = remove_os_pontos_e_traco_do_cpf(cpf)


    if cpf_sem_numeros == cpf_sem_numeros[0] * 11:

        return False

    if len(cpf_sem_numeros) != tamanho_de_um_cpf_normal:

        return False


    if not verifica_os_pontos_e_traco_do_cpf(cpf):

        return False
    

    if not verifica_primeiro_digito_verificador_do_cpf(cpf):

        return False
    
    if not verifica_segundo_digito_verificador_do_cpf(cpf):

        return False    
        

    return True



def remove_os_pontos_e_traco_do_cpf(cpf):

    cpf_apenas_com_numeros = ''


    numeros = ['0', '1', '2', '3', '4', '5',
               '6', '7', '8', '9']
    


    for digito in cpf:

        if digito in numeros:

            cpf_apenas_com_numeros += digito


    return cpf_apenas_com_numeros



def verifica_os_pontos_e_traco_do_cpf(cpf):

    if cpf[3] == "." and cpf[7] == "." and cpf[-3] == "-":

        return True
    
    else:

        return False
    


def verifica_primeiro_digito_verificador_do_cpf(cpf):


    cpf = remove_os_pontos_e_traco_do_cpf(cpf)

    soma = total = resultado = 0

    primeiro_digito_do_cpf = cpf[-2]

    digito = ''

    peso = 10

    for digito in cpf[0:9]:

        soma += (int(digito) * peso)

        peso -= 1

    total = (soma * 10) % 11


    resultado = total


    if resultado >= 10:

        digito = "0"

    else:

        digito = f"{resultado}"


    digito_obtido = digito

    if str(digito_obtido) == primeiro_digito_do_cpf:

        return True
    
    else:

        return False


    



def verifica_segundo_digito_verificador_do_cpf(cpf):


    cpf = remove_os_pontos_e_traco_do_cpf(cpf)

    soma = total = resultado = 0

    digito = ''

    segundo_digito_do_cpf = cpf[-1]

    peso = 11

    for digito in cpf[0:10]:

        soma += (int(digito) * peso)

        peso -= 1

    total = (soma * 10) % 11


    resultado = total


    if resultado >= 10:

        digito = "0"

    else:

        digito = f"{resultado}"


    digito_obtido = digito

    if str(digito_obtido) == segundo_digito_do_cpf:

        return True
    
    else:

        return False

    #return digito

