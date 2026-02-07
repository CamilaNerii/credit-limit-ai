# 💳 Credit Limit AI - Intelligent Limit Allocation

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![SQL](https://img.shields.io/badge/Database-SQLite-blue)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)

[🇺🇸 English](#english) | [🇧🇷 Português](#portugues)

---

<a name="english"></a>
## 🇺🇸 English

### 🎯 Project Overview
This project aims to build a **Regression Machine Learning Model** to predict the **"Ideal Credit Limit"** for banking customers. Unlike traditional models that just classify "Good vs. Bad" payers, this solution calculates the exact credit amount that balances **Revenue Opportunity** with **Default Risk**.

### 🔍 Key Business Insights (SQL Phase)
Before modeling, an extensive Exploratory Data Analysis (EDA) using SQL revealed crucial behavioral patterns:
1.  **The "Cash Advance" Trap:** Customers who frequently use "Cash Advance" are **4x more likely** to exceed their credit limit. This is a strong predictor of financial distress.
2.  **The Limit Paradox:** High-limit customers are proportionally safer.
    * *Low Limit (< $2.5k):* ~20% risk rate.
    * *High Limit (> $7k):* ~4% risk rate.
3.  **The "Ideal Limit" Logic:** The model will not simply predict the *current* bank limit (which may be inefficient). Instead, we are engineering a new target variable based on usage:
    * **Healthy Users:** Limit should be increased (Incentivize spending).
    * **Risky Users:** Limit should be capped or reduced (Mitigate loss).

### 🛠️ Tech Stack
* **Core:** Python 🐍 (Pandas, Numpy)
* **Database & Analytics:** SQL (SQLite) for Data Warehousing and KPI extraction.
* **Machine Learning:** Scikit-Learn (Random Forest / XGBoost - *Upcoming*).
* **Visualization:** Matplotlib/Seaborn & Power BI (*Upcoming*).

### 🚀 Current Status & Roadmap
* ✅ **Phase 1: ETL & Database Setup** (Raw CSV $\to$ SQLite).
* ✅ **Phase 2: SQL Exploratory Analysis** (Risk factors identified: Cash Advance & Low Limits).
* ✅ **Phase 3: Business Logic Definition** (Rules for the "Ideal Limit" target created).
* 🔄 **Phase 4 (Current):** Feature Engineering in Python & Machine Learning Modeling.

---

<a name="portugues"></a>
## 🇧🇷 Português

### 🎯 Visão Geral do Projeto
Este projeto tem como objetivo construir um **Modelo de Machine Learning (Regressão)** para prever o **"Limite de Crédito Ideal"** para clientes bancários. Diferente de modelos tradicionais que apenas classificam "Bom vs. Mau" pagador, esta solução calcula o valor exato de limite que equilibra **Oportunidade de Receita** com **Risco de Inadimplência**.

### 🔍 Insights de Negócio (Fase SQL)
Antes da modelagem, uma Análise Exploratória de Dados (EDA) via SQL revelou padrões comportamentais cruciais:
1.  **A Armadilha do Saque (Cash Advance):** Clientes que utilizam frequentemente o saque em dinheiro têm **4x mais chances** de estourar o limite. Este é um forte preditor de dificuldade financeira.
2.  **O Paradoxo do Limite:** Clientes com limites altos são proporcionalmente mais seguros.
    * *Limite Baixo (< $2.5k):* ~20% de taxa de risco.
    * *Limite Alto (> $7k):* ~4% de taxa de risco.
3.  **Lógica do "Limite Ideal":** O modelo não irá apenas prever o limite *atual* do banco (que pode estar errado). Estamos criando uma nova variável alvo (Target Engineering):
    * **Usuários Saudáveis:** O limite deve ser aumentado (Incentivar uso).
    * **Usuários de Risco:** O limite deve ser travado ou reduzido (Mitigar perdas).

### 🛠️ Tecnologias Utilizadas
* **Core:** Python 🐍 (Pandas, Numpy)
* **Banco de Dados & Analytics:** SQL (SQLite) para Data Warehousing e extração de KPIs.
* **Machine Learning:** Scikit-Learn (Random Forest / XGBoost - *Em breve*).
* **Visualização:** Matplotlib/Seaborn & Power BI (*Em breve*).

### 🚀 Status Atual & Roadmap
* ✅ **Fase 1: ETL & Configuração do Banco** (CSV Bruto $\to$ SQLite).
* ✅ **Fase 2: Análise Exploratória SQL** (Fatores de risco identificados: Saque/Cash Advance & Limites Baixos).
* ✅ **Fase 3: Definição de Lógica de Negócio** (Regras para a variável "Limite Ideal" criadas).
* 🔄 **Fase 4 (Atual):** Engenharia de Atributos (Feature Engineering) em Python & Modelagem de Machine Learning.