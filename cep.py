#importando bibliotecas de requerimento do python
import requests
#criando classe responsável por tratar os CEPs
class Cep:
    def __init__(self, cep):
        #chamando a função para validar o cep
        if self.valida_cep(str(cep)):
            self.cep = cep
        #caso a quantidade de dígitos do cep seja diferente do esperado retornará uma mensagem de erro
        else:
            raise ValueError("Cep inválido!!!")

    #definindo função para validar quantidade de dígitos do cep
    def valida_cep(self, cep):
        if len(cep) == 8:
            return True
        else:
            return False

    #definindo o retorno em string da classe
    def __str__(self):
        return self.cep_formatado()

    #criando máscara para formatar o cep no formato padrão 99999-999
    def cep_formatado(self):
        parte_1 = self.cep[:5]
        parte_2 = self.cep[5:]
        retorno = f'{parte_1}-{parte_2}'
        return retorno

    #acessando site do via cep para retornar o json com os dados sobre o cep informado
    def acessa_via_cep(self):
        url = f"https://viacep.com.br/ws/{self.cep}/json/"
        request = requests.get(url)
        dicionario = request.json()
        dados = f"Cidade - {dicionario['localidade']}\nUF - {dicionario['uf']}\nDDD - {dicionario['ddd']}"
        return dados
