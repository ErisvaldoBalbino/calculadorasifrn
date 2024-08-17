import streamlit as st
from menu import menu

menu()

st.title('Calcular presença:')

if 'faltas' not in st.session_state:
    st.session_state.faltas = 0

if 'aulas' not in st.session_state:
    st.session_state.aulas = 0

if 'porcentagem' not in st.session_state:
    st.session_state.porcentagem = 0

def calcula_presenca():
    try:
        resultado = ((st.session_state.aulas - st.session_state.faltas) / st.session_state.aulas) * 100
        st.session_state.porcentagem = resultado
    except ZeroDivisionError:
        pass

row1_1, row1_2 = st.columns([1, 1])
row1_1.number_input('Aulas', value=0, min_value=0, max_value=2000, key='aulas')
row1_2.number_input('Faltas', value=0, min_value=0, max_value=2000, key='faltas')
st.button('Calcular porcentagem', on_click=calcula_presenca, type='primary', use_container_width=True)

if st.session_state.porcentagem is not None:
    if st.session_state.faltas > st.session_state.aulas:
        st.error('A quantidade de faltas não pode ser maior do que o total de aulas.')
    elif st.session_state.aulas == 0:
        st.warning('O número de aulas deve ser maior que zero.')
    elif st.session_state.faltas == st.session_state.aulas:
        st.error(f'Você tem **{st.session_state.porcentagem:.2f}%** de presença.')
    else:
        if st.session_state.porcentagem >= 75:
            st.success(f'Você tem **{st.session_state.porcentagem:.2f}%** de presença.')
        else:
            st.error(f'Você tem **{st.session_state.porcentagem:.2f}%** de presença.')

        faltasdisponiveis = st.session_state.aulas - ((75 / 100) * st.session_state.aulas)
        st.info(f'O máximo de faltas que você pode ter é **{faltasdisponiveis:.0f}**.')