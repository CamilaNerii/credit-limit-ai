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



# --- BLOCO DE RELATÓRIO FINAL ---
media_gastos = df['purchases'].mean()
total_vips = len(df)

print("\n") # Pula linha
print("=" * 45)
print("📊 RESULTADO DA ANÁLISE DE CRÉDITO (VIPs)")
print("=" * 45)
print(f"🎯 Critério Utilizado: Limite >= $10.000")
print(f"👥 Quantidade de Clientes: {total_vips}")
print("-" * 45)
print(f"💰 MÉDIA DE GASTOS REAIS: ${media_gastos:,.2f}")
print("=" * 45)
print("\n")