#importando biblioteca de data do python
from datetime import datetime

#criando classe que gerencia data de cadastro
class DataBR:
    def __init__(self):
        #definindo atributos da classe através de métodos da biblioteca datetime
        self._momento_cadastro = datetime.today()
        self._mes_cadastro = self._momento_cadastro.month
        self._dia_semana = self._momento_cadastro.weekday()

    @property
    #definindo função para tratar o mês
    def mes(self):
        #tratando valor retornado em 'month' de número para nome do mês
        meses = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        return meses[self._mes_cadastro]

    @property
    #função que exibe o momento de cadastro no formato brasileiro de datas
    def momento_cadastro(self):
        return self._momento_cadastro.strftime("%d/%m/%Y %H:%M")

    @property
    #definindo função que retorna dia da semana do cadastro
    def dia_semana(self):
        dia_da_semana = [
         "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"
        ]
        return dia_da_semana[self._dia_semana]

    #definindo função que calcula há quanto tempo o usuário está cadastrado
    def tempo_de_cadastro(self):
        tempo = datetime.today() - self._momento_cadastro
        return tempo