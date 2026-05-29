import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Configuração da página e estilização de Cores (Dourado e Elegante)
st.set_page_config(
    page_title="Gráciare - Gestão", 
    layout="centered", 
    initial_sidebar_state="collapsed"
)

# Injeta CSS personalizado para mudar a cor dos botões e fontes para combinar com o Dourado/Sofisticado
st.markdown("""
    <style>
        /* Altera a cor de fundo geral do site para um branco elegante */
        .stApp {
            background-color: #FFFFFF;
        }
        /* Estiliza os títulos secundários com um tom de dourado escuro/bronze para leitura */
        h1, h2, h3 {
            color: #B58D3D !important;
            font-family: 'Georgia', serif;
        }
        /* Estiliza as métricas financeiras */
        [data-testid="stMetricValue"] {
            color: #B58D3D !important;
        }
    </style>
""", unsafe_allow_html=True)


def verificar_senha():
    if "autenticado" not in st.session_state:
        st.session_state["autenticado"] = False
    if not st.session_state["autenticado"]:
        
        # Exibe a logo no topo da tela de login também!
        if os.path.exists("logo.jpeg"):
            st.image("logo.jpeg", use_container_width=True)
        else:
            st.title("✨ GRÁCIARE")
            
        with st.form(key="login_form"):
            st.subheader("🔒 Acesso Restrito ao Sistema")
            senha = st.text_input("Senha de Gerente:", type="password")
            botao_entrar = st.form_submit_button("Entrar no Painel")
            if botao_entrar:
                if senha == "moda123":
                    st.session_state["autenticado"] = True
                    st.rerun()
                else:
                    st.error("❌ Senha incorreta.")
        return False
    return True

if verificar_senha():
    # --- CABEÇALHO DO SITE COM A LOGO MARCA ---
    col_logo, col_sair = st.columns([4, 1])
    with col_logo:
        # Se a imagem existir na pasta, ele mostra a logo dourada maravilhosa
        if os.path.exists("logo.jpeg"):
            st.image("logo.jpeg", width=280)
        else:
            st.title("✨ GRÁCIARE")
    with col_sair:
        st.write("") # Espaçamento visual
        if st.button("Sair"):
            st.session_state["autenticado"] = False
            st.rerun()
            
    st.markdown("*Painel Executivo de Controle de Estoque e Vendas.*")
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
    
    # Cores do gráfico ajustadas para tons combinando com a marca (Azul Marinho sofisticado e Cinza)
    barras_v = ax.barh([i - altura_barra/2 for i in y], df['Vendidas'], altura_barra, label='Vendidas', color='#1A2E40')
    barras_e = ax.barh([i + altura_barra/2 for i in y], df['Estoque Atual'], altura_barra, label='Estoque', color='#D4AF37')
    
    ax.set_yticks(y)
    ax.set_yticklabels(df['Produto'], fontsize=9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.legend()
    
    st.tight_layout()
    st.pyplot(fig)

    st.caption("🔒 Aplicativo Oficial de Produção - Gráciare.")
    
