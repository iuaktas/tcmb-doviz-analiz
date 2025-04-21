
import requests
import xml.etree.ElementTree as ET
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def veri_cek():
    url = "https://www.tcmb.gov.tr/kurlar/today.xml"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    return response

def veri_isle(response):
    if response.status_code == 200:
        tree = ET.ElementTree(ET.fromstring(response.content))
        root = tree.getroot()
        data = []
        for currency in root.findall("Currency"):
            code = currency.get("CurrencyCode")
            name = currency.find("Isim").text
            forex_buying = currency.find("ForexBuying").text
            forex_selling = currency.find("ForexSelling").text
            data.append({
                "Code": code,
                "Name": name,
                "ForexBuying": float(forex_buying.replace(',', '.')) if forex_buying else None,
                "ForexSelling": float(forex_selling.replace(',', '.')) if forex_selling else None
            })
        return pd.DataFrame(data)
    else:
        print(f"Veri Çekilemedi! HTTP Kod: {response.status_code}")
        return None

def veriyi_kaydet(df):
    today = datetime.now().strftime('%Y-%m-%d')
    df.to_csv(f"tcmb_doviz_kurlari_{today}.csv", index=False)
    print(f"Veriler basariyla kaydedildi: tcmb_doviz_kurlari_{today}.csv")

def grafik_ciz(df):
    secili_kurlar = df[df["Code"].isin(["USD", "EUR", "GBP"])]
    plt.figure(figsize=(8, 5))
    plt.bar(secili_kurlar["Code"], secili_kurlar["ForexBuying"], color=["skyblue", "orange", "green"])
    plt.title("Güncel Döviz Alış Kurları (TCMB)")
    plt.ylabel("TL")
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

def main():
    response = veri_cek()
    df = veri_isle(response)
    if df is not None:
        veriyi_kaydet(df)
        grafik_ciz(df)

if __name__ == "__main__":
    main()
