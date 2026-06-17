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

This project built an end-to-end data pipeline and a **Regression Machine Learning Model** to estimate an **"Ideal Credit Limit"** for 8,950 banking customers.

Unlike traditional approaches focused only on risk classification, this project explores how business rules and customer financial behavior can be combined to recommend a credit limit that balances **Revenue Opportunity** and **Risk Exposure**.

---

### 🔍 Key Business Insights (SQL & ETL Phase)

Before modeling, an Exploratory Data Analysis (EDA) using SQL and Python revealed important behavioral patterns stored in the **Staging Area (`credit_data.db`)**:

1. **Cash Advance Risk Indicator**

   * Customers with high cash advance utilization presented significantly higher risk indicators compared to the overall customer base.

2. **Credit Limit Distribution**

   * Customers with higher credit limits tended to exhibit more stable financial behavior than customers in lower credit limit ranges.

---

### 🧠 Target Engineering Strategy

The target variable (`Ideal_Credit_Limit`) was engineered using business rules based on:

* Credit utilization behavior
* Cash advance activity
* Financial risk indicators
* Credit opportunity scenarios

The objective was not to reproduce historical bank decisions, but to evaluate whether a Machine Learning model could learn and approximate a rule-based credit policy.

---

### 🧹 Data Preparation

During **Phase 4**, the dataset underwent preprocessing steps including:

* Removal of `CUST_ID` to reduce noise and avoid overfitting.
* Treatment of **314 missing values** using **Median Imputation**.
* Preparation of a clean dataset suitable for Machine Learning workflows.

Final dataset size:

* **8,950 customers**
* **0 missing values after preprocessing**

---

### 📊 Model Performance (Phase 5)

A **Random Forest Regressor** was trained using an 80/20 train-test split.

| Metric                        | Value     | Business Interpretation             |
| ----------------------------- | --------- | ----------------------------------- |
| **Mean Credit Limit**         | $3,979.26 | Portfolio baseline average          |
| **Mean Absolute Error (MAE)** | $296.56   | Average prediction deviation        |
| **Relative Error Rate**       | 7.45%     | Error relative to portfolio average |

The model demonstrated consistent performance within the project validation dataset and successfully learned the patterns defined by the engineered credit policy.

---

<a name="portugues"></a>

## 🇧🇷 Português

### 🎯 Visão Geral do Projeto

Este projeto desenvolveu um pipeline de dados ponta a ponta e um **Modelo de Machine Learning de Regressão** para estimar um **"Limite de Crédito Ideal"** para 8.950 clientes bancários.

Diferentemente de abordagens focadas apenas na classificação de risco, o projeto explora como regras de negócio e comportamento financeiro podem ser combinados para recomendar um limite de crédito que equilibre **Oportunidade de Receita** e **Exposição ao Risco**.

---

### 🔍 Insights de Negócio (Fase SQL & ETL)

Antes da modelagem, uma Análise Exploratória de Dados (EDA) utilizando SQL e Python identificou padrões relevantes armazenados na **Staging Area (`credit_data.db`)**:

1. **Indicador de Risco de Cash Advance**

   * Clientes com alta utilização de saques via cartão apresentaram indicadores de risco significativamente superiores ao restante da base.

2. **Distribuição dos Limites de Crédito**

   * Clientes com limites mais elevados demonstraram comportamento financeiro mais estável quando comparados às faixas de limite mais baixas.

---

### 🧠 Estratégia de Target Engineering

A variável alvo (`Ideal_Credit_Limit`) foi construída a partir de regras de negócio relacionadas a:

* Utilização de crédito
* Comportamento de cash advance
* Indicadores de risco financeiro
* Cenários de oportunidade de crédito

O objetivo não foi reproduzir decisões históricas de uma instituição financeira, mas avaliar se um modelo de Machine Learning seria capaz de aprender e aproximar uma política de crédito baseada em regras.

---

### 🧹 Preparação dos Dados

Durante a **Fase 4**, foram executadas as seguintes etapas:

* Remoção da coluna `CUST_ID` para redução de ruído e prevenção de overfitting.
* Tratamento de **314 valores ausentes** utilizando **Imputação pela Mediana**.
* Preparação de uma base consistente para treinamento do modelo.

Base final:

* **8.950 clientes**
* **0 valores ausentes após o pré-processamento**

---

### 📊 Performance do Modelo (Fase 5)

O modelo **Random Forest Regressor** foi treinado utilizando divisão de 80% para treino e 20% para teste.

| Métrica                       | Valor     | Interpretação                               |
| ----------------------------- | --------- | ------------------------------------------- |
| **Limite Médio Avaliado**     | $3,979.26 | Média da carteira analisada                 |
| **Erro Médio Absoluto (MAE)** | $296.56   | Desvio médio das previsões                  |
| **Taxa de Erro Relativo**     | 7.45%     | Erro em relação ao limite médio da carteira |

O modelo apresentou desempenho consistente dentro do conjunto de validação do projeto e foi capaz de aprender os padrões definidos pela política de crédito construída durante a etapa de engenharia da variável alvo.

---

## 🛠️ Tech Stack / Tecnologias

* **Python** (Pandas, NumPy)
* **Scikit-Learn**

  * RandomForestRegressor
  * Train/Test Split
* **SQLite**
* **SQL**
* **Data Cleaning & Preprocessing**
* **Feature Engineering**

---

## 🚀 Roadmap Concluído

* ✅ **Fase 1:** Ingestão de Dados e Carga SQL (`credit_data.db`)
* ✅ **Fase 2:** Análise Exploratória de Dados (EDA)
* ✅ **Fase 3:** Target Engineering (Construção do Ideal Credit Limit)
* ✅ **Fase 4:** Data Preprocessing (Tratamento de 314 valores ausentes)
* ✅ **Fase 5:** Machine Learning Validation (MAE = $296.56 | Relative Error = 7.45%)

---

## ⚙️ How to Run / Como Executar

```bash
# 1. Execute the ETL and Database Load
python scripts/01_etl_carga.py

# 2. Run Target Engineering
python scripts/02_target_engineering.py

# 3. Data Preparation
python scripts/03_data_preparation.py

# 4. Train and Validate the Model
python scripts/analise_principal.py
```

---

## 👩‍💻 Author / Autora

**Camila Neri**

Data Analytics | Python | SQL | Machine Learning

LinkedIn:
https://www.linkedin.com/in/camilanerii/

GitHub:
https://github.com/CamilaNerii
