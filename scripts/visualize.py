import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
df=pd.read_csv(r"data\processed\cleaned_cafe_sales.csv")
def drawBar(data, col1, col2):
    plt.figure(figsize=(12,6))
    sns.barplot(data, x=col1, y=col2, palette="husl", hue=col1)
    plt.title(f"The comparision between {col1} and {col2}")
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.show()
def drawHistogram(data, col):
    plt.figure(figsize=(12,6))
    sns.histplot(data, x=col, bins=10)
    plt.title(f"the distribution of {col}")
    plt.xlabel(col)
    plt.ylabel("quantity")
    plt.show()
def drawCount(data, col, quantity="Quantity"):
    plt.figure(figsize=(12,6))
    data=data.groupby(col)[quantity].sum().reset_index()
    sns.barplot(data, x=col, y=quantity, hue=col, palette="husl")
    plt.title(f"the frequency of {col}")
    plt.xlabel(col)
    plt.ylabel(quantity)
    plt.show()
def drawLine(data, item_name, time, item_col="Item", quantity="Quantity", freq="M"):
    data = data.copy()
    data[time] = pd.to_datetime(data[time])
    filtered = data[data[item_col] == item_name].copy()
    filtered["Period"] = filtered[time].dt.to_period(freq).astype(str)
    grouped = filtered.groupby("Period")[quantity].sum().reset_index()
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=grouped, x="Period", y=quantity, marker='o', color='steelblue')
    
    plt.title(f"the trend {quantity} of {item_name} according to time")
    plt.xlabel("time")
    plt.ylabel(quantity)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

if __name__=="__main__":
    drawBar(df, "Item", "Total Spent")
    drawHistogram(df, "Total Spent")
    drawCount(df, "Item")
    drawLine(df, "Salad", "Transaction Date")
    drawLine(df, "Juice", "Transaction Date")





    

    