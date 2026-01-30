import pandas as pd
import sqlite3

# 1. EXTRAÇÃO (Extract)
df = pd.read_csv('data/CC GENERAL.csv')

#2. TRANSFORMAÇÃO (Transform - Limpeza)

df = df.drop_duplicates()

df = df.dropna()

df.columns = [col.strip().lower() for col in df.columns]

# 3. CONEXÃO (Connection)
conn = sqlite3.connect('credit_data.db')

# 4. CARGA (Load)

df.to_sql('tb_clientes_credito', conn, if_exists='replace', index=False)

# 5. FECHAMENTO
conn.close()
