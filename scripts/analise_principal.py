import pandas as pd
import sqlite3


caminho_banco = r'C:\Users\camil\Desktop\credit-limit-ai-2\data\credit_data.db'
caminho_sql = r'C:\Users\camil\Desktop\credit-limit-ai-2\sql\filtro_credito.sql'


with open(caminho_sql, 'r') as arquivo:
    minha_query = arquivo.read()


conn = sqlite3.connect(caminho_banco)
df = pd.read_sql(minha_query, conn)
conn.close()


df['credit_limit'] = pd.to_numeric(df['credit_limit'])
df['minimum_payments'] = pd.to_numeric(df['minimum_payments'])


print(f"Linhas carregadas: {df.shape[0]}")
print(df.head())