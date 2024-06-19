import os
import time
from datetime import datetime


def limpar_tela(): # Criando método
    os.system("cls")

def delay():
    time.sleep(2)

def converter_data(data_original):
    if data_original is not None:
        data_formatada = data_original.strftime('%d/%m/%Y')
        return data_formatada
