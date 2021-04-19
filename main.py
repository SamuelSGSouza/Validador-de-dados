from cpf_cnpj import Documento


documento = ""
validador = Documento.cria_documento(documento)
print(f"CPF confirmado! = {validador}")

from cadastro import DataBR

cadastro = DataBR()
print(f"Tempo de cadastro = {cadastro.tempo_de_cadastro()}")

from cep import Cep

cep1 = ""
objeto = Cep(cep1)
a = objeto.acessa_via_cep()
print(f"Informações de localidade: \n{a}")