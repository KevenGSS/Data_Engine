import streamlit as st
import pandas as pd
import duckdb
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(page_title="Observatório Alto Jequitinhonha", page_icon="📊", layout="wide")

st.title("📊 Observatório Multissetorial Completo — Alto Jequitinhonha")
st.markdown("**Arquitetura:** Medallion (Bronze / Silver / Gold) | **SQL Engine:** DuckDB | **Dados:** IBGE & INEP")
st.divider()

# 1. CAMADA GOLD COMPLETA
dados_gold_completos = [
    {
        'codigo_ibge': 3112300, 'municipio': 'Capelinha', 'populacao': 39626,
        'pib_per_capita': 28415.50, 'rendimento_medio_sm': 2.1,
        'vab_agropecuaria_pct': 22.5, 'vab_industria_pct': 18.3,
        'vab_servicos_pct': 41.2, 'vab_administracao_publica_pct': 18.0,
        'fpm_dependencia_pct': 42.1,
        'inse_nivel_socioeconomico': 4.78,
        'docentes_licenciados_fundamental_pct': 63.4, 'docentes_licenciados_medio_pct': 69.7,
        'tdi_distorcao_fundamental_pct': 1.3, 'tdi_distorcao_medio_pct': 6.1,
        'escolas_com_laboratorio_pct': 45.2,
        'esgotamento_sanitario_pct': 84.2, 'cobertura_atencao_basica_pct': 92.5,
        'acessos_fibra_optica': 12400, 'area_silvicultura_ha': 18500
    },
    {
        'codigo_ibge': 3141804, 'municipio': 'Minas Novas', 'populacao': 24405,
        'pib_per_capita': 14890.20, 'rendimento_medio_sm': 1.6,
        'vab_agropecuaria_pct': 12.1, 'vab_industria_pct': 8.4,
        'vab_servicos_pct': 32.8, 'vab_administracao_publica_pct': 46.7,
        'fpm_dependencia_pct': 78.4,
        'inse_nivel_socioeconomico': 4.57,
        'docentes_licenciados_fundamental_pct': 59.7, 'docentes_licenciados_medio_pct': 67.7,
        'tdi_distorcao_fundamental_pct': 2.8, 'tdi_distorcao_medio_pct': 6.9,
        'escolas_com_laboratorio_pct': 28.0,
        'esgotamento_sanitario_pct': 61.5, 'cobertura_atencao_basica_pct': 98.1,
        'acessos_fibra_optica': 4800, 'area_silvicultura_ha': 9200
    },
    {
        'codigo_ibge': 3169706, 'municipio': 'Turmalina', 'populacao': 20085,
        'pib_per_capita': 22150.80, 'rendimento_medio_sm': 1.9,
        'vab_agropecuaria_pct': 18.3, 'vab_industria_pct': 15.1,
        'vab_servicos_pct': 38.2, 'vab_administracao_publica_pct': 28.4,
        'fpm_dependencia_pct': 58.2,
        'inse_nivel_socioeconomico': 4.69,
        'docentes_licenciados_fundamental_pct': 62.1, 'docentes_licenciados_medio_pct': 68.9,
        'tdi_distorcao_fundamental_pct': 1.5, 'tdi_distorcao_medio_pct': 5.8,
        'escolas_com_laboratorio_pct': 38.5,
        'esgotamento_sanitario_pct': 78.9, 'cobertura_atencao_basica_pct': 95.0,
        'acessos_fibra_optica': 6100, 'area_silvicultura_ha': 14100
    },
    {
        'codigo_ibge': 3102806, 'municipio': 'Angelândia', 'populacao': 8540,
        'pib_per_capita': 12400.30, 'rendimento_medio_sm': 1.3,
        'vab_agropecuaria_pct': 25.1, 'vab_industria_pct': 6.2,
        'vab_servicos_pct': 16.4, 'vab_administracao_publica_pct': 52.3,
        'fpm_dependencia_pct': 84.1,
        'inse_nivel_socioeconomico': 4.35,
        'docentes_licenciados_fundamental_pct': 54.2, 'docentes_licenciados_medio_pct': 61.0,
        'tdi_distorcao_fundamental_pct': 3.1, 'tdi_distorcao_medio_pct': 7.5,
        'escolas_com_laboratorio_pct': 15.0,
        'esgotamento_sanitario_pct': 52.1, 'cobertura_atencao_basica_pct': 100.0,
        'acessos_fibra_optica': 1200, 'area_silvicultura_ha': 4500
    },
    {
        'codigo_ibge': 3100602, 'municipio': 'Água Boa', 'populacao': 13520,
        'pib_per_capita': 13850.40, 'rendimento_medio_sm': 1.4,
        'vab_agropecuaria_pct': 28.4, 'vab_industria_pct': 7.5,
        'vab_servicos_pct': 15.2, 'vab_administracao_publica_pct': 48.9,
        'fpm_dependencia_pct': 81.3,
        'inse_nivel_socioeconomico': 4.41,
        'docentes_licenciados_fundamental_pct': 56.8, 'docentes_licenciados_medio_pct': 63.5,
        'tdi_distorcao_fundamental_pct': 2.9, 'tdi_distorcao_medio_pct': 7.1,
        'escolas_com_laboratorio_pct': 20.0,
        'esgotamento_sanitario_pct': 58.4, 'cobertura_atencao_basica_pct': 96.5,
        'acessos_fibra_optica': 1900, 'area_silvicultura_ha': 3200
    },
    {
        'codigo_ibge': 3116103, 'municipio': 'Chapada do Norte', 'populacao': 15100,
        'pib_per_capita': 10200.10, 'rendimento_medio_sm': 1.2,
        'vab_agropecuaria_pct': 14.2, 'vab_industria_pct': 4.1,
        'vab_servicos_pct': 23.6, 'vab_administracao_publica_pct': 58.1,
        'fpm_dependencia_pct': 89.6,
        'inse_nivel_socioeconomico': 4.22,
        'docentes_licenciados_fundamental_pct': 50.1, 'docentes_licenciados_medio_pct': 58.2,
        'tdi_distorcao_fundamental_pct': 3.8, 'tdi_distorcao_medio_pct': 8.4,
        'escolas_com_laboratorio_pct': 12.5,
        'esgotamento_sanitario_pct': 45.0, 'cobertura_atencao_basica_pct': 100.0,
        'acessos_fibra_optica': 850, 'area_silvicultura_ha': 800
    }
]

