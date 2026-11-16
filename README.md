# 📊 Observatório Multissetorial — Alto Jequitinhonha

Pipeline de Engenharia e Análise de Dados estruturado na **Arquitetura Medallion (Bronze / Silver / Gold)** para consolidação de indicadores socioeconômicos, educacionais e de infraestrutura de 6 municípios do Alto Jequitinhonha (Minas Novas, Capelinha, Turmalina, Angelândia, Água Boa e Chapada do Norte).

## 🎯 Objetivo Técnico
Transformar bases públicas dispersas (**IBGE e INEP**) em diagnósticos executivos acionáveis, aplicando regras de negócio em **SQL (DuckDB)** para calcular *gaps* em relação a metas de referência e gerar o **Índice de Vulnerabilidade Multissetorial (IVM)**.

## 🛠️ Arquitetura & Stack
* **Camadas Bronze & Silver:** Padronização e tratamento de dados tabulares com **Python (Pandas)**.
* **Camada Gold & Motor Analítico:** Consultas relacionais, cálculo de *gaps* e classificação prescritiva via **DuckDB SQL**.
* **Visualização & Deploy:** Dashboard interativo desenvolvido com **Streamlit** e **Plotly**, hospedado no Streamlit Community Cloud.

## 🖥️ Preview do Dashboard

### Diagnóstico & Soluções (IVM)
![Diagnóstico & Soluções](Diagnóstico%20&%20Soluções.png)

### Educação Completa (INEP)
![Educação Completa](Educação%20Completa%20(INEP).png)

### Setores Econômicos (VAB & Agro)
![Setores Econômicos](Setores%20Econômicos.png)

### Infraestrutura & Fibra
![Infraestrutura & Fibra](Infraestrutura%20&%20Fibra.png)

### Tabela Master Completa
![Tabela Master](Tabela%20Master%20Completa.png)

---
> *Nota Metodológica: Projeto desenvolvido para fins de portfólio técnico e demonstração arquitetural, combinando indicadores públicos oficiais (IBGE/INEP) e parâmetros de benchmark para modelagem analítica.*
