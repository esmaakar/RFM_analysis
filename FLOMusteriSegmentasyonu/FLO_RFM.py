
import pandas as pd
import datetime as dt
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
df_=pd.read_csv("C:/Users/irem/Desktop/FLOMusteriSegmentasyonu/FLOMusteriSegmentasyonu/flo_data_20k.csv")
df=df_.copy()

df.head(10)
df.columns
df.shape
df.describe().T
df.isnull().sum()
df.dtypes

df["order_num_total"]=df["order_num_total_ever_online"]+df["order_num_total_ever_offline"]
df["customer_value_total"]=df["customer_value_total_ever_offline"]+df["customer_value_total_ever_online"]



df.dtypes
df["order_channel"].head()
for col in df.columns:
    if "date" in col:
        df[col]=df[col].apply(pd.to_datetime)






df.groupby("order_channel").agg({"master_id":"nunique",
                                 "order_num_total":"sum",
                                 "customer_value_total":"sum"})


df.sort_values("customer_value_total",ascending=False).head(10)



df.sort_values("order_num_total",ascending=False).head(10)




def data(dataframe):
    dataframe.head(10)
    dataframe.columns
    dataframe.shape
    dataframe.describe().T
    dataframe.isnull().sum()
    dataframe.dtypes
    dataframe["order_num_total"] = dataframe["order_num_total_ever_online"] + dataframe["order_num_total_ever_offline"]
    dataframe["customer_value_total"] = dataframe["customer_value_total_ever_offline"] + dataframe["customer_value_total_ever_online"]
    dataframe.dtypes
    dataframe["order_channel"].head()
    for col in dataframe.columns:
        if "date" in col:
            dataframe[col] = dataframe[col].apply(pd.to_datetime)

    # [df[col]==df[col].apply(pd.to_datetime) for col in df.columns if "date" in col]
    dataframe.groupby("order_channel").agg({"master_id": "nunique",
                                     "order_num_total": "sum",
                                     "customer_value_total": "sum"})
    dataframe.sort_values("customer_value_total", ascending=False).head(10)
    dataframe.sort_values("order_num_total", ascending=False).head(10)
    return dataframe
x=data(df)
x.head()



df.head()
df["last_order_date"].max()
today_date=dt.datetime(2021,6,1)


rfm=df.groupby("master_id").agg({
    "last_order_date": lambda date:(today_date-date.max()).days,
    "order_num_total": lambda y:y.sum(),
    "customer_value_total": lambda x: x.sum()
})
rfm.head()
rfm.reset_index(inplace=True)
rfm.columns=["customer_id","recency","frequency","monetary"]





rfm["recency_score"]=pd.qcut(rfm["recency"],5,labels=[5,4,3,2,1])
rfm["frequency_score"]=pd.qcut(rfm["frequency"].rank(method="first"),5,labels=[1,2,3,4,5])
rfm["monetary_score"]=pd.qcut(rfm["monetary"],5,labels=[1,2,3,4,5])

rfm["RF_SCORE"]=rfm["recency_score"].astype(str)+rfm["frequency_score"].astype(str)

seg_map = {
    r'[1-2][1-2]': 'hibernating',
    r'[1-2][3-4]': 'at_Risk',
    r'[1-2]5': 'cant_loose',
    r'3[1-2]': 'about_to_sleep',
    r'33': 'need_attention',
    r'[3-4][4-5]': 'loyal_customers',
    r'41': 'promising',
    r'51': 'new_customers',
    r'[4-5][2-3]': 'potential_loyalists',
    r'5[4-5]': 'champions'

}

rfm["segment"]=rfm["RF_SCORE"].replace(seg_map,regex=True)



rfm.groupby("segment").agg({
    "recency": "mean",
    "frequency": "mean",
    "monetary": "mean"
})


df.head()
rfm.head()
df = df.rename(columns={"master_id": "customer_id"})

y=rfm.merge(df,on="customer_id",how="left")

k=y[(y["segment"]=="loyal_customers")&(y["interested_in_categories_12"].str.contains("KADIN",na=False))]
k.head()
f.head()

f=k[["customer_id"]]

f.to_csv("yeni_marka_hedef_müşteri_id.csv")


y.head()

b=y[(y["segment"].isin(["new_customers","cant_loose"]))&((y["interested_in_categories_12"].str.contains("ERKEK|COCUK",na=False)))]
b.head()

g=b[["customer_id"]]
g.head()
g.to_csv("indirim_hedef_müşteri_ids.csv")