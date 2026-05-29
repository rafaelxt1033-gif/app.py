import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Layout Mobile First limpo
st.set_page_config(page_title="App Lojista", layout="centered", initial_sidebar_state="collapsed")

def verificar_senha():
    if "autenticado" not in st.session_state:
        st.session_state["autenticado"] = False
    if not st.session_state["autenticado"]:
        with st.form(key="login_form"):
            st.subheader("🔒 Acesso Restrito")
            senha = st.text_input("Senha de Gerente:", type="password")
            botao_entrar = st.form_submit_button("Entrar")
            if botao_entrar:
                if senha == "moda123":
                    st.session_state["autenticado"] = True
                    st.rerun()
                else:
                    st.error("❌ Senha incorreta.")
        return False
    return True

if verificar_senha():
    col_titulo, col_sair = st.columns([4, 1])
    with col_titulo:
        st.title("📱 Gestão da Loja")
    with col_sair:
        if st.button("Sair"):
            st.session_state["autenticado"] = False
            st.rerun()
            
    st.markdown("Controle rápido de estoque, vendas e preços por setor.")
    st.divider()

    st.subheader("🎛️ Painel de Produtos e Preços")
    
    # --- SETOR INFANTIL ---
    with st.expander("👶 Roupas Infantis", expanded=True):
        est_infantil = st.number_input("Estoque Inicial (Infantil):", 0, 500, 150, key="est_inf")
        vendas_infantil = st.slider("Peças Vendidas (Infantil):", 0, est_infantil, 40, key="vend_inf")
        # Preço exclusivo para o setor infantil
        preco_infantil = st.number_input("Preço de Venda (Infantil) R$:", 10, 200, 49, key="pr_inf")

    # --- SETOR MASCULINO ---
    with st.expander("👨 Masculino Adulto"):
        est_masc = st.number_input("Estoque Inicial (Masc Adulto):", 0, 500, 200, key="est_masc")
        vendas_masc = st.slider("Peças Vendidas (Masc Adulto):", 0, est_masc, 95, key="vend_masc")
        # Preço exclusivo para o setor masculino
        preco_masc = st.number_input("Preço de Venda (Masc Adulto) R$:", 10, 300, 79, key="pr_masc")

    # --- SETOR FEMININO ---
    with st.expander("👩 Feminino Adulto"):
        est_fem = st.number_input("Estoque Inicial (Fem Adulto):", 0, 500, 250, key="est_fem")
        vendas_fem = st.slider("Peças Vendidas (Fem Adulto):", 0, est_fem, 130, key="vend_fem")
        # Preço exclusivo para o setor feminino
        preco_fem = st.number_input("Preço de Venda (Fem Adulto) R$:", 10, 400, 99, key="pr_fem")

    # 3. PROCESSAMENTO MATEMÁTICO DOS DADOS
    df = pd.DataFrame({
        'Categoria': ['Infantil', 'Masculino Adulto', 'Feminino Adulto'],
        'Estoque Inicial': [est_infantil, est_masc, est_fem],
        'Vendidas': [vendas_infantil, vendas_masc, vendas_fem],
        'Preço Unitário (R$)': [preco_infantil, preco_masc, preco_fem] # Aplicando os preços separados aqui!
    })

    # O sistema calcula o faturamento multiplicando as vendas pelo preço específico de cada um
    df['Faturamento (R$)'] = df['Vendidas'] * df['Preço Unitário (R$)']
    df['Estoque Atual'] = df['Estoque Inicial'] - df['Vendidas']
    df['Status'] = df['Estoque Atual'].apply(lambda x: '🚨 Repor' if x < 30 else '✅ OK')

    st.divider()
    
    # 4. EXIBIÇÃO DOS RESULTADOS NA TELA
    st.subheader("💰 Resumo Financeiro")
    c1, c2, c3 = st.columns(3)
    c1.metric(label="💰 Faturamento Total", value=f"R$ {df['Faturamento (R$)'].sum()},00")
    c2.metric(label="📦 Peças Vendidas", value=f"{df['Vendidas'].sum()} un")
    c3.metric(label="🏬 No Estoque", value=f"{df['Estoque Atual'].sum()} un")
    
    st.divider()
    st.subheader("📋 Relatório Geral")
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(label="📥 Baixar Planilha Excel", data=csv, file_name='estoque_vendas.csv', mime='text/csv', use_container_width=True)

    st.divider()
    st.subheader("📊 Gráfico de Estoque")
    fig, ax = plt.subplots(figsize=(6, 3.5))
    y = range(len(df['Categoria']))
    altura_barra = 0.35
    barras_v = ax.barh([i - altura_barra/2 for i in y], df['Vendidas'], altura_barra, label='Vendidas', color='#0288D1')
    barras_e = ax.barh([i + altura_barra/2 for i in y], df['Estoque Atual'], altura_barra, label='Estoque', color='#B0BEC5')
    ax.set_yticks(y)
    ax.set_yticklabels(df['Categoria'])
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.legend()
    ax.bar_label(barras_v, padding=3, color='#0288D1', fontweight='bold')
    ax.bar_label(barras_e, padding=3, color='#37474F', fontweight='bold')
    st.pyplot(fig)

    st.caption("🔒 Aplicativo Oficial de Produção.")
   
