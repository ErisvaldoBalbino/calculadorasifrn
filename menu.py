import streamlit as st

def menu():
    st.sidebar.title('Ferramentas')
    st.sidebar.markdown('Selecione a ferramenta desejada:')
    st.sidebar.markdown('---')
    st.sidebar.page_link("app.py", label="Home")
    st.sidebar.page_link("pages/faltas.py", label="Calcular presença")
    st.sidebar.page_link("pages/ferias.py", label="Contador até as férias")
    st.sidebar.page_link("pages/notas.py", label="Calculadora de notas")
    st.sidebar.page_link("pages/sobre.py", label="Sobre")