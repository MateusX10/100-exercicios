from funcs import *




cpf = "000.000.000-00"


print(valida_cpf("529.982.247-25"))  # True
print(valida_cpf("123.456.789-09"))  # True
print(valida_cpf("123.456.789-00"))  # False
print(valida_cpf("111.111.111-11"))  # False
print(valida_cpf("390.533.447-05"))  # True
print(valida_cpf("745.376.980-11"))

#print(remove_os_pontos_e_traco_do_cpf(cpf))


#print(verifica_primeiro_digito_verificador_do_cpf(cpf))

#print(verifica_segundo_digito_verificador_do_cpf(cpf))