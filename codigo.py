# Passo a passo

# título - Sistema de vendas
# Seção Cadastrar Vendas
    # Campo Data
    # Campo Vendedor - Ana, Bruno, Carla
    # Campo Produto - Notebook, Fone, Celular
    # Campo Quantidade
    # Campo Valor
    # Botão Cadastrar Venda
        # quando eu clicar no botão -> adicionar a venda na tabela
# Seção Vendas Cadastradas
    # Tabela com as Vendas
# Seção Dashboard
    # Card/Métrica -> Faturamento Total
    # Gráfico de Barra/Coluna -> Venda por vendedor
    # Gráfico de Pizza -> Venda por produto

# Ferramentas
    # streamlit - é responsável por criar sites e apps do python
    # pandas - trabalha com base de dados
    # plotly - é responsável por criar gráficos

# Para baixar as libs deve ser executado o comando no terminal:
    # pip install streamlit pandas plotly

# Para visualizar o projeto localmente trabalhando com a lib streamlit, deve ser executado o comando no terminal:
    # streamlit run nome_do_arquivo
    # Exemplo: streamlit run codigo.py

import streamlit as st
import pandas as pd
import plotly.express as px

# carregar a base de vendas
tabela_vendas = pd.read_csv("vendas.csv")

st.write("# Sistemas de Vendas")

# seção de cadastros de vendas
st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data",)
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla"])
produto = st.sidebar.selectbox("Produto", ["Notebook", "Celular", "Fone"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar Venda")

if botao_cadastrar:
    if data == "":
        st.warning("O campo de Data deve estar preenchido.")
    elif quantidade == 0:
        st.warning("O campo de Quantidade deve estar preenchido.")
    elif valor == 0:
        st.warning("O campo de Valor deve estar preenchido.")
    else:
        nova_venda = [str(data), vendedor, produto, quantidade, valor]
        ultima_linha = len(tabela_vendas)
        tabela_vendas.loc[ultima_linha] = nova_venda
        tabela_vendas.to_csv("vendas.csv", index=False)
        st.success("Venda cadastrada!")

# seção de visualizar as vendas
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)

# seção de Dashboard
st.write("## Dashboard")

# Card/Métrica -> Faturamento Total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento total", f"R${faturamento:.2f}")

# Gráfico de Barra/Coluna -> Venda por vendedor
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)

# Gráfico de Pizza -> Venda por produto
grafico2 = px.pie(tabela_vendas, names="produto", values="valor", hole=0.5)
st.plotly_chart(grafico2)
