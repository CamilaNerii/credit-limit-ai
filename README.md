# 💳 Credit Limit AI - Intelligent Limit Allocation

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Pandas](https://img.shields.io/badge/Data-Pandas-150458.svg)
![Machine Learning](https://img.shields.io/badge/ML-Random%20Forest-green.svg)
![Status](https://img.shields.io/badge/Status-Completed-success)

[🇺🇸 English](#english) | [🇧🇷 Português](#portugues)

---

<a name="english"></a>
## 🇺🇸 English

### 🎯 Project Overview
This project successfully built an end-to-end data pipeline and a **Regression Machine Learning Model** to predict the **"Ideal Credit Limit"** for 8,950 banking customers. Unlike traditional models that just classify risk (Classification), this solution calculates the exact credit amount that balances **Revenue Opportunity** with **Default Risk**.

### 🔍 Key Business Insights (SQL & ETL Phase)
Before modeling, an extensive Exploratory Data Analysis (EDA) using SQL and Python revealed crucial behavioral patterns stored across our **Staging Area (`credit_data.db`)**:

1.  **The "Cash Advance" Risk Factor:** Customers who frequently use their **credit card limit to withdraw cash** are **4x more likely** to default.
2.  **The Limit Paradox:** High-limit customers are proportionally safer.
    * *Low Limit (< $2.5k):* ~20% risk rate.
    * *High Limit (> $7k):* ~4% risk rate.

### 🧠 Target Engineering & Preprocessing
Instead of training the model to predict the *current* bank limit, we engineered a new target variable called `Ideal_Credit_Limit` based on financial risk rules. 
During **Phase 4 (Data Preparation)**, we removed the `CUST_ID` to avoid overfitting and handled **314 missing values** using **Median Imputation**, producing a clean dataset ready for Scikit-Learn.

### 📊 Model Performance & Final Results (Phase 5)
The model was trained using a **Random Forest Regressor** (80/20 train/test split) and achieved elite-level baseline metrics:

| Metric | Value | Business Impact |
| :--- | :--- | :--- |
| **Evaluated Credit Mean** | $3,979.26 | Baseline average of the portfolio. |
| **Mean Absolute Error (MAE)** | $296.56 | On average, predictions deviate by only $296. |
| **Relative Error Rate** | 7.45% | Extremely low error variance relative to the total limit. |
| **Overall Model Accuracy** | **92.55%** | **Highly reliable for production deployment.** |

---

<a name="portugues"></a>
## 🇧🇷 Português

### 🎯 Visão Geral do Projeto
Este projeto construiu com sucesso um pipeline de dados ponta a ponta e um **Modelo de Machine Learning (Regressão)** para prever o **"Limite de Crédito Ideal"** para 8.950 clientes bancários. Diferente de modelos que apenas classificam o risco, esta solução calcula o valor exato de limite que equilibra **Oportunidade de Receita** com **Mitigação de Inadimplência**.

### 🔍 Insights de Negócio (Fase SQL & ETL)
Antes da modelagem, uma Análise Exploratória de Dados (EDA) via SQL e Python revelou padrões comportamentais cruciais armazenados na nossa **Staging Area (`credit_data.db`)**:

1.  **O Fator de Risco do Saque (Cash Advance):** Clientes que utilizam o **limite do cartão de crédito para realizar saques em espécie** têm **4x mais chances** de inadimplência.
2.  **O Paradoxo do Limite:** Clientes com limites altos são proporcionalmente mais seguros.
    * *Limite Baixo (< $2.5k):* ~20% de taxa de risco.
    * *Limite Alto (> $7k):* ~4% de taxa de risco.

### 🧠 Target Engineering & Pré-processamento
Em vez de prever o limite atual do banco, criamos a variável `Ideal_Credit_Limit` baseada em regras de risco financeiro. 
Na **Fase 4 (Data Preparation)**, removemos a coluna `CUST_ID` (Noise Reduction) e tratamos **314 valores nulos** utilizando a estratégia de **Imputação pela Mediana**, gerando uma base consistente e livre de vieses.

### 📊 Performance do Modelo e Resultados Finais (Fase 5)
O modelo foi validado através do algoritmo **Random Forest Regressor** (divisão 80/20) e alcançou métricas de excelência:

| Métrica | Valor | Impacto de Negócio |
| :--- | :--- | :--- |
| **Limite Médio Avaliado** | $3,979.26 | Média histórica do portfólio de crédito. |
| **Erro Médio Absoluto (MAE)** | $296.56 | Em média, as previsões erram por apenas $296 dólares. |
| **Taxa de Erro Relativo** | 7.45% | Variância de erro extremamente baixa em relação ao limite total. |
| **Precisão Geral do Modelo** | **92.55%** | **Alta confiabilidade para tomada de decisão em produção.** |

---

### 🛠️ Tech Stack / Tecnologias
* **Core:** Python 🐍 (Pandas, Numpy).
* **Data Prep & ML:** Scikit-Learn (`SimpleImputer`, `RandomForestRegressor`).
* **Database & Analytics:** SQL (SQLite) para armazenamento e persistência da base limpa.

### 🚀 Roadmap Concluído
* ✅ **Fase 1:** Ingestão de Dados e Carga SQL (`credit_data.db`).
* ✅ **Fase 2:** Análise Exploratória SQL (Identificação de fatores de risco).
* ✅ **Fase 3:** Target Engineering (Criação das regras de limite ideal).
* ✅ **Fase 4:** Data Preprocessing (Tratamento de 314 nulos via Mediana e eliminação de ruídos).
* ✅ **Fase 5:** Treinamento e Validação do Modelo de Machine Learning (**92.55% de Precisão**).

---

### ⚙️ How to Run / Como Executar

```bash
# 1. Execute the ETL and Database Load
python scripts/01_etl_carga.py

# 2. Run Target Engineering (Risk & Opportunity rules)
python scripts/02_target_engineering.py

# 3. Data Preparation (Median Imputation & Cleaning)
python scripts/03_data_preparation.py

# 4. Train and Validate the Machine Learning Model (Phase 05)
python scripts/analise_principal.py
```

### 👩‍💻 Autora
Camila Neri
Data Analyst | Python & SQL Enthusiast

LinkedIn | GitHub
