import requests
import json
import pandas as pd
import datetime
import sys

def getData(codigo):
    #print(codigo)
    F_Final = datetime.datetime.now() 
    Fecha_final   = F_Final.strftime("%Y-%m-%d")
    url = f"https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx?user=169073872&pass=3HyzXWj5eSs8&firstdate=2000-01-01&lastdate={F_Final}&timeseries={codigo}&function=GetSeries"
    response = requests.get(url)
    response1 = response.json()
    response2 = response1["Series"]["Obs"]
    pd.DataFrame(response2).to_excel(f"Data/{codigo}.xlsx", index=False)
    return True

def proceso():
    ruta = r"Resource/series.xls"
    serie = pd.read_excel(ruta)
    for i in serie["Código"][:3]:
        try:
            print(i)
            getData(i)
        except:
            error = sys.exc_info()[1]
            print(error)

if __name__ == '__main__':
    proceso();