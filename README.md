# 📊 Observatório Multissetorial — Alto Jequitinhonha

Pipeline completo de Engenharia de Dados (Arquitetura Medallion) consolidando indicadores socioeconômicos e educacionais (IBGE e INEP) de 6 municípios do Alto Jequitinhonha, processado em **DuckDB SQL** e publicado em **Streamlit**.

## 🖥️ Preview do Dashboard

### 🎯 Diagnóstico & Soluções (IVM)
![Diagnóstico & Soluções](Diagnóstico%20&%20Soluções.png)

### 🏫 Educação Completa (INEP)
![Educação Completa](Educação%20Completa%20(INEP).png)

### 🏭 Setores Econômicos
![Setores Econômicos](Setores%20Econômicos.png)

### 🌐 Infraestrutura & Fibra
![Infraestrutura & Fibra](Infraestrutura%20&%20Fibra.png)

### 📋 Tabela Master Completa
![Tabela Master](Tabela%20Master%20Completa.png)

## 🛠️ Stack & Arquitetura
* **Ingestão & Camadas:** Python (Pandas) — Bronze / Silver / Gold
* **Processamento Analítico:** DuckDB SQL (Cálculo de Gaps e Índice de Vulnerabilidade Multissetorial - IVM)
* **Visualização & Web App:** Plotly & Streamlit
