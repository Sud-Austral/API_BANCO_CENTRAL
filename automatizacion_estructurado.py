import requests
import json
import pandas as pd
import datetime
import sys


def getPass():
    diccionario = {"b":"n","6":"7","n":"m","T":"Y","1":"2","E":"R","U":"I","5":"6","m":",","q":"w"}
    dct = {v: k for k, v in diccionario.items()}
    salida = "n7mY2RI6,7mw"
    salida2 = ""
    for i in salida:
        salida2 = salida2 + dct[i]
    return salida2

#F074.IPC.VAR.Z.Z.C.M

def getPrueba():
    F_Final = datetime.datetime.now() 
    #print(2)
    Fecha_final   = F_Final.strftime("%Y-%m-%d")
    codigo = "F074.IPC.VAR.Z.Z.C.M"
    url = f"https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx?user=169073872&pass={getPass()}&firstdate=2000-01-01&lastdate={Fecha_final}&timeseries={codigo}&function=GetSeries"
    response = requests.get(url)
    #print(5)
    response1 = response.json()
    #print(response1)
    #print(6)
    response2 = response1["Series"]["Obs"]
    #print(7)
    df = pd.DataFrame(response2)
    print(df)

def getData(codigo):
    #print(codigo)
    #print(1)
    F_Final = datetime.datetime.now() 
    #print(2)
    Fecha_final   = F_Final.strftime("%Y-%m-%d")
    #print(3)
    url = f"https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx?user=169073872&pass=3HyzXWj5eSs8&firstdate=2000-01-01&lastdate={Fecha_final}&timeseries={codigo}&function=GetSeries"
    #print(url)
    #print(datetime.datetime.now())
    #print(4)
    response = requests.get(url)
    #print(5)
    response1 = response.json()
    #print(response1)
    #print(6)
    response2 = response1["Series"]["Obs"]
    #print(7)
    df = pd.DataFrame(response2)
    #print(len(df))
    #print(8)
    df.to_excel(f"Data/{codigo}.xlsx", index=False)
    #print(datetime.datetime.now())
    return True

def proceso():
    #ruta = r"Resource/series.xls"
    ruta = r"Resource/Referencia_diaria.xlsx"
    serie = pd.read_excel(ruta)
    
    #for i in serie["Código"]:
    for i in serie["seriesId"][:400]:
        try:
            print(i)
            getData(i)
        except:
            error = sys.exc_info()[1]
            print(error)
    return None

if __name__ == '__main__':
    print("Comenzo...")
    getPrueba()