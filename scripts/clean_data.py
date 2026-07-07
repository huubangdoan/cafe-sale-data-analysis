import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
def convertToNumber(numCols):
    for i in numCols:
        df[i]=pd.to_numeric(df[i], errors="coerce")
def convertToCategory(str_cols):
    df[str_cols] = df[str_cols].astype('category')
def convertToDatetime(dateTime):
    df[dateTime] = pd.to_datetime(df[dateTime], errors="coerce")
def checkUnique(cols):
    for i in cols:
        print(f"the unique value in {i} is ")
        print(df[i].unique())
def removeNotRelated(cols):
    df[cols]=df[cols].replace(["UNKNOWN", "ERROR"], np.nan)
def firstLook(df):
    print(df.head())
    print(df.info())
def checkOutlier(cols):
    for i in cols:
        sns.boxplot(df[i])
        plt.title(f"the boxplot of {i}")
        plt.show()
def fillMissing(cols):
    for i in cols:
        if pd.api.types.is_float_dtype(df[i]):
            df[i]=df[i].fillna(df[i].median())
        if pd.api.types.is_categorical_dtype(df[i]):
            df[i]=df[i].fillna(df[i].mode()[0])
        if pd.api.types.is_datetime64_any_dtype(df[i]):
            df.dropna(subset=[i], inplace=True) 
def savefile(df):
    df.to_csv(f"data/processed/cleaned_cafe_sales.csv")
if __name__=="__main__":
    df=pd.read_csv(r"data\raw\dirty_cafe_sales.csv")
    cols=df.columns
    firstLook(df)
    checkUnique(cols)
    removeNotRelated(cols)
    checkUnique(cols)
    convertToNumber(cols[2:5])
    convertToDatetime(cols[-1])
    convertToCategory(cols[[0,1,5,6]])
    fillMissing(cols)
    checkOutlier(cols[2:5])
    savefile(df)


