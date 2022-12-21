# pip install pandas streamlit plotly.express xlrd

import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image
icone = Image.open(caminho_icone)
st.set_page_config(page_title="DASHBOARD RODOBROTTO", page_icon=icone, layout="wide")

planilha = st.sidebar.file_uploader(label='Planilha Fornecedor', type='xls')


dashboard = st.sidebar.radio("Escolha Planilha",('Fornecedor', 'Clientes',))

if dashboard == 'Fornecedor':
    if planilha == None:
        planilha = 'Fornecedores.xls'
        # dados
        df = pd.read_excel(io=planilha)
        # parametros
        ParametroUm = st.sidebar.selectbox(label='Parâmentro 1:', options=df.columns, key='<ParametroUm>', index=2)
        ParametroDois = st.sidebar.selectbox(label='Parâmentro 2:', options=df.columns, key='<ParametroDois>', index=12)
        ParametroTres = st.sidebar.selectbox(label='Parâmentro 3:', options=df.columns, key='<ParametroTres>', index=2)
        ParametroQuatro = st.sidebar.selectbox(label='Parâmentro 4:', options=df.columns, key='<ParametroQuatro>', index=12)
        ParametroCinco = st.sidebar.selectbox(label='Parâmentro 5:', options=df.columns, key='<ParametroCinco>', index=33)
        ParametroSeis = st.sidebar.selectbox(label='Parâmentro 6:', options=df.columns, key='<ParametroSeis>', index=12)
        # tela
        col1, col2 = st.columns(2)
        # grafico
        GraficoUmDados = (
            df.groupby(by=[f"{ParametroUm}"]).sum()[[f"{ParametroDois}"]].sort_values(by=f"{ParametroDois}"))
        GraficoUm = px.bar(
            GraficoUmDados,
            x=f"{ParametroDois}",
            y=GraficoUmDados.index,
            text_auto='.2s',
            orientation="h",
            title="<b>VALOR</b>",
            color_discrete_sequence=["#FF9900"] * len(GraficoUmDados),
            template="plotly_white", )
        GraficoUm.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False)))
        col1.plotly_chart(GraficoUm, use_container_width=True)
        # grafico
        GraficoDoisDados = (
            df.groupby(by=[f"{ParametroTres}"]).count()[[f"{ParametroQuatro}"]].sort_values(by=f"{ParametroQuatro}"))
        GraficoDois = px.bar(
            GraficoDoisDados,
            x=f"{ParametroQuatro}",
            y=GraficoDoisDados.index,
            text_auto='.2s',
            orientation="h",
            title="<b>QUANTIDADE</b>",
            color_discrete_sequence=["#FF9900"] * len(GraficoDoisDados),
            template="plotly_white", )
        GraficoDois.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False)))
        col2.plotly_chart(GraficoDois, use_container_width=True)
        # grafico
        GraficoTresDados = (
            df.groupby(by=[f"{ParametroCinco}"]).count()[[f"{ParametroSeis}"]].sort_values(by=f"{ParametroSeis}"))
        GraficoTres = px.bar(
            GraficoTresDados,
            x=f"{ParametroSeis}",
            y=GraficoTresDados.index,
            text_auto='.2s',
            orientation="h",
            title="<b>OPERADOR</b>",
            color_discrete_sequence=["#FF9900"] * len(GraficoTresDados),
            template="plotly_white", )
        GraficoTres.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False)))
        st.plotly_chart(GraficoTres, use_container_width=True)
    else:
        # dados
        df = pd.read_excel(io=planilha)
        # parametros
        ParametroUm = st.sidebar.selectbox(label='Parâmentro 1:', options=df.columns, key='<ParametroUm>', index=2)
        ParametroDois = st.sidebar.selectbox(label='Parâmentro 2:', options=df.columns, key='<ParametroDois>', index=12)
        ParametroTres = st.sidebar.selectbox(label='Parâmentro 3:', options=df.columns, key='<ParametroTres>', index=2)
        ParametroQuatro = st.sidebar.selectbox(label='Parâmentro 4:', options=df.columns, key='<ParametroQuatro>',
                                               index=12)
        ParametroCinco = st.sidebar.selectbox(label='Parâmentro 5:', options=df.columns, key='<ParametroCinco>',
                                              index=33)
        ParametroSeis = st.sidebar.selectbox(label='Parâmentro 6:', options=df.columns, key='<ParametroSeis>', index=12)
        # tela
        col1, col2 = st.columns(2)
        # grafico
        GraficoUmDados = (
            df.groupby(by=[f"{ParametroUm}"]).sum()[[f"{ParametroDois}"]].sort_values(by=f"{ParametroDois}"))
        GraficoUm = px.bar(
            GraficoUmDados,
            x=f"{ParametroDois}",
            y=GraficoUmDados.index,
            text_auto='.2s',
            orientation="h",
            title="<b>VALOR</b>",
            color_discrete_sequence=["#FF9900"] * len(GraficoUmDados),
            template="plotly_white", )
        GraficoUm.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False)))
        col1.plotly_chart(GraficoUm, use_container_width=True)
        # grafico
        GraficoDoisDados = (
            df.groupby(by=[f"{ParametroTres}"]).count()[[f"{ParametroQuatro}"]].sort_values(by=f"{ParametroQuatro}"))
        GraficoDois = px.bar(
            GraficoDoisDados,
            x=f"{ParametroQuatro}",
            y=GraficoDoisDados.index,
            text_auto='.2s',
            orientation="h",
            title="<b>QUANTIDADE</b>",
            color_discrete_sequence=["#FF9900"] * len(GraficoDoisDados),
            template="plotly_white", )
        GraficoDois.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False)))
        col2.plotly_chart(GraficoDois, use_container_width=True)
        # grafico
        GraficoTresDados = (
            df.groupby(by=[f"{ParametroCinco}"]).count()[[f"{ParametroSeis}"]].sort_values(by=f"{ParametroSeis}"))
        GraficoTres = px.bar(
            GraficoTresDados,
            x=f"{ParametroSeis}",
            y=GraficoTresDados.index,
            text_auto='.2s',
            orientation="h",
            title="<b>OPERADOR</b>",
            color_discrete_sequence=["#FF9900"] * len(GraficoTresDados),
            template="plotly_white", )
        GraficoTres.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False)))
        st.plotly_chart(GraficoTres, use_container_width=True)
if dashboard == 'Clientes':
    if planilha == None:
        planilha = 'Clientes.xls'
        # dados
        df = pd.read_excel(io=planilha)
        # parametros
        ParametroUm = st.sidebar.selectbox(label='Parâmentro 1:', options=df.columns, key='<ParametroUm>', index=14)
        ParametroDois = st.sidebar.selectbox(label='Parâmentro 2:', options=df.columns, key='<ParametroDois>', index=3)
        ParametroTres = st.sidebar.selectbox(label='Parâmentro 3:', options=df.columns, key='<ParametroTres>', index=14)
        ParametroQuatro = st.sidebar.selectbox(label='Parâmentro 4:', options=df.columns, key='<ParametroQuatro>',
                                               index=3)
        ParametroCinco = st.sidebar.selectbox(label='Parâmentro 5:', options=df.columns, key='<ParametroCinco>',
                                              index=23)
        ParametroSeis = st.sidebar.selectbox(label='Parâmentro 6:', options=df.columns, key='<ParametroSeis>', index=3)
        # tela
        col1, col2 = st.columns(2)
        # grafico
        GraficoUmDados = (
            df.groupby(by=[f"{ParametroUm}"]).sum()[[f"{ParametroDois}"]].sort_values(by=f"{ParametroDois}"))
        GraficoUm = px.bar(
            GraficoUmDados,
            x=f"{ParametroDois}",
            y=GraficoUmDados.index,
            text_auto='.2s',
            orientation="h",
            title="<b>VALOR</b>",
            color_discrete_sequence=["#FF9900"] * len(GraficoUmDados),
            template="plotly_white", )
        GraficoUm.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False)))
        col1.plotly_chart(GraficoUm, use_container_width=True)
        # grafico
        GraficoDoisDados = (
            df.groupby(by=[f"{ParametroTres}"]).count()[[f"{ParametroQuatro}"]].sort_values(by=f"{ParametroQuatro}"))
        GraficoDois = px.bar(
            GraficoDoisDados,
            x=f"{ParametroQuatro}",
            y=GraficoDoisDados.index,
            text_auto='.2s',
            orientation="h",
            title="<b>QUANTIDADE</b>",
            color_discrete_sequence=["#FF9900"] * len(GraficoDoisDados),
            template="plotly_white", )
        GraficoDois.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False)))
        col2.plotly_chart(GraficoDois, use_container_width=True)
        # grafico
        GraficoTresDados = (
            df.groupby(by=[f"{ParametroCinco}"]).count()[[f"{ParametroSeis}"]].sort_values(by=f"{ParametroSeis}"))
        GraficoTres = px.bar(
            GraficoTresDados,
            x=f"{ParametroSeis}",
            y=GraficoTresDados.index,
            text_auto='.2s',
            orientation="h",
            title="<b>OPERADOR</b>",
            color_discrete_sequence=["#FF9900"] * len(GraficoTresDados),
            template="plotly_white", )
        GraficoTres.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False)))
        st.plotly_chart(GraficoTres, use_container_width=True)
    else:
        # dados
        df = pd.read_excel(io=planilha)
        # parametros
        ParametroUm = st.sidebar.selectbox(label='Parâmentro 1:', options=df.columns, key='<ParametroUm>', index=14)
        ParametroDois = st.sidebar.selectbox(label='Parâmentro 2:', options=df.columns, key='<ParametroDois>', index=3)
        ParametroTres = st.sidebar.selectbox(label='Parâmentro 3:', options=df.columns, key='<ParametroTres>', index=14)
        ParametroQuatro = st.sidebar.selectbox(label='Parâmentro 4:', options=df.columns, key='<ParametroQuatro>', index=3)
        ParametroCinco = st.sidebar.selectbox(label='Parâmentro 5:', options=df.columns, key='<ParametroCinco>', index=23)
        ParametroSeis = st.sidebar.selectbox(label='Parâmentro 6:', options=df.columns, key='<ParametroSeis>', index=3)
        # tela
        col1, col2 = st.columns(2)
        # grafico
        GraficoUmDados = (
            df.groupby(by=[f"{ParametroUm}"]).sum()[[f"{ParametroDois}"]].sort_values(by=f"{ParametroDois}"))
        GraficoUm = px.bar(
            GraficoUmDados,
            x=f"{ParametroDois}",
            y=GraficoUmDados.index,
            text_auto='.2s',
            orientation="h",
            title="<b>VALOR</b>",
            color_discrete_sequence=["#FF9900"] * len(GraficoUmDados),
            template="plotly_white", )
        GraficoUm.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False)))
        col1.plotly_chart(GraficoUm, use_container_width=True)
        # grafico
        GraficoDoisDados = (
            df.groupby(by=[f"{ParametroTres}"]).count()[[f"{ParametroQuatro}"]].sort_values(by=f"{ParametroQuatro}"))
        GraficoDois = px.bar(
            GraficoDoisDados,
            x=f"{ParametroQuatro}",
            y=GraficoDoisDados.index,
            text_auto='.2s',
            orientation="h",
            title="<b>QUANTIDADE</b>",
            color_discrete_sequence=["#FF9900"] * len(GraficoDoisDados),
            template="plotly_white", )
        GraficoDois.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False)))
        col2.plotly_chart(GraficoDois, use_container_width=True)
        # grafico
        GraficoTresDados = (
            df.groupby(by=[f"{ParametroCinco}"]).count()[[f"{ParametroSeis}"]].sort_values(by=f"{ParametroSeis}"))
        GraficoTres = px.bar(
            GraficoTresDados,
            x=f"{ParametroSeis}",
            y=GraficoTresDados.index,
            text_auto='.2s',
            orientation="h",
            title="<b>OPERADOR</b>",
            color_discrete_sequence=["#FF9900"] * len(GraficoTresDados),
            template="plotly_white", )
        GraficoTres.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            xaxis=(dict(showgrid=False)))
        st.plotly_chart(GraficoTres, use_container_width=True)