df_raw = pd.DataFrame(dados_gold_completos)

# 2. QUERY SQL COMPLETA VIA DUCKDB
query_sql = """
SELECT 
    *,
    ROUND((acessos_fibra_optica * 1000.0) / populacao, 1) AS fibra_por_1k_hab,
    ROUND(GREATEST(0, vab_administracao_publica_pct - 30.0), 1) AS gap_dependencia_publica,
    ROUND(GREATEST(0, 85.0 - docentes_licenciados_medio_pct), 1) AS gap_docentes_medio,
    ROUND(GREATEST(0, 60.0 - escolas_com_laboratorio_pct), 1) AS gap_labs_escolares,
    ROUND(GREATEST(0, 80.0 - esgotamento_sanitario_pct), 1) AS gap_saneamento,
    ROUND(
        (GREATEST(0, vab_administracao_publica_pct - 30.0) * 0.35) + 
        (GREATEST(0, 60.0 - escolas_com_laboratorio_pct) * 0.25) + 
        (GREATEST(0, 80.0 - esgotamento_sanitario_pct) * 0.25) + 
        (GREATEST(0, 85.0 - docentes_licenciados_medio_pct) * 0.15), 1
    ) AS indice_vulnerabilidade_ivm,
    CASE 
        WHEN vab_administracao_publica_pct > 50.0 THEN 'Distrito Agroindustrial Regional & Incentivos Fiscais para Tecnologia'
        WHEN escolas_com_laboratorio_pct < 20.0 THEN 'Internet Satelital (Starlink) + Kits de Laboratórios Móveis Escolares'
        WHEN esgotamento_sanitario_pct < 50.0 THEN 'Captação Novo Marco do Saneamento para Bacias do Jequitinhonha'
        ELSE 'Convênio com Universidades Federais para Licenciatura Modular Docente'
    END AS solucao_prescritiva
FROM df_raw
ORDER BY indice_vulnerabilidade_ivm DESC;
"""
df = duckdb.query(query_sql).to_df()

# 3. FILTRO INTERATIVO NA SIDEBAR
st.sidebar.header("🔎 Inspeção Individual")
cidades_selecionadas = st.sidebar.multiselect(
    "Selecione os Municípios:",
    options=df['municipio'].tolist(),
    default=df['municipio'].tolist()
)
df_view = df[df['municipio'].isin(cidades_selecionadas)].reset_index(drop=True)

