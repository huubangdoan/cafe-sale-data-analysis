import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
df=pd.read_csv(r"data\processed\cleaned_cafe_sales.csv")
load_dotenv() 
url = URL.create(
    drivername="mysql+pymysql",
    username=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    database=os.getenv("DB_NAME")
)
engine = create_engine(url)
df.to_sql("cafe_sales", con=engine, if_exists="replace", index=False)
print(df.head())
