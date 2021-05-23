from cpf_cnpj import Documento

#Exemplo de utilização do validador
#aqui como valor de 'documento' deve ser inserido o cpf que deseja validar
documento = ""
validador = Documento.cria_documento(documento)
print(f"CPF confirmado! = {validador}")

from cadastro import DataBR
#exibindo tempo de cadastro
cadastro = DataBR()
print(f"Tempo de cadastro = {cadastro.tempo_de_cadastro()}")

from cep import Cep
#exibindo informações sobre cpf
cep1 = ""
objeto = Cep(cep1)
a = objeto.acessa_via_cep()
print(f"Informações de localidade: \n{a}")