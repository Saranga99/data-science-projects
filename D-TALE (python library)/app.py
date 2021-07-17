import pandas as pd
import dtale 
import dtale.app as dtale_app
df=pd.read_csv('train.csv')
dtale_app.USE_NGROK=True
dtale.show(df)
