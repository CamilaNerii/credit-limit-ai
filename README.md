# 💳 Credit Limit AI - Intelligent Limit Allocation

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Pandas](https://img.shields.io/badge/Data-Pandas-150458.svg)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

[🇺🇸 English](#english) | [🇧🇷 Português](#portugues)

---

<a name="english"></a>
## 🇺🇸 English

### 🎯 Project Overview
This project aims to build a **Regression Machine Learning Model** to predict the **"Ideal Credit Limit"** for banking customers. Unlike traditional models that just classify "Creditworthy vs. Non-creditworthy" (Classification), this solution calculates the exact credit amount that balances **Revenue Opportunity** with **Default Risk**.

### 🔍 Key Business Insights (SQL Phase)
Before modeling, an extensive Exploratory Data Analysis (EDA) using SQL revealed crucial behavioral patterns:

1.  **The "Cash Advance" Risk Factor:** Customers who frequently use their **credit card limit to withdraw cash** are **4x more likely** to default. This behavior signals financial distress distinct from regular purchasing.
2.  **The Limit Paradox:** High-limit customers are proportionally safer.
    * *Low Limit (< $2.5k):* ~20% risk rate.
    * *High Limit (> $7k):* ~4% risk rate.

### 🧠 Modeling Strategy: The "Ideal Limit" (Target Engineering)
Instead of training the model to predict the *current* bank limit (which may contain historical biases), we engineered a new target variable called `Ideal_Credit_Limit` using Python. The goal is to correct inefficiencies:

| Customer Profile | Observed Behavior | Model Action (Logic) |
| :--- | :--- | :--- |
| **🟢 Healthy** | On-time payments + Low limit utilization. | **Increase Limit:** Incentivize spending & loyalty. |
| **🔴 High Risk** | High Cash Advance usage + High debt. | **Decrease Limit:** Mitigate default risk. |
| **🟡 Alert** | Recurring usage above 80%. | **Hold/Cap Limit:** Prevent over-indebtedness. |

*Outcome:* The AI learns to suggest the limit a customer *should have*, rather than just copying what they *currently have*.

### 🛠️ Tech Stack
* **Core:** Python 🐍 (Pandas, Numpy).
* **Data Prep:** Scikit-Learn (Imputation & Scaling).
* **Database & Analytics:** SQL (SQLite) for Data Warehousing.
* **Machine Learning:** Random Forest Regressor (*Upcoming*).

### 🚀 Current Status & Roadmap
* ✅ **Phase 1: ETL & Database Setup** (Raw CSV $\to$ SQLite).
* ✅ **Phase 2: SQL Exploratory Analysis** (Risk factors identified).
* ✅ **Phase 3: Feature Engineering** (Created `Ideal_Credit_Limit` target variable based on Risk Rules).
* ✅ **Phase 4: Data Preprocessing** (Cleaning, removing IDs, handling NaN values).
* 🔄 **Phase 5 (Next):** Machine Learning Model Training.

---

<a name="portugues"></a>
## 🇧🇷 Português

### 🎯 Visão Geral do Projeto
Este projeto tem como objetivo construir um **Modelo de Machine Learning (Regressão)** para prever o **"Limite de Crédito Ideal"** para clientes bancários. Diferente de modelos tradicionais que apenas classificam entre "Adimplente vs. Inadimplente", esta solução calcula o valor exato de limite que equilibra **Oportunidade de Receita** com **Risco de Inadimplência**.

### 🔍 Insights de Negócio (Fase SQL)
Antes da modelagem, uma Análise Exploratória de Dados (EDA) via SQL revelou padrões comportamentais cruciais:

1.  **O Fator de Risco do Saque (Cash Advance):** Clientes que utilizam o **limite do cartão de crédito para realizar saques em espécie** têm **4x mais chances** de inadimplência. Isso indica alta dependência de crédito rotativo.
2.  **O Paradoxo do Limite:** Clientes com limites altos são proporcionalmente mais seguros.
    * *Limite Baixo (< $2.5k):* ~20% de taxa de risco.
    * *Limite Alto (> $7k):* ~4% de taxa de risco.

### 🧠 Estratégia de Modelagem: O "Limite Ideal" (Target Engineering)
Em vez de treinar o modelo para prever o limite *atual* do banco (que pode conter erros históricos), criamos uma nova variável alvo chamada `Ideal_Credit_Limit` usando Python. O objetivo é corrigir distorções:

| Perfil do Cliente | Comportamento Observado | Ação do Modelo (Lógica) |
| :--- | :--- | :--- |
| **🟢 Saudável** | Pagamento em dia + Baixo uso do limite. | **Aumentar Limite:** Incentivar gastos e fidelidade. |
| **🔴 Alto Risco** | Uso de Saque (Cash Advance) + Dívida alta. | **Reduzir Limite:** Mitigar risco de inadimplência (Default). |
| **🟡 Alerta** | Uso acima de 80% recorrente. | **Manter/Travar:** Evitar superendividamento. |

*Resultado:* A IA aprende a sugerir o limite que o cliente *deveria ter*, e não necessariamente o que ele *tem*.

### 🛠️ Tecnologias Utilizadas
* **Core:** Python 🐍 (Pandas, Numpy).
* **Data Prep:** Scikit-Learn (Imputation & Scaling).
* **Banco de Dados & Analytics:** SQL (SQLite) para Data Warehousing.
* **Machine Learning:** Random Forest Regressor (*Em breve*).

### 🚀 Status Atual & Roadmap
* ✅ **Fase 1: ETL & Configuração do Banco** (CSV Bruto $\to$ SQLite).
* ✅ **Fase 2: Análise Exploratória SQL** (Fatores de risco identificados).
* ✅ **Fase 3: Feature Engineering** (Criação da variável Target `Ideal_Credit_Limit` baseada em regras de risco).
* ✅ **Fase 4: Pré-processamento de Dados** (Limpeza, remoção de IDs e tratamento de valores nulos).
* 🔄 **Fase 5 (Próxima):** Treinamento do Modelo de Machine Learning.

---

### ⚙️ How to Run (Como Executar)
To reproduce the dataset processing:

```bash
# 1. Generate Target Variable (Ideal Limit)
python scripts/feature_engineering.py

# 2. Clean Data for ML (Remove Nulls & IDs)
python scripts/2_preparacao_ml.py