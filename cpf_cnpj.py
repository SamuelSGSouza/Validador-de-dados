#Importando pacote python para tratamento de documentos
from validate_docbr import CPF, CNPJ

#Criando classe que vai determinar o tipo de documento inserido
class Documento:

    @staticmethod
    def cria_documento(documento):
        #pegando valor digitado e transformando em texto
        doc = str(documento)
        #verificando quantidade de dígitos informados
        #caso tenha 11 dígitos é um cpf
        if len(doc) == 11:
            #chamando função para tratamento de cpf
            return DocCPF(doc)
        #se tiver 14 dígitos é cnpj
        elif len(doc) == 14:
            #chamando função para tratamento de cnpj
            return DocCNPJ(doc)
        #caso não possua a quantidade de dígitos de nenhum dos dois documentos, retorna erro de quantidade de dígitos
        else:
            raise ValueError("Quantidade de dígitos inválida!!!")
#definindo classe que irá tratar e retornar valor co cpf
class DocCPF:
    def __init__(self, documento):
        self.documento = documento
        # chamando função para definir se o documento informado é válido
        if self.cpf_e_valido():
            self.cpf = self.documento
        #caso seja inválido retorna mensagem de erro
        else:
            raise ValueError("CPF inválido!!!")

    #criando função para utilizar biblioteca do python para validação de documentos
    def cpf_e_valido(self):
        #validadando documento. caso seja válido retorna True senão retorna False
            validado = CPF().validate(self.documento)
            return validado

    #definindo valor string da classe
    def __str__(self):
        return self.formata_documento()

    #criando função para adicionar máscara ao documento para deixá-lo no formato padrão 999.999.999-99
    def formata_documento(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

#definindo classe que irá tratar e retornar valor co cnpj
class DocCNPJ:
    def __init__(self, documento):
        self.documento = documento
        # chamando função para definir se o documento informado é válido
        if self.cnpj_e_valido():
            self.cnpj = self.documento
        # caso seja inválido retorna mensagem de erro
        else:
            raise ValueError("CNPJ inválido!!!")

    # criando função para utilizar biblioteca do python para validação de documentos
    def cnpj_e_valido(self):
        validado = CNPJ().validate(self.documento)
        return validado

    # definindo valor string da classe
    def __str__(self):
        return self.formata_documento()

    #criando função para adicionar máscara ao documento para deixá-lo no formato padrão 999.999.999-99
    def formata_documento(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
