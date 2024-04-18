#############################################
# GELİŞMİŞ FONKSİYONEL KEŞİFÇİ VERİ ANALİZİ (ADVANCED FUNCTIONAL EDA)
#############################################
# 1. Genel Resim
# 2. Kategorik Değişken Analizi (Analysis of Categorical Variables)
# 3. Sayısal Değişken Analizi (Analysis of Numerical Variables)
# 4. Hedef Değişken Analizi (Analysis of Target Variable)
# 5. Korelasyon Analizi (Analysis of Correlation)


#############################################
# 1. Genel Resim
#############################################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("titanic")
######### veri setimizdeki kolon isimlerini anlayalim #########
# survived = hayatta mı değil mi
# pclass = Yolculuk sinifi (int)
# sex = cinsiyet
# age = yas
# sibsp = akraba kisi sayisini ifade eden degiskenler
# parch = akraba kisi sayisini ifade eden degiskenler
# fare = bilet ucreti
# embarked = yolculuga cikilan liman
# class = Yolculuk sinifi (category)
# who = kadin mi erkek mi
# adult_male = yetiskin erkek mi
# deck = güverte
# embark_town = limanin acik sekilde yazilmis ifadesi
# alive = yasiyor mu
# alone = yanliz mi

df.head() # ilk 5 satir
df.tail() # son 5 satir
df.shape # veriseti boyutu
df.info() # veriseti hakkında genel bilgi
df.columns # sutun isimleri
df.index # index numaralandirmasi
df.describe().T # sayısal sütunların istatistiksel özetini verir
df.isnull().values.any() # veriseti icerisinde herhangi bir null deger var mi
df.isnull().sum() # teker teker her sutundaki eksik deger sayilarini dondurur

def check_df(dataframe, head=5):
    print("##################### Shape #####################")
    print(dataframe)
    print("##################### Types #####################")
    print(dataframe.dtypes)
    print("##################### Head #####################")
    print(dataframe.head(head))
    print("##################### Tail #####################")
    print(dataframe.tail(head))
    print("##################### NA #####################")
    print(dataframe.isnull().sum())
    print("##################### Quantiles #####################")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)


check_df(df)

df = sns.load_dataset("tips")
check_df(df)

















