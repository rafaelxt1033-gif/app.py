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
            
    st.markdown("Controle de estoque e vendas detalhado por tipo de peça.")
    st.divider()

    st.subheader("🎛️ Painel de Produtos por Setor")
    
    dados_produtos = []

    # --- SETOR INFANTIL ---
    with st.expander("👶 Setor Infantil (Meninos e Meninas)", expanded=True):
        st.markdown("**1. Camisetas / Blusinhas**")
        est_inf_1 = st.number_input("Estoque Inicial (Camiseta Inf):", 0, 500, 100, key="ei_inf1")
        vend_inf_1 = st.slider("Vendidas (Camiseta Inf):", 0, est_inf_1, 30, key="vi_inf1")
        pr_inf_1 = st.number_input("Preço R$ (Camiseta Inf):", 10, 200, 39, key="pi_inf1")
        dados_produtos.append(['Infantil - Camiseta/Blusinha', est_inf_1, vend_inf_1, pr_inf_1])
        
        st.markdown("---")
        st.markdown("**2. Calças / Bermudas**")
        est_inf_2 = st.number_input("Estoque Inicial (Calça Inf):", 0, 500, 80, key="ei_inf2")
        vend_inf_2 = st.slider("Vendidas (Calça Inf):", 0, est_inf_2, 20, key="vi_inf2")
        pr_inf_2 = st.number_input("Preço R$ (Calça Inf):", 10, 200, 59, key="pi_inf2")
        dados_produtos.append(['Infantil - Calça/Bermuda', est_inf_2, vend_inf_2, pr_inf_2])
        
        st.markdown("---")
        st.markdown("**3. Conjuntos / Vestidos**")
        est_inf_3 = st.number_input("Estoque Inicial (Conjunto Inf):", 0, 500, 60, key="ei_inf3")
        vend_inf_3 = st.slider("Vendidas (Conjunto Inf):", 0, est_inf_3, 15, key="vi_inf3")
        pr_inf_3 = st.number_input("Preço R$ (Conjunto Inf):", 10, 300, 89, key="pi_inf3")
        dados_produtos.append(['Infantil - Conjunto/Vestido', est_inf_3, vend_inf_3, pr_inf_3])

    # --- SETOR MASCULINO ADULTO ---
    with st.expander("👨 Setor Masculino Adulto"):
        st.markdown("**1. Camisetas / Polos**")
        est_masc_1 = st.number_input("Estoque Inicial (Camiseta Masc):", 0, 500, 120, key="ei_masc1")
        vend_masc_1 = st.slider("Vendidas (Camiseta Masc):", 0, est_masc_1, 45, key="vi_masc1")
        pr_masc_1 = st.number_input("Preço R$ (Camiseta Masc):", 10, 200, 69, key="pi_masc1")
        dados_produtos.append(['Masculino - Camiseta/Polo', est_masc_1, vend_masc_1, pr_masc_1])
        
        st.markdown("---")
        st.markdown("**2. Calças Jeans**")
        est_masc_2 = st.number_input("Estoque Inicial (Calça Masc):", 0, 500, 90, key="ei_masc2")
        vend_masc_2 = st.slider("Vendidas (Calça Masc):", 0, est_masc_2, 25, key="vi_masc2")
        pr_masc_2 = st.number_input("Preço R$ (Calça Masc):", 10, 400, 139, key="pi_masc2")
        dados_produtos.append(['Masculino - Calça Jeans', est_masc_2, vend_masc_2, pr_masc_2])
        
        st.markdown("---")
        st.markdown("**3. Bermudas / Shorts**")
        est_masc_3 = st.number_input("Estoque Inicial (Bermuda Masc):", 0, 500, 100, key="ei_masc3")
        vend_masc_3 = st.slider("Vendidas (Bermuda Masc):", 0, est_masc_3, 40, key="vi_masc3")
        pr_masc_3 = st.number_input("Preço R$ (Bermuda Masc):", 10, 300, 89, key="pi_masc3")
        dados_produtos.append(['Masculino - Bermuda/Short', est_masc_3, vend_masc_3, pr_masc_3])

    # --- SETOR FEMININO ADULTO ---
    with st.expander("👩 Setor Feminino Adulto"):
        st.markdown("**1. Blusas / Tops**")
        est_fem_1 = st.number_input("Estoque Inicial (Blusa Fem):", 0, 500, 150, key="ei_fem1")
        vend_fem_1 = st.slider("Vendidas (Blusa Fem):", 0, est_fem_1, 60, key="vi_fem1")
        pr_fem_1 = st.number_input("Preço R$ (Blusa Fem):", 10, 200, 49, key="pi_fem1")
        dados_produtos.append(['Feminino - Blusa/Top', est_fem_1, vend_fem_1, pr_fem_1])
        
        st.markdown("---")
        st.markdown("**2. Calças / Saias**")
        est_fem_2 = st.number_input("Estoque Inicial (Calça Fem):", 0, 500, 100, key="ei_fem2")
        vend_fem_2 = st.slider("Vendidas (Calça Fem):", 0, est_fem_2, 35, key="vi_fem2")
        pr_fem_2 = st.number_input("Preço R$ (Calça Fem):", 10, 400, 119, key="pi_fem2")
        dados_produtos.append(['Feminino - Calça/Saia', est_fem_2, vend_fem_2, pr_fem_2])
        
        st.markdown("---")
        st.markdown("**3. Vestidos / Macacões**")
        est_fem_3 = st.number_input("Estoque Inicial (Vestido Fem):", 0, 500, 80, key="ei_fem3")
        vend_fem_3 = st.slider("Vendidas (Vestido Fem):", 0, est_fem_3, 30, key="vi_fem3")
        pr_fem_3 = st.number_input("Preço R$ (Vestido Fem):", 10, 500, 159, key="pi_fem3")
        dados_produtos.append(['Feminino - Vestido/Macacão', est_fem_3, vend_fem_3, pr_fem_3])

    # 3. PROCESSAMENTO MATEMÁTICO AVANÇADO
    df = pd.DataFrame(dados_produtos, columns=['Produto', 'Estoque Inicial', 'Vendidas', 'Preço Unitário (R$)'])

    df['Faturamento (R$)'] = df['Vendidas'] * df['Preço Unitário (R$)']
    df['Estoque Atual'] = df['Estoque Inicial'] - df['Vendidas']
    df['Status'] = df['Estoque Atual'].apply(lambda x: '🚨 Repor' if x < 20 else '✅ OK')

    st.divider()
    
    # 4. EXIBIÇÃO DOS RESULTADOS NA TELA
    st.subheader("💰 Resumo Financeiro Geral")
    c1, c2, c3 = st.columns(3)
    c1.metric(label="💰 Faturamento Total", value=f"R$ {df['Faturamento (R$)'].sum()},00")
    c2.metric(label="📦 Peças Vendidas", value=f"{df['Vendidas'].sum()} un")
    c3.metric(label="🏬 No Estoque", value=f"{df['Estoque Atual'].sum()} un")
    
    st.divider()
    st.subheader("📋 Relatório por Tipo de Peça")
    st.dataframe(df, use_container_width=True, hide_index=True)
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(label="📥 Baixar Planilha Completa", data=csv, file_name='estoque_detalhado.csv', mime='text/csv', use_container_width=True)

    st.divider()
    st.subheader("📊 Gráfico de Movimentação por Peça")
    
    fig, ax = plt.subplots(figsize=(7, 5))
    y = range(len(df['Produto']))
    altura_barra = 0.35
    
    barras_v = ax.barh([i - altura_barra/2 for i in y], df['Vendidas'], altura_barra, label='Vendidas', color='#0288D1')
    barras_e = ax.barh([i + altura_barra/2 for i in y], df['Estoque Atual'], altura_barra, label='Estoque', color='#B0BEC5')
    
    ax.set_yticks(y)
    ax.set_yticklabels(df['Produto'], fontsize=9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.legend()
    
    st.tight_layout()
    st.pyplot(fig)

    st.caption("🔒 Aplicativo Oficial de Produção.")
