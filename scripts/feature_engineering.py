import pandas as pd
import numpy as np
import os

# --- 1. CONFIGURAÇÃO DE CAMINHOS ---

pasta_atual = os.path.dirname(os.path.abspath(__file__))

caminho_leitura = os.path.join(pasta_atual, '..', 'data', 'CC GENERAL.csv')
caminho_salvar = os.path.join(pasta_atual, '..', 'data', 'CC_GENERAL_COM_TARGET.csv')

# --- 2. VERIFICAÇÃO E CARREGAMENTO ---
if not os.path.exists(caminho_leitura):
    print(f"\n❌ ERRO CRÍTICO: O arquivo não foi encontrado.")
    print(f"O Python procurou aqui: {caminho_leitura}")
    print("Dica: Verifique se o nome do arquivo na pasta 'data' é exatamente 'CC GENERAL.csv'")
else:
    df = pd.read_csv(caminho_leitura)
    print("\n✅ Sucesso! Dados carregados.")

    # --- 3. LÓGICA DE NEGÓCIO (TARGET ENGINEERING) ---
    def calcular_limite_ideal(row):
        limite_atual = row['CREDIT_LIMIT'] if row['CREDIT_LIMIT'] > 0 else 1
        uso_atual = row['BALANCE'] / limite_atual
        
        # Regra de Risco
        if (row['CASH_ADVANCE'] > 500) or (uso_atual >= 0.90):
            return row['BALANCE'] * 1.1 
        # Regra de Oportunidade
        elif (uso_atual < 0.50) and (row['ONEOFF_PURCHASES'] > 0):
            return row['CREDIT_LIMIT'] * 1.2
        # Manutenção
        else:
            return row['CREDIT_LIMIT']

    # Aplica a lógica
    df['Ideal_Credit_Limit'] = df.apply(calcular_limite_ideal, axis=1)

    # --- 4. SALVAMENTO ---
    print("\n--- Amostra do Novo Limite (Target) ---")
    print(df[['CUST_ID', 'CREDIT_LIMIT', 'BALANCE', 'Ideal_Credit_Limit']].head())
    
    # Salva o arquivo novo
    df.to_csv(caminho_salvar, index=False)
    print(f"\n💾 Arquivo salvo com sucesso em: {caminho_salvar}")