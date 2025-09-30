import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ==============================
# Configuração inicial
# ==============================
st.set_page_config(
    page_title="Relatório de Vendas - Nutrição Esportiva e Suplementos",
    layout="wide"
)
st.markdown("## 📊 Relatório de Vendas - Nutrição Esportiva e Suplementos")

# Ajuste global do Seaborn
sns.set(style="whitegrid", palette="muted", font_scale=0.7)

# ==============================
# Carregamento de dados
# ==============================
df = pd.read_csv("data/DT_Store_Suplements_final.csv")
df["Receita"] = df["Preco"] * df["Quantidade"]

# ==============================
# KPIs principais
# ==============================
receita_total = df["Receita"].sum()
ticket_medio = df["Receita"].mean()
total_vendas = len(df)
num_lojas = df["Loja"].nunique()

col1, col2, col3, col4 = st.columns(4, gap="small")
col1.metric("💰 Receita", f"R$ {receita_total:,.0f}")
col2.metric("🛒 Ticket Médio", f"R$ {ticket_medio:,.0f}")
col3.metric("📦 Vendas", total_vendas)
col4.metric("🏬 Lojas", num_lojas)

st.markdown("---")

# ==============================
# Linha 1: Produtos e Marcas
# ==============================
st.subheader("📦 Produtos e Marcas")

col1, col2 = st.columns(2)

with col1:
    st.markdown("**🏆 Top 5 Produtos mais Vendidos**")
    top_produtos = df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False).head(5)
    fig, ax = plt.subplots(figsize=(4,2.5))
    sns.barplot(x=top_produtos.values, y=top_produtos.index, palette="Blues_r", ax=ax)
    ax.set_xlabel("Qtd")
    ax.set_ylabel("")
    st.pyplot(fig, clear_figure=True)

with col2:
    st.markdown("**🏷️ Top Marcas por Receita**")
    top_marcas = df.groupby("Marca")["Receita"].sum().sort_values(ascending=False).head(5)
    fig, ax = plt.subplots(figsize=(4,2.5))
    sns.barplot(x=top_marcas.values, y=top_marcas.index, palette="Oranges_r", ax=ax)
    ax.set_xlabel("Receita (R$)")
    ax.set_ylabel("")
    st.pyplot(fig, clear_figure=True)

st.markdown("---")

# ==============================
# Linha 2: Pagamentos e Lojas
# ==============================
st.subheader("💳 Pagamentos e Receita por Loja")

col3, col4 = st.columns(2)

with col3:
    st.markdown("**💳 Formas de Pagamento**")
    fig, ax = plt.subplots(figsize=(3,3))
    df["Pagamento"].value_counts().plot.pie(
        autopct="%.0f%%", startangle=90, colors=sns.color_palette("pastel"), ax=ax
    )
    ax.set_ylabel("")
    st.pyplot(fig, clear_figure=True)

with col4:
    st.markdown("**🏬 Receita por Loja**")
    receita_lojas = df.groupby("Loja")["Receita"].sum()
    fig, ax = plt.subplots(figsize=(4,2.5))
    sns.barplot(x=receita_lojas.index, y=receita_lojas.values, palette="Purples_r", ax=ax)
    ax.set_ylabel("")
    ax.set_xlabel("")
    st.pyplot(fig, clear_figure=True)
