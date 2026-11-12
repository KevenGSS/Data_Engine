# 📊 Observatório Multissetorial — Alto Jequitinhonha

Pipeline completo de Engenharia de Dados (Arquitetura Medallion) consolidando indicadores socioeconômicos e educacionais (IBGE e INEP) de 6 municípios do Alto Jequitinhonha, processado em **DuckDB SQL** e publicado em **Streamlit**.

## 🖥️ Preview do Dashboard

![Visão Geral do Dashboard](dashboard_geral.png)

## 🛠️ Stack & Arquitetura
* **Ingestão & Camadas:** Python (Pandas) — Bronze / Silver / Gold
* **Processamento Analítico:** DuckDB SQL (Cálculo de Gaps e Índice de Vulnerabilidade Multissetorial - IVM)
* **Visualização & Web App:** Plotly & Streamlit
