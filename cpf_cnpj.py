from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        doc = str(documento)
        if len(doc) == 11:
            return DocCPF(doc)
        elif len(doc) == 14:
            return DocCNPJ(doc)
        else:
            raise ValueError("Quantidade de dígitos inválida!!!")

class DocCPF:
    def __init__(self, documento):
        self.documento = documento
        if self.cpf_e_valido():
            self.cpf = self.documento
        else:
            raise ValueError("CPF inválido!!!")

    def cpf_e_valido(self):
            validado = CPF().validate(self.documento)
            return validado

    def __str__(self):
        return self.formata_documento()


    def formata_documento(self):
        mascara = CPF()
        return mascara.mask(self.cpf)


class DocCNPJ:
    def __init__(self, documento):
        self.documento = documento
        if self.cnpj_e_valido():
            self.cnpj = self.documento
        else:
            raise ValueError("CNPJ inválido!!!")

    def cnpj_e_valido(self):
        validado = CNPJ().validate(self.documento)
        return validado

    def __str__(self):
        return self.formata_documento()

    def formata_documento(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)
