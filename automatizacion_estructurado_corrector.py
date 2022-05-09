import requests
import json
import pandas as pd
import datetime
import sys
import os

def DescargaMasiva():
    #diario.to_excel("dataEstructurado/diario.xlsx", index=False)
    #mensual.to_excel("dataEstructurado/mensual.xlsx", index=False)
    #trimestral.to_excel("dataEstructurado/trimestral.xlsx", index=False)
    #anual.to_excel("dataEstructurado/anual.xlsx", index=False)
    diario = pd.read_excel("dataEstructurado/diario.xlsx")
    mensual = pd.read_excel("dataEstructurado/mensual.xlsx")
    trimestral = pd.read_excel("dataEstructurado/trimestral.xlsx")
    anual = pd.read_excel("dataEstructurado/anual.xlsx")
    print(diario.columns)
    print(mensual.columns)
    print(trimestral.columns)
    print(anual.columns)  
    return




if __name__ == '__main__':
    print("Comenzo...")
    DescargaMasiva()
