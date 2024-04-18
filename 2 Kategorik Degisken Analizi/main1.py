#####################################################################
# 2. Kategorik Degisken Analizi (Analysis of Categorical Variables)
#####################################################################

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("titanic")
df.head()

df["embarked"].value_counts() # embarked degiskeninde kac adet sinif var ve bu siniflarda kac adet degisken var
df["sex"].unique() # unique(benzersiz) degerleri dondurur.
df["sex"].nunique() # bu ise kac tane unique(benzersiz) deger oldugunu dondurur.


cat_cols = [col for col in df.columns if str(df[col].dtypes) in ["category", "object", "bool"]]
# "category", "object", "bool" tipinde olan kolonları aldık ve cat_cols listesine koyduk

print(df["sex"].dtypes)
print(str(df["sex"].dtypes))

num_but_cat = [col for col in df.columns if df[col].nunique() < 10 and df[col].dtypes in ["int64", "float64"]]
# tipi int yada float olduğu halde benzersiz değişken sayısı 10 adetin altında olan degişkenleri aldık

cat_but_car = [col for col in df.columns if df[col].nunique() > 20 and str(df[col].dtypes) in ["category", "object"]]
# cardinality'si yüksek değişkenleri bulduk, yani veriseti içerisinde çok fazla unique değeri olan değişkenlerdir. Titanic verisetinde bu şekildeki değişkenlerden yokmuş

cat_cols = cat_cols + num_but_cat

cat_cols = [col for col in cat_cols if col not in cat_but_car]
# cat_cols içinde gezdik ve cardinality'si yüksek değişkenleri bunun içinden çıkarttik.

df[cat_cols]
df[cat_cols].nunique()

[col for col in df.columns if col not in cat_cols]
# ana verisetimiz içerisinde cat_cols listemizde olmayan kolonları bulduk

df["survived"].value_counts()
100 * df["survived"].value_counts() / len(df)

def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(), "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("#####################################################################")

# yaptigimiz tum islemleri fonksiyonel hale getirdik.

cat_summary(df, "sex")

for col in cat_cols:
    cat_summary(df, col)

def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(), "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("#####################################################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

cat_summary(df, "sex", plot=True)

for col in cat_cols:
    if df[col].dtypes == "bool":
        print("şasdlkjfşaslkdf")
    else:
        cat_summary(df, col, plot=True)


df["adult_male"].astype(int)

for col in cat_cols:
    if df[col].dtypes == "bool":
        df[col] = df[col].astype(int)
        cat_summary(df, col, plot=True)
    else:
        cat_summary(df, col, plot=True)


#####################################################################


def cat_summary(dataframe, col_name, plot=False):
    if dataframe[col_name].dtypes == "bool":
        dataframe[col_name] = dataframe[col_name].astype(int)

        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(), "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("#####################################################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)

    else:
        print(pd.DataFrame({col_name: dataframe[col_name].value_counts(), "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
        print("#####################################################################")

        if plot:
            sns.countplot(x=dataframe[col_name], data=dataframe)
            plt.show(block=True)


for col in cat_cols:
    cat_summary(df, col, plot=True)


#####################################################################



