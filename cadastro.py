from datetime import datetime, timedelta

class DataBR:
    def __init__(self):
        self._momento_cadastro = datetime.today()
        self._mes_cadastro = self._momento_cadastro.month
        self._dia_semana = self._momento_cadastro.weekday()

    @property
    def mes(self):
        meses = ["", "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
        return meses[self._mes_cadastro]

    @property
    def momento_cadastro(self):
        return self._momento_cadastro.strftime("%d/%m/%Y %H:%M")

    @property
    def dia_semana(self):
        dia_da_semana = [
         "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"
        ]
        return dia_da_semana[self._dia_semana]

    def tempo_de_cadastro(self):
        tempo = (datetime.today() + timedelta(days=30)) - self._momento_cadastro
        return tempo