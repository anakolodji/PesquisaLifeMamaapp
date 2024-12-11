import streamlit as st
import pandas as pd
from datetime import datetime

# Configuração da página
st.set_page_config(page_title="Pesquisa Life Mama", layout="wide")

# Cores da marca
cor_principal = "#F5A623"  # Laranja
cor_secundaria = "#4A90E2"  # Azul
cor_fundo = "#F9F9F9"  # Cinza claro

# Estilo CSS personalizado
st.markdown(f"""
    <style>
    .stApp {{
        background-color: {cor_fundo};
    }}
    .stButton > button {{
        background-color: {cor_principal};
        color: white;
    }}
    h1, h2, h3 {{
        color: {cor_secundaria};
    }}
    </style>
    """, unsafe_allow_html=True)

# Título e introdução
st.image("logo_life_mama.png", width=200)  # Substitua pelo caminho correto do logo
st.title("Pesquisa Life Mama")
st.write("""
Olá!
Estamos em desenvolvimento de uma solução digital voltada à rotina materna.

Ao participar você estará contribuindo voluntariamente com seus dados, que não serão divulgados.

Para tirar dúvidas, entre em contato com 
Valéria Rezende, Chief Marketing Officer CMO, pelo telefone: 11 98144 7031
""")

# Função para salvar respostas
def salvar_respostas(respostas):
    df = pd.DataFrame([respostas])
    df['timestamp'] = datetime.now()
    df.to_csv('respostas_pesquisa.csv', mode='a', header=False, index=False)

# Formulário
with st.form("pesquisa_form"):
    q1 = st.radio("1. Você estaria disposta a pagar por um aplicativo que ajuda a organizar sua rotina e a cuidar do seu bem-estar?", 
                  ["Sim", "Não"])

    q2 = st.selectbox("2. Se sim, qual faixa de valor você considera justa para pagar mensalmente por um app que apoie sua organização e autocuidado?",
                      ["Não estaria disposta a pagar", "Menos de R$10 / mês", "R$10 a R$20 / mês", "R$20 a R$30 / mês", "Mais de R$30 / mês"])

    q3 = st.multiselect("3. Quais recursos ou funcionalidades no aplicativo fariam com que você considerasse o pagamento da assinatura?",
                        ["Lembretes de rotina", "Dicas de autocuidado", "Monitoramento de saúde"])
    q3_outro = st.text_input("Outro recurso:")

    q4 = st.multiselect("4. Selecione os itens que você possui na sua casa atualmente:",
                        ["Carro próprio", "TV a cabo ou streaming", "Computador ou notebook", "Internet banda larga", 
                         "Geladeira duplex", "Ar-condicionado", "Nenhum destes"])
    q4_outro = st.text_input("Outro item:")

    q5 = st.text_area("5. Atualmente, onde você busca soluções para organizar sua rotina ou cuidar de seu bem-estar e saúde mental?")

    q6 = st.text_area("6. Quais são os maiores desafios ou limitações que você encontra nas soluções que usa hoje?")

    q7 = st.multiselect("7. O que faz você baixar um aplicativo novo?",
                        ["Recomendação de amigos ou conhecidos", "Avaliações positivas na loja de apps", 
                         "Funcionalidades úteis para meu dia a dia", "Facilidade de uso"])
    q7_outro = st.text_input("Outro motivo para baixar:")

    q8 = st.multiselect("8. O que faz você manter um aplicativo no celular após baixá-lo?",
                        ["Uso frequente", "Atualizações e melhorias constantes", "Ajuda na organização e ganho de tempo", 
                         "Oferece benefícios ou recompensas"])
    q8_outro = st.text_input("Outro motivo para manter:")

    q9 = st.radio("9. Você já utilizou algum aplicativo especificamente voltado para mães?", ["Sim", "Não"])

    q10 = st.text_input("10. Se sim, qual aplicativo?")

    q11 = st.text_input("11. Se você toparia dar continuidade neste papo, deixe seu WhatsApp e email para participar de uma entrevista em profundidade.")

    submitted = st.form_submit_button("Enviar Respostas")

    if submitted:
        respostas = {
            "q1": q1,
            "q2": q2,
            "q3": ", ".join(q3) + (f", {q3_outro}" if q3_outro else ""),
            "q4": ", ".join(q4) + (f", {q4_outro}" if q4_outro else ""),
            "q5": q5,
            "q6": q6,
            "q7": ", ".join(q7) + (f", {q7_outro}" if q7_outro else ""),
            "q8": ", ".join(q8) + (f", {q8_outro}" if q8_outro else ""),
            "q9": q9,
            "q10": q10,
            "q11": q11
        }
        salvar_respostas(respostas)
        st.success("Obrigado por participar da nossa pesquisa!")

# Rodapé
st.markdown("---")
st.write("© 2024 Life Mama. Todos os direitos reservados.")