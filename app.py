import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# 1. Configuração de Alta Performance e Design
st.set_page_config(
    page_title="Gráciare | Gestão Executiva",
    page_icon="✨",
    layout="centered"
)

# 2. Injeção de CSS para Interatividade e Elegância (O "Coração" do novo Design)
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=DM+Sans:wght@400;500&display=swap');

        /* Fundo e Fonte Geral */
        .stApp {
            background-color: #FDFCF0;
            font-family: 'DM Sans', sans-serif;
        }

        /* Estilização dos Títulos */
        h1, h2, h3 {
            font-family: 'Playfair Display', serif !important;
            color: #001F3F !important; /* Azul Marinho Gráciare */
        }

        /* Botões Interativos */
        div.stButton > button {
            background-color: #D4AF37 !important; /* Dourado */
            color: white !important;
            border-radius: 25px !important;
            border: none !important;
            padding: 10px 25px !important;
            transition: all 0.3s ease-in-out !important;
            font-weight: 500 !important;
            width: 100%;
        }
        div.stButton > button:hover {
            background-color: #001F3F !important;
            transform: scale(1.05);
            box-shadow: 0px 4px 15px rgba(212, 175, 55, 0.4);
        }

        /* Cartões de Produtos (Expander Customizado) */
        .stExpander {
            background-color: white !important;
            border: 1px solid #E5E0D5 !important;
            border-radius: 15px !important;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.03) !important;
            margin-bottom: 15px !important;
        }

        /* Métricas Elegantes */
        [data-testid="stMetricValue"] {
            color: #D4AF37 !important;
            font-family: 'Playfair Display', serif;
        }
        
        /* Inputs e Sliders */
        .stSlider > div > div > div > div {
            background-color: #D4AF37 !important;
        }
    </style>
""", unsafe_allow_html=True)

def verificar_senha():
    if "autenticado" not in st.session_state:
        st.session_state["autenticado"] = False
    if not st.session_state["autenticado"]:
        
        # Centralização da Logo no Login
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if os.path.exists("logo.jpeg"):
                st.image("logo.jpeg", use_container_width=True)
            else:
                st.title("✨ GRÁCIARE")
            
        with st.form(key="login_form"):
            st.markdown("<h3 style='text-align: center;'>Acesso ao Painel</h3>", unsafe_allow_html=True)
            senha = st.text_input("Chave de Segurança:", type="password")
            botao_entrar = st.form_submit_button("DESBLOQUEAR SISTEMA")
            if botao_entrar:
                if senha == "moda123":
                    st.session_state["autenticado"] = True
                    st.rerun()
                else:
                    st.error("❌ Acesso negado.")
        return False
    return True

if verificar_senha():
    # Cabeçalho Superior
    col_logo, col_sair = st.columns([3, 1])
    with col_logo:
        if os.path.exists("logo.jpeg"):
            st.image("logo.jpeg", width=220)
        else:
            st.header("GRÁCIARE")
    with col_sair:
        st.write("")
        if st.button("Encerrar Sessão"):
            st.session_state["autenticado"] = False
            st.rerun()
            
    st.markdown("<p style='color: #B58D3D; font-style: italic;'>Gestão de elegância e controle de resultados.</p>", unsafe_allow_html=True)
    st.divider()

    # Corpo do Aplicativo
    st.subheader("⚜️ Inventário e Coleções")
    
    dados_produtos = []

    # Configuração dos Setores em Colunas ou Cards
    setores = {
        "👶 Infantil": [
            ("Camiseta/Blusinha", "ei_inf1", "vi_inf1", "pi_inf1", 39),
            ("Calça/Bermuda", "ei_inf2", "vi_inf2", "pi_inf2", 59),
            ("Conjunto/Vestido", "ei_inf3", "vi_inf3", "pi_inf3", 89)
        ],
        "👨 Masculino": [
            ("Camiseta/Polo", "ei_mas1", "vi_mas1", "pi_mas1", 69),
            ("Calça Jeans", "ei_mas2", "vi_mas2", "pi_mas2", 139),
            ("Bermuda/Short", "ei_mas3", "vi_mas3", "pi_mas3", 89)
        ],
        "👩 Feminino": [
            ("Blusa/Top", "ei_fem1", "vi_fem1", "pi_fem1", 49),
            ("Calça/Saia", "ei_fem2", "vi_fem2", "pi_fem2", 119),
            ("Vestido/Macacão", "ei_fem3", "vi_fem3", "pi_fem3", 159)
        ]
    }

    for setor, itens in setores.items():
        with st.expander(setor, expanded=(setor == "👩 Feminino")):
            for nome, k_est, k_vend, k_prec, v_prec in itens:
                col1, col2 = st.columns([2, 1])
                with col1:
                    st.markdown(f"**{nome}**")
                    est = st.number_input(f"Estoque:", 0, 500, 100, key=k_est)
                with col2:
                    st.write("") # alinhamento
                    prec = st.number_input(f"Preço R$:", 10, 1000, v_prec, key=k_prec)
                
                vend = st.slider(f"Unidades Vendidas:", 0, est, 10, key=k_vend)
                dados_produtos.append([f"{setor} - {nome}", est, vend, prec])
                st.markdown("---")

    # Cálculos Avançados
    df = pd.DataFrame(dados_produtos, columns=['Produto', 'Inicial', 'Vendidas', 'Preço'])
    df['Faturamento'] = df['Vendidas'] * df['Preço']
    df['Atual'] = df['Inicial'] - df['Vendidas']

    # Dashboard de Métricas
    st.subheader("💰 Performance Financeira")
    m1, m2, m3 = st.columns(3)
    m1.metric("Faturamento", f"R$ {df['Faturamento'].sum():,.2f}")
    m2.metric("Peças Saídas", f"{df['Vendidas'].sum()} un")
    m3.metric("Giro Estoque", f"{(df['Vendidas'].sum()/df['Inicial'].sum()*100):.1f}%")

    # Gráfico Customizado Estilo "Gráciare Gold"
    st.subheader("📊 Análise de Fluxo")
    fig, ax = plt.subplots(figsize=(8, 5))
    fig.patch.set_facecolor('#FDFCF0') # Fundo igual ao site
    
    cores = ['#001F3F', '#D4AF37'] # Navy e Gold
    df.plot(kind='barh', x='Produto', y=['Vendidas', 'Atual'], ax=ax, color=cores, width=0.7)
    
    ax.set_facecolor('#FDFCF0')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.legend(['Vendidas', 'Em Loja'], frameon=False)
    plt.tight_layout()
    st.pyplot(fig)

    st.divider()
    # Botão de Exportação Elegante
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 EXPORTAR RELATÓRIO EXECUTIVO (CSV)",
        data=csv,
        file_name='relatorio_graciare.csv',
        mime='text/csv'
    )

    st.caption("© 2024 Gráciare - Gestão de Luxo Protegida.")