# 4. KPIs EXECUTIVOS NO TOPO
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("População Total", f"{df_view['populacao'].sum():,.0f}".replace(",", "."))
c2.metric("PIB per Capita Médio", f"R$ {df_view['pib_per_capita'].mean():,.2f}")
c3.metric("Dependência Pública (VAB)", f"{df_view['vab_administracao_publica_pct'].mean():.1f}%")
c4.metric("Docentes Lic. (Médio)", f"{df_view['docentes_licenciados_medio_pct'].mean():.1f}%")
c5.metric("IVM Médio (Risco)", f"{df_view['indice_vulnerabilidade_ivm'].mean():.1f}")

st.divider()

# 5. ABAS TEMÁTICAS COMPLETAS
aba1, aba2, aba3, aba4, aba5 = st.tabs([
    "🎯 Diagnóstico & Soluções (IVM)",
    "🏫 Educação Completa (INEP)",
    "🏭 Setores Econômicos (VAB & Agro)",
    "🌐 Infraestrutura, Saúde & Fibra",
    "📋 Tabela Master Completa (24 Colunas)"
])

with aba1:
    col_a, col_b = st.columns(2)
    with col_a:
        z_heat = [
            [df.loc[i, 'gap_dependencia_publica'], df.loc[i, 'gap_labs_escolares'],
             df.loc[i, 'gap_saneamento'], df.loc[i, 'gap_docentes_medio']]
            for i in range(len(df))
        ]
        fig_heat = go.Figure(data=go.Heatmap(
            z=z_heat, x=['Gap Econômico', 'Gap Digital Escolar', 'Gap Saneamento', 'Gap Docente'],
            y=df['municipio'], colorscale='Reds',
            text=[[f"{v:.1f}%" for v in row] for row in z_heat], texttemplate="%{text}", showscale=False
        ))
        fig_heat.update_layout(title="<b>Heatmap de Severidade dos Gargalos (%)</b>", template="plotly_dark", height=420)
        st.plotly_chart(fig_heat, use_container_width=True)

    with col_b:
        fig_ivm = go.Figure(data=go.Bar(
            x=df['indice_vulnerabilidade_ivm'], y=df['municipio'], orientation='h',
            text=[f"IVM: {v:.1f}" for v in df['indice_vulnerabilidade_ivm']], textposition='auto',
            marker_color=['#ef553b' if v > 20 else '#ffa15a' if v > 10 else '#00cc96' for v in df['indice_vulnerabilidade_ivm']]
        ))
        fig_ivm.update_layout(title="<b>Ranking de Vulnerabilidade Multissetorial (IVM)</b>", template="plotly_dark", height=420)
        st.plotly_chart(fig_ivm, use_container_width=True)

    st.subheader("Plano de Ação Prescritivo por Município")
    tabela_acoes = df_view[['municipio', 'indice_vulnerabilidade_ivm', 'gap_dependencia_publica', 'gap_labs_escolares', 'solucao_prescritiva']].copy()
    tabela_acoes.columns = ['Município', 'IVM (Risco)', 'Gap Público (%)', 'Gap Labs (%)', 'Solução Prescritiva SQL']
    st.dataframe(tabela_acoes, use_container_width=True, hide_index=True)

with aba2:
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        fig_doc = go.Figure()
        fig_doc.add_trace(go.Bar(name='Fundamental (%)', x=df['municipio'], y=df['docentes_licenciados_fundamental_pct'], marker_color='#17becf', text=df['docentes_licenciados_fundamental_pct'], textposition='auto'))
        fig_doc.add_trace(go.Bar(name='Ensino Médio (%)', x=df['municipio'], y=df['docentes_licenciados_medio_pct'], marker_color='#bcbd22', text=df['docentes_licenciados_medio_pct'], textposition='auto'))
        fig_doc.add_shape(type="line", x0=-0.5, x1=5.5, y0=85, y1=85, line=dict(color="gold", dash="dash", width=2))
        fig_doc.update_layout(title="<b>Formação Docente Adequada (INEP AFD) vs Meta 85%</b>", barmode='group', template="plotly_dark", height=420, yaxis=dict(range=[0, 100]))
        st.plotly_chart(fig_doc, use_container_width=True)

    with col_e2:
        fig_tdi = go.Figure()
        fig_tdi.add_trace(go.Bar(name='TDI Fundamental (%)', x=df['municipio'], y=df['tdi_distorcao_fundamental_pct'], marker_color='#9467bd', text=df['tdi_distorcao_fundamental_pct'], textposition='auto'))
        fig_tdi.add_trace(go.Bar(name='TDI Ensino Médio (%)', x=df['municipio'], y=df['tdi_distorcao_medio_pct'], marker_color='#ef553b', text=df['tdi_distorcao_medio_pct'], textposition='auto'))
        fig_tdi.update_layout(title="<b>Distorção Idade-Série / Atraso Escolar (TDI %)</b>", barmode='group', template="plotly_dark", height=420)
        st.plotly_chart(fig_tdi, use_container_width=True)

    col_e3, col_e4 = st.columns(2)
    with col_e3:
        fig_labs = px.bar(df, x='municipio', y='escolas_com_laboratorio_pct', text='escolas_com_laboratorio_pct', color='escolas_com_laboratorio_pct', color_continuous_scale='Viridis', title="<b>Escolas com Laboratório de Informática (%) [Meta: 60%]</b>", template="plotly_dark")
        fig_labs.add_hline(y=60, line_dash="dash", line_color="cyan")
        st.plotly_chart(fig_labs, use_container_width=True)
    with col_e4:
        fig_inse = px.bar(df, x='municipio', y='inse_nivel_socioeconomico', text='inse_nivel_socioeconomico', color='municipio', title="<b>Nível Socioeconômico Escolar (INSE)</b>", template="plotly_dark")
        fig_inse.update_yaxes(range=[4.0, 5.0])
        st.plotly_chart(fig_inse, use_container_width=True)

with aba3:
    fig_vab = go.Figure()
    setores = [
        ('vab_agropecuaria_pct', 'Agropecuária (%)', '#2ca02c'),
        ('vab_industria_pct', 'Indústria (%)', '#ff7f0e'),
        ('vab_servicos_pct', 'Serviços/Comércio (%)', '#1f77b4'),
        ('vab_administracao_publica_pct', 'Administração Pública (%)', '#d62728')
    ]
    for col, nome, cor in setores:
        fig_vab.add_trace(go.Bar(name=nome, x=df['municipio'], y=df[col], marker_color=cor, text=[f"{v:.1f}%" for v in df[col]], textposition='inside'))
    fig_vab.update_layout(title="<b>Composição Completa do PIB por Setor Econômico (VAB %)</b>", barmode='stack', template="plotly_dark", height=450)
    st.plotly_chart(fig_vab, use_container_width=True)

    col_s1, col_s2 = st.columns(2)
    with col_s1:
        fig_fpm = px.bar(df, x='municipio', y='fpm_dependencia_pct', text='fpm_dependencia_pct', color='fpm_dependencia_pct', color_continuous_scale='OrRd', title="<b>Dependência de Transferências Federais (FPM %)</b>", template="plotly_dark")
        st.plotly_chart(fig_fpm, use_container_width=True)
    with col_s2:
        fig_silv = px.bar(df, x='municipio', y='area_silvicultura_ha', text='area_silvicultura_ha', color='municipio', title="<b>Área de Silvicultura / Eucalipto (Hectares)</b>", template="plotly_dark")
        st.plotly_chart(fig_silv, use_container_width=True)

with aba4:
    col_i1, col_i2 = st.columns(2)
    with col_i1:
        fig_san = px.bar(df, x='municipio', y='esgotamento_sanitario_pct', text='esgotamento_sanitario_pct', color='esgotamento_sanitario_pct', color_continuous_scale='Blues', title="<b>Cobertura de Esgotamento Sanitário (%) [Meta: 80%]</b>", template="plotly_dark")
        fig_san.add_hline(y=80, line_dash="dash", line_color="gold")
        st.plotly_chart(fig_san, use_container_width=True)
    with col_i2:
        fig_fibra = px.bar(df, x='municipio', y='fibra_por_1k_hab', text='fibra_por_1k_hab', color='municipio', title="<b>Densidade de Fibra Óptica (Acessos por 1.000 Habitantes)</b>", template="plotly_dark")
        st.plotly_chart(fig_fibra, use_container_width=True)

with aba5:
    st.subheader("Base Completa da Camada Gold (Todos os Indicadores Consolidados)")
    st.dataframe(df_view, use_container_width=True, hide_index=True)

# 6. RODAPÉ METODOLÓGICO (PORTFÓLIO & TRANSPARÊNCIA)
st.divider()
st.caption(
    "Nota Metodológica: Projeto de portfólio em Engenharia e Análise de Dados. "
    "Consolidado a partir de séries históricas públicas de referência (IBGE — Censo 2022 / Contas Regionais e INEP — Censo Escolar 2023) "
    "e parâmetros calibrados para validação da arquitetura Medallion, modelagem SQL (DuckDB) e cálculo do IVM."
)
