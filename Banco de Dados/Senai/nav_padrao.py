import os
import time
from datetime import datetime


def limpar_tela(): # Criando método
    os.system("cls")

def delay():
    time.sleep(2)

def converter_data(data_original): # YYYY/MM/DD -> DD/MM/YYYY
    if data_original is not None:
        data_formatada = data_original.strftime('%d/%m/%Y')
        return data_formatada

def converter_data_banco(data_inserida): # DD/MM/YYYY -> YYYY/MM/DD
    data_convertida = datetime.strptime(data_inserida, "%d/%m/%Y")
    data_formatada = data_convertida.strftime("%Y-%m-%d")
    return data_formatada