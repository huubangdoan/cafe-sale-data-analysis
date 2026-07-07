import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv(r"data\raw\dirty_cafe_sales.csv")
print(df.shape)
print(df.dtypes)
print(df.head())
print(df.info())
totalRow=10000
def convertToNumeric(col):
    df[col]=pd.to_numeric(df[col], errors="coerce")
convertToNumeric("Quantity")
convertToNumeric("Price Per Unit")
convertToNumeric("Total Spent")
df["Transaction Date"]=pd.to_datetime(df["Transaction Date"], errors="coerce")
cols=df.columns.to_list()
def missingPercent(col):
    for i in col:
        print(f"the missing percent in column {i} is {round(100-(df[i].count()*100/totalRow),2)}")
missingPercent(cols)
df_copy=pd.DataFrame(df)
print(len(df_copy.dropna()))
numeric_cols=df_copy.select_dtypes(include="number").columns.to_list()
def drawBoxplot(numCols):
    for i in numCols:
        data=df[i]
        plt.boxplot(data)
        plt.title(f"the boxplot of {i}")
        plt.show()
drawBoxplot(numeric_cols)
