import streamlit as st
from menu import menu

menu()

if 'media' not in st.session_state:
    st.session_state.media = 0

def media():
    if 0 <= st.session_state.nota1 <= 100 and 0 <= st.session_state.nota2 <= 100:
        resultado = (2 * st.session_state.nota1 + 3 * st.session_state.nota2) / 5
        st.session_state.media = resultado
    else:
        st.error("As notas devem estar entre 0 e 100.")
        st.session_state.media = 0

def nota2_aprovacao():
    resultado = (5 * 60 - 2 * st.session_state.nota1) / 3
    st.session_state.nota2_aprovacao = resultado

### Media final

def mf_1():
    return (st.session_state.media + st.session_state.notafinal) / 2

def mf_2():
    return (2 * st.session_state.notafinal + 3 * st.session_state.nota2) / 5

def mf_3():
    return (2 * st.session_state.nota1 + 3 * st.session_state.notafinal) / 5

def escolher_melhor_formula():
    opcao1 = mf_1()  # Média aritmética entre média parcial e nota final
    opcao2 = mf_2()  # Média ponderada entre nota final (peso 2) e N2 (peso 3)
    opcao3 = mf_3()  # Média ponderada entre N1 (peso 2) e nota final (peso 3)

    melhores_resultados = {'1': opcao1, '2': opcao2, '3': opcao3}
    melhor_opcao = max(melhores_resultados, key=melhores_resultados.get)
    
    return melhor_opcao, melhores_resultados[melhor_opcao]

st.title('Calcular média:')
row1_1, row1_2 = st.columns([1, 1])

row1_1.number_input('N1', value=0, max_value=100, key = 'nota1')
row1_2.number_input('N2', value=0, max_value=100, key = 'nota2')
st.button('Calcular média', on_click=media, type='primary', use_container_width=True, )


if st.session_state.media:
    st.info(f'**{st.session_state.media:.0f}** é a sua média atual.')
    if st.session_state.media < 60:
        nota2_aprovacao()
        st.error(f'Para ser aprovado, você precisaria tirar **{st.session_state.nota2_aprovacao:.0f}** na segunda nota ou fazer a **prova final**.')
        st.write('---')
        st.title('Calcular nota final')
        st.number_input('Nota da prova final', value=0, max_value=100, key = 'notafinal')
        if st.button('Calcular', type='primary', use_container_width=True):
            melhor_opcao, melhor_resultado = escolher_melhor_formula()
            st.info(f'Sua média final é: **{melhor_resultado:.0f}** usando a fórmula **{melhor_opcao}**.')