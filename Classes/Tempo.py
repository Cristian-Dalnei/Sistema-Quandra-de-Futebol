from datetime import datetime, timedelta

import requests
class Tempo:
    climas = {
        0: "Céu limpo",
        1: "Principalmente limpo",
        2: "Parcialmente nublado",
        3: "Nublado",
        45: "Neblina",
        48: "Neblina",
        51: "Garoa fraca",
        53: "Garoa moderada",
        55: "Garoa forte",
        61: "Chuva fraca",
        63: "Chuva moderada",
        65: "Chuva forte",
        80: "Pancadas de chuva fracas",
        81: "Pancadas de chuva moderadas",
        82: "Pancadas de chuva fortes",
        95: "Tempestade",
        96: "Tempestade com granizo"
    }

    @staticmethod
    def consulta_santoangelo():
        data_inicial = datetime.now().date()
        data_final = data_inicial + timedelta(days=4)
        url_string = f"https://api.open-meteo.com/v1/forecast?latitude=-28.30&longitude=-54.26&daily=temperature_2m_max,temperature_2m_min,weather_code&start_date={data_inicial}&end_date={data_final}"
        url = requests.get(url_string)
        dados = url.json()
        return dados['daily']

    @staticmethod
    def dados_santoangelo():
        tabela = Tempo.consulta_santoangelo()
        dicionario = {}
        for i in range(len(tabela['time'])):
            dicionario[i] = {'data': tabela['time'][i],'temp_max': tabela['temperature_2m_max'][i], 'temp_min': tabela['temperature_2m_min'][i], 'codi_tempo': Tempo.climas[tabela['weather_code'][i]]}
        return dicionario

