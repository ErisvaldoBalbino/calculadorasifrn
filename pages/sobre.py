import streamlit as st
from menu import menu

menu()

st.title('Sobre')
st.write('---')
st.subheader('Calculadora de notas')
st.text('Média necessária para aprovação: 60')
st.text('Fórmula para a obter a média: (2 * N1 + 3 * N2) / 5')
st.text('Fórmula para a obter a média apenas com a primeira nota: (5 * 60 - 2 * N1) / 3')
st.text('Fórmulas para obter a média com a prova final: \n(MD + NAF) / 2\n(2 * NAF + 3 * N2) / 5\n(2 * N1 + 3 * NAF) / 5')
st.text('^ Será usada a fórmula que resultar na maior média.')
st.write('---')
st.subheader('Calculadora de presença')
st.text('Fórmula: ((aulas - faltas) / aulas) * 100')
st.text('Fórmula para saber quantidade max de faltas: \ntotalaulas - ((75 / 100) * totalaulas')
st.write('---')
st.subheader('Contador das férias')
st.text('O contador das férias é atualizado uma vez por dia.')
st.text('Data das férias esse semestre: 21/09/2024')
