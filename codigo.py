# Titulo - Sistema de vendas 
# Seção cadastrar vendas
    # campo data
    # campo vendedor 
    # campo produto
    # campo quantidade
    # campo valor
    # botão cadastrar vendas
        # quando eu clicar no botão -> adicionar a venda na tabela 
# Seção vendas cadastradas
    # tabela com as vendas 
# Seção dashboard
    # Card/Métrica -> Faturamento Total
    # Gráfico de Barra/Coluna -> Venda por Vendedor 
    # Gráfico de Pizza -> Venda por Produto

import streamlit as st
import pandas as pd
import plotly.express as px

# carregar base de dados
tabela_vendas = pd.read_csv("vendas.csv")

st.write("# Sistema de Vendas")

# seção cadastrar vendas 
st.sidebar.write("## Cadastrar Vendas")
data = st.sidebar.date_input("Data")
vendedor = st.sidebar.selectbox("Vendedor", ["Ana", "Bruno", "Carla", "Matheus", "Isabela", "Eliel"])
produto = st.sidebar.selectbox("Produto",["Notebook", "Celular", "Fone", "Tablet", "Powerbank", "Teclado", "Mouse", "Computador"])
quantidade = st.sidebar.number_input("Quantidade", step=1)
valor = st.sidebar.number_input("Valor")
botao_cadastrar = st.sidebar.button("Cadastrar Vendas")

#logica de cadastro
if botao_cadastrar:
    nova_venda = [str(data), vendedor, produto, quantidade, valor]
    ultima_linha = len(tabela_vendas)
    tabela_vendas.loc[ultima_linha] = nova_venda
    tabela_vendas.to_csv("vendas.csv", index=False)
    st.success("Venda Cadastrada!")

# seção de visualizar vendas 
st.write("## Vendas Cadastradas")
st.dataframe(tabela_vendas)


# seção de Dashboard 
st.write("## Dashboard")

# Card/Métrica -> Faturamento Total
faturamento = tabela_vendas["valor"].sum()
st.metric("Faturamento Total", f"R$ {faturamento}")

# Gráfico de Barra/Coluna -> Venda por Vendedor
grafico1 = px.bar(tabela_vendas, x="vendedor", y="valor", color="produto")
st.plotly_chart(grafico1)

# Gráfico de Pizza -> Venda por Produto
grafico2 = px.pie(tabela_vendas, names="produto", values="valor")
st.plotly_chart(grafico2)





