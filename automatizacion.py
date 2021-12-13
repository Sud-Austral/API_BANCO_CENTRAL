import requests
import json
import pandas as pd
import datetime
import sys



def getData(codigo):
    #print(codigo)
    F_Final = datetime.datetime.now() 
    Fecha_final   = F_Final.strftime("%Y-%m-%d")
    url = f"https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx?user=169073872&pass=3HyzXWj5eSs8&firstdate=2000-01-01&lastdate={Fecha_final}&timeseries={codigo}&function=GetSeries"
    #print(url)
    print(datetime.datetime.now())
    response = requests.get(url)
    response1 = response.json()
    #print(response1)
    response2 = response1["Series"]["Obs"]
    df = pd.DataFrame(response2)
    #print(len(df))
    df.to_excel(f"Data/{codigo}.xlsx", index=False)
    print(datetime.datetime.now())
    return True
"""
def proceso():
    #ruta = r"Resource/series.xls"
    ruta = r"Resource/Referencia_diaria.xlsx"
    serie = pd.read_excel(ruta)
    
    #for i in serie["Código"]:
    for i in serie["seriesId"]:
        try:
            print(i)
            getData(i)
        except:
            error = sys.exc_info()[1]
            print(error)
"""
if __name__ == '__main__':
    print("Comenzo...")
    #proceso()