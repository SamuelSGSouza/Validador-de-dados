import requests
class Cep:
    def __init__(self, cep):
        if self.valida_cep(str(cep)):
            self.cep = cep
        else:
            raise ValueError("Cep inválido!!!")

    def valida_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    def __str__(self):
        return self.cep_formatado()

    def cep_formatado(self):
        parte_1 = self.cep[:5]
        parte_2 = self.cep[5:]
        retorno = f'{parte_1}-{parte_2}'
        return retorno

    def acessa_via_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        request = requests.get(url)
        dicionario = request.json()
        dados = f"Cidade - {dicionario['localidade']}\nUF - {dicionario['uf']}\nDDD - {dicionario['ddd']}"
        return dados
