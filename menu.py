import streamlit as st

def menu():
    st.sidebar.title('Calculadoras')
    st.sidebar.markdown('Selecione a calculadora desejada:')
    st.sidebar.markdown('---')
    st.sidebar.page_link("app.py", label="Página inicial")
    st.sidebar.page_link("pages/notas.py", label="Calculadora de notas")
    st.sidebar.page_link("pages/faltas.py", label="Calculadora de presença")
    st.sidebar.page_link("pages/ferias.py", label="Contador das férias")
    st.sidebar.page_link("pages/sobre.py", label="Sobre")