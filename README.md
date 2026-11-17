# 📊 Observatório Multissetorial — Alto Jequitinhonha (`v1.1`)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://observatorio-alto-jequitinhonha.streamlit.app)

Pipeline de Engenharia e Análise de Dados estruturado na **Arquitetura Medallion (Bronze / Silver / Gold)** para consolidação de indicadores socioeconômicos, educacionais e de infraestrutura de 6 municípios do Alto Jequitinhonha (**Minas Novas, Capelinha, Turmalina, Angelândia, Água Boa e Chapada do Norte**).

🔗 **Acesse o Painel Interativo ao Vivo:** [observatorio-alto-jequitinhonha.streamlit.app](https://observatorio-alto-jequitinhonha.streamlit.app)

---

## 🎯 Objetivo Técnico
Transformar bases públicas dispersas (**IBGE e INEP**) em diagnósticos executivos acionáveis, aplicando regras de negócio em **SQL (DuckDB)** para calcular *gaps* em relação a benchmarks nacionais e gerar o **Índice de Vulnerabilidade Multissetorial (IVM)**.

## 🛠️ Arquitetura & Stack
* **Camadas Bronze & Silver:** Padronização e tratamento de dados tabulares com **Python (Pandas)**.
* **Camada Gold & Motor Analítico:** Consultas relacionais, cálculo de *gaps* e classificação prescritiva via **DuckDB SQL**.
* **Visualização & Deploy:** Dashboard interativo desenvolvido com **Streamlit** e **Plotly**, hospedado no Streamlit Community Cloud.

---

## 📐 Metodologia do IVM: Origem das Metas e Critérios de Ponderação
O **Índice de Vulnerabilidade Multissetorial (IVM)** mede a distância ponderada (*gap*) de cada município em relação a parâmetros de políticas públicas nacionais e equilíbrio fiscal:

| Dimensão | Meta / Limite | Peso | Origem & Justificativa Técnica |
| :--- | :---: | :---: | :--- |
| **Dependência da Adm. Pública (VAB)** | `≤ 30,0%` do VAB | **35%** (`0,35`) | Benchmark regional de diversificação econômica (polo de referência: Turmalina/Capelinha). Maior peso por determinar a capacidade própria de investimento e arrecadação do município. |
| **Infraestrutura Digital Escolar** | `≥ 60,0%` das escolas | **25%** (`0,25`) | Parâmetro da Estratégia Nacional de Escolas Conectadas / PNE (Meta 7). Impacta diretamente a inclusão digital e o desempenho nas avaliações do SAEB. |
| **Cobertura de Esgotamento Sanitário** | `≥ 80,0%` dos domicílios | **25%** (`0,25`) | Referência intermediária alinhada ao Novo Marco Legal do Saneamento (Lei 14.026/2020, que estabelece 90% até 2033). Indicador crítico de saúde pública preventiva. |
| **Docentes com Licenciatura (Médio)** | `≥ 85,0%` licenciados | **15%** (`0,15`) | Alinhado à Meta 15 do Plano Nacional de Educação (PNE / INEP AFD) para adequação da formação docente à disciplina lecionada. |

---

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

## 📋 Histórico de Versões
* **`v1.1`:** Adição da matriz de transparência metodológica do IVM (origem das metas e critérios de ponderação) na interface do dashboard e na documentação, além da especificação do recorte temporal das bases.
* **`v1.0`:** Implementação inicial do pipeline Medallion, motor analítico em DuckDB SQL e dashboard interativo em Streamlit/Plotly.

---

> *Nota Metodológica: Projeto de portfólio em Engenharia e Análise de Dados. Consolidado a partir de séries históricas públicas de referência (IBGE — Censo 2022 / Contas Regionais e INEP — Censo Escolar 2023) e parâmetros calibrados para validação da arquitetura Medallion, modelagem SQL (DuckDB) e cálculo do IVM.*
