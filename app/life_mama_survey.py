import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Configuração da página
st.set_page_config(page_title="Pesquisa Life Mama", layout="wide")

# Cores da marca
COR_PRINCIPAL = "#F5A623"  # Laranja
COR_SECUNDARIA = "#4A90E2"  # Azul
COR_FUNDO = "#F9F9F9"  # Cinza claro

# Estilo CSS personalizado
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {COR_FUNDO};
    }}
    .stButton > button {{
        background-color: {COR_PRINCIPAL};
        color: white;
        font-size: 20px;
        padding: 10px 24px;
        border-radius: 5px;
        border: none;
        cursor: pointer;
    }}
    .stButton > button:hover {{
        background-color: {COR_SECUNDARIA};
    }}
    h1, h2, h3, p {{
        color: black !important;
    }}
    .question {{
        font-size: 24px;
        color: {COR_SECUNDARIA} !important;
        margin-bottom: 20px;
    }}
    </style>
    """, unsafe_allow_html=True)

# Função para salvar respostas
def salvar_respostas(respostas):
    df = pd.DataFrame([respostas])
    df['timestamp'] = datetime.now()
    df.to_csv('respostas_pesquisa.csv', mode='a', header=False, index=False)

# Inicialização de variáveis de estado
if 'page' not in st.session_state:
    st.session_state.page = 0
if 'respostas' not in st.session_state:
    st.session_state.respostas = {}

# Lista de perguntas
perguntas = [
    {
        "pergunta": "Você estaria disposta a pagar por um aplicativo que ajuda a organizar sua rotina e a cuidar do seu bem-estar?",
        "tipo": "radio",
        "opcoes": ["Sim", "Não"]
    },
    {
        "pergunta": "Se sim, qual faixa de valor você considera justa para pagar mensalmente por um app que apoie sua organização e autocuidado?",
        "tipo": "selectbox",
        "opcoes": ["Não estaria disposta a pagar", "Menos de R$10 / mês", "R$10 a R$20 / mês", "R$20 a R$30 / mês", "Mais de R$30 / mês"]
    },
    {
        "pergunta": "Quais recursos ou funcionalidades no aplicativo fariam com que você considerasse o pagamento da assinatura?",
        "tipo": "multiselect",
        "opcoes": ["Lembretes de rotina", "Dicas de autocuidado", "Monitoramento de saúde"]
    },
    {
        "pergunta": "Selecione os itens que você possui na sua casa atualmente:",
        "tipo": "multiselect",
        "opcoes": ["Carro próprio", "TV a cabo ou streaming", "Computador ou notebook", "Internet banda larga", "Geladeira duplex", "Ar-condicionado", "Nenhum destes"]
    },
    {
        "pergunta": "Atualmente, onde você busca soluções para organizar sua rotina ou cuidar de seu bem-estar e saúde mental?",
        "tipo": "text_area"
    },
    {
        "pergunta": "Quais são os maiores desafios ou limitações que você encontra nas soluções que usa hoje?",
        "tipo": "text_area"
    },
    {
        "pergunta": "O que faz você baixar um aplicativo novo?",
        "tipo": "multiselect",
        "opcoes": ["Recomendação de amigos ou conhecidos", "Avaliações positivas na loja de apps", "Funcionalidades úteis para meu dia a dia", "Facilidade de uso"]
    },
    {
        "pergunta": "O que faz você manter um aplicativo no celular após baixá-lo?",
        "tipo": "multiselect",
        "opcoes": ["Uso frequente", "Atualizações e melhorias constantes", "Ajuda na organização e ganho de tempo", "Oferece benefícios ou recompensas"]
    },
    {
        "pergunta": "Você já utilizou algum aplicativo especificamente voltado para mães?",
        "tipo": "radio",
        "opcoes": ["Sim", "Não"]
    },
    {
        "pergunta": "Se sim, qual aplicativo?",
        "tipo": "text_input"
    },
    {
        "pergunta": "Se você toparia dar continuidade neste papo, deixe seu WhatsApp e email para participar de uma entrevista em profundidade.",
        "tipo": "text_input"
    }
]

# Função para exibir a pergunta atual
def mostrar_pergunta(index):
    pergunta = perguntas[index]
    st.markdown(f"<div class='question'>{pergunta['pergunta']}</div>", unsafe_allow_html=True)
    
    if pergunta['tipo'] == 'radio':
        resposta = st.radio("", pergunta['opcoes'], key=f"pergunta_{index}")
    elif pergunta['tipo'] == 'selectbox':
        resposta = st.selectbox("", pergunta['opcoes'], key=f"pergunta_{index}")
    elif pergunta['tipo'] == 'multiselect':
        resposta = st.multiselect("", pergunta['opcoes'], key=f"pergunta_{index}")
    elif pergunta['tipo'] == 'text_area':
        resposta = st.text_area("", key=f"pergunta_{index}")
    elif pergunta['tipo'] == 'text_input':
        resposta = st.text_input("", key=f"pergunta_{index}")
    
    st.session_state.respostas[f"pergunta_{index}"] = resposta

# Logo
logo_path = os.path.join(os.path.dirname(__file__), "Camada_1 (3).png")
if os.path.exists(logo_path):
    st.image(logo_path, width=200)
else:
    st.warning(f"Logo não encontrado em: {logo_path}")

# Título e introdução
st.title("Pesquisa Life Mama")

# Exibir página atual
if st.session_state.page == 0:
    st.write("""
    Olá!
    Estamos em desenvolvimento de uma solução digital voltada à rotina materna.

    Ao participar você estará contribuindo voluntariamente com seus dados, que não serão divulgados.

    Para tirar dúvidas, entre em contato com 
    Valéria Rezende, Chief Marketing Officer CMO, pelo telefone: 11 98144 7031
    """)
    if st.button("Começar"):
        st.session_state.page += 1
        st.experimental_rerun()
elif st.session_state.page <= len(perguntas):
    mostrar_pergunta(st.session_state.page - 1)
    col1, col2, col3 = st.columns([1,1,1])
    with col1:
        if st.button("Anterior") and st.session_state.page > 1:
            st.session_state.page -= 1
            st.experimental_rerun()
    with col3:
        if st.button("Próxima"):
            if st.session_state.page < len(perguntas):
                st.session_state.page += 1
                st.experimental_rerun()
            else:
                salvar_respostas(st.session_state.respostas)
                st.session_state.page = len(perguntas) + 1
                st.experimental_rerun()
else:
    st.success("Obrigado por participar da nossa pesquisa!")
    if st.button("Reiniciar"):
        st.session_state.page = 0
        st.session_state.respostas = {}
        st.experimental_rerun()

# Rodapé
st.markdown("---")
st.write("© 2024 Life Mama. Todos os direitos reservados.")

# Depuração
st.sidebar.write(f"Diretório atual: {os.getcwd()}")
st.sidebar.write(f"Arquivos no diretório: {os.listdir()}")