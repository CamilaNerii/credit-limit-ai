import pandas as pd
import sqlite3

# 1. EXTRAÇÃO (Extract)
df = pd.read_csv('data/CC GENERAL.csv')

# 2. CONEXÃO (Connection)
conn = sqlite3.connect('credit_data.db')

# 3. CARGA (Load)

df.to_sql('tb_clientes_credito', conn, if_exists='replace', index=False)

# 4. FECHAMENTO
conn.close()
