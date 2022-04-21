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

def getSeries():
    serie = pd.read_excel(r"dataEstructurado/series.xls")
    return serie
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
    df.to_excel("text.xlsx")
    print(df)

def getData2(codigo, password):
    #print(codigo)
    url = f"https://si3.bcentral.cl/SieteRestWS/SieteRestWS.ashx?user=169073872&pass={password}&firstdate=2000-01-01&lastdate=2021-12-31&timeseries={codigo}&function=GetSeries"
    response = requests.get(url)    
    response1 = response.json()
    response2 = response1["Series"]["Obs"]
    #return pd.DataFrame(response2) #.to_csv(f"{codigo}.csv", index=False)
    df = pd.DataFrame(response2)
    df["Codigo"] = codigo
    return df

def DescargaMasiva():
    serie = getSeries()
    password = getPass()
    fechas = []
    start =  datetime.datetime(2000,1,1)
    now = datetime.datetime.now()
    actual = start
    while actual < now:
        fechas.append(actual.strftime("%d-%m-%Y"))
        actual = actual +  datetime.timedelta(days = 1)
        referenciaFecha = pd.DataFrame({"Fecha":fechas})
    diario = referenciaFecha
    mensual = referenciaFecha
    trimestral = referenciaFecha
    anual = referenciaFecha
    error = []
    n = 1
    for i in serie["Código"]:
        frecuencia = i.split(".")[-1]
        #print(frecuencia)
        df = getData2(i,password)
        if(len(df) == 0):
            error.append(i)
        else:
            print(i)
            print(f"Llevamos {n} de {len(serie)}")
            n = n + 1
            if(frecuencia == "D"):        
                diario = diario.merge(df, left_on="Fecha", right_on="indexDateString", how="left")
                diario[i] = diario["value"] 
                del diario["value"]
                del diario["statusCode"]
                del diario["Codigo"]
            """
            elif(frecuencia == "M"):
                mensual = mensual.merge(df, left_on="Fecha", right_on="indexDateString", how="left")
                mensual[i] = mensual["value"] 
                del mensual["value"]
                del mensual["statusCode"]
                del mensual["Codigo"]
            elif(frecuencia == "T"):
                trimestral = trimestral.merge(df, left_on="Fecha", right_on="indexDateString", how="left")
                trimestral[i] = trimestral["value"] 
                del trimestral["value"]
                del trimestral["statusCode"]
                del trimestral["Codigo"]
            elif(frecuencia == "T"):
                anual = anual.merge(df, left_on="Fecha", right_on="indexDateString", how="left")
                anual[i] = anual["value"] 
                del anual["value"]
                del anual["statusCode"]
                del anual["Codigo"]
            """
    diario.to_excel("dataEstructurado/diario.xlsx", index=False)
    #mensual.to_excel("dataEstructurado/mensual1.xlsx", index=False)
    #trimestral.to_excel("dataEstructurado/trimestral1.xlsx", index=False) 
    #anual.to_excel("dataEstructurado/anual1.xlsx", index=False)
    return


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
    DescargaMasiva()