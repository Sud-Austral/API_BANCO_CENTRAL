import requests
import json
import pandas as pd
import datetime
import sys
import os

def limpiarData(texto):
    try:
        num = int(texto)
        num = str(num).replace(".",",")
        return num
    except:
        return None

def DescargaMasiva():
    #diario.to_excel("dataEstructurado/diario.xlsx", index=False)
    #mensual.to_excel("dataEstructurado/mensual.xlsx", index=False)
    #trimestral.to_excel("dataEstructurado/trimestral.xlsx", index=False)
    #anual.to_excel("dataEstructurado/anual.xlsx", index=False)
    diario = pd.read_excel("dataEstructurado/diario.xlsx")
    mensual = pd.read_excel("dataEstructurado/mensual.xlsx")
    trimestral = pd.read_excel("dataEstructurado/trimestral.xlsx")
    anual = pd.read_excel("dataEstructurado/anual.xlsx")

    for i in diario.columns[1:]:
        print(i)
        diario[i] = diario[i].apply(limpiarData)

    for i in mensual.columns[1:]:
        print(i)
        mensual[i] = mensual[i].apply(limpiarData)

    for i in trimestral.columns[1:]:
        print(i)
        trimestral[i] = trimestral[i].apply(limpiarData) 

    for i in anual.columns[1:]:
        print(i)
        anual[i] = anual[i].apply(limpiarData)  

    diario.to_csv("dataEstructurado/diario.csv", index=False)
    mensual.to_csv("dataEstructurado/mensual.csv", index=False)
    trimestral.to_csv("dataEstructurado/trimestral.csv", index=False)
    anual.to_csv("dataEstructurado/anual.csv", index=False)
      
    return




if __name__ == '__main__':
    print("Comenzo...")
    DescargaMasiva()
