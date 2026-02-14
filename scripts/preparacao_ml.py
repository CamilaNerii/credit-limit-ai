import pandas as pd
import numpy as np
import os
from sklearn.impute import SimpleImputer

# --- 1. CONFIGURAÇÃO DE CAMINHOS ---
pasta_atual = os.path.dirname(os.path.abspath(__file__))

caminho_leitura = os.path.join(pasta_atual, '..', 'data', 'CC_GENERAL_COM_TARGET.csv')

caminho_salvar = os.path.join(pasta_atual, '..', 'data', 'CC_GENERAL_PRONTO_PARA_ML.csv')

# --- 2. CARREGAMENTO ---
if not os.path.exists(caminho_leitura):
    print("❌ Erro: Arquivo com Target não encontrado. Rode o script anterior primeiro!")
else:
    df = pd.read_csv(caminho_leitura)
    print(f"✅ Dados carregados! Total de clientes: {df.shape[0]}")

    # --- 3. LIMPEZA DOS DADOS (DATA CLEANING) ---
    print("\n🚿 Iniciando a limpeza...")

    # A. Remover colunas que não são números (ID do cliente)
    
    df_clean = df.drop(columns=['CUST_ID'])
    print("   -> Coluna 'CUST_ID' removida.")

    # B. Verificar Valores Vazios (NaN)
    nulos_antes = df_clean.isnull().sum().sum()
    print(f"   -> Encontrados {nulos_antes} valores vazios na tabela.")

    # C. Preencher valores vazios com a MÉDIA (Imputação)

    imputer = SimpleImputer(strategy='median')
    
    
    colunas = df_clean.columns
    df_array = imputer.fit_transform(df_clean)
    df_final = pd.DataFrame(df_array, columns=colunas)

    nulos_depois = df_final.isnull().sum().sum()
    print(f"   -> Valores vazios após tratamento: {nulos_depois} (Sucesso!)")

    # --- 4. CHECAGEM FINAL ---
    print("\n📊 Amostra dos dados prontos para a IA:")
    
    pd.set_option('display.float_format', '{:.2f}'.format)
    print(df_final.head())

    # --- 5. SALVAMENTO ---
    df_final.to_csv(caminho_salvar, index=False)
    print("\n" + "="*50)
    print(f"💾 ARQUIVO PRONTO SALVO EM:\n{caminho_salvar}")
    print("="*50)
    print("🚀 Próximo passo: Treinar o modelo (Machine Learning)!")