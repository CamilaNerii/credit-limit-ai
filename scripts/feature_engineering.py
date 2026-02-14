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



# --- COLE ISSO NO FINAL DO SEU ARQUIVO (SUBSTITUINDO O PRINT ANTERIOR) ---

# 1. Pegamos os dados reais dos nossos "personagens" da história
cliente_risco = df[df['CUST_ID'] == 'C10002'].iloc[0]
cliente_top = df[df['CUST_ID'] == 'C10003'].iloc[0]

# 2. Desenhamos o Relatório Visual (O estilo do seu post viral)
print("\n")
print("="*60)
print(" 🛠  RESULTADO: TARGET ENGINEERING (CORREÇÃO DE LIMITES)")
print("="*60)

print(f" 🔴 CASO 1: RISCO DETECTADO (Uso de Saque/Alavancagem)")
print(f"    🆔 Cliente:       {cliente_risco['CUST_ID']}")
print(f"    💳 Limite Banco:  ${cliente_risco['CREDIT_LIMIT']:,.2f}")
print(f"    💸 Dívida Real:   ${cliente_risco['BALANCE']:,.2f}")
print(f"    🔒 NOVO TARGET:   ${cliente_risco['Ideal_Credit_Limit']:,.2f} (Redução de Segurança)")

print("-" * 60)

print(f" 🟢 CASO 2: OPORTUNIDADE (Bom Pagador + Baixo Uso)")
print(f"    🆔 Cliente:       {cliente_top['CUST_ID']}")
print(f"    💳 Limite Banco:  ${cliente_top['CREDIT_LIMIT']:,.2f}")
print(f"    💸 Dívida Real:   ${cliente_top['BALANCE']:,.2f}")
print(f"    🚀 NOVO TARGET:   ${cliente_top['Ideal_Credit_Limit']:,.2f} (Aumento de 20%)")

print("="*60)
print(f" 💾 Arquivo 'Target' gerado com sucesso para {len(df)} clientes.")
print("="*60 + "\n")