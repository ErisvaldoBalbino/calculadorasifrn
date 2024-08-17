import streamlit as st
from menu import menu
from datetime import datetime
import pytz
import calendar

def countdown_timer(ferias):
    agora = datetime.now(pytz.timezone('America/Sao_Paulo'))
    tempo_faltando = ferias - agora

    if tempo_faltando.total_segundos() <= 0:
        return "As férias chegaram!"

    dias = tempo_faltando.days
    horas, resto = divmod(tempo_faltando.seconds, 3600)
    minutos, segundos = divmod(resto, 60)

    return f"{dias} dias, {horas:02d}:{minutos:02d}:{segundos:02d}"

st.title("Faltam")

# Permitir que o usuário escolha a data das férias
ferias = datetime(2024, 9, 21).date()

# Converter a data escolhida para datetime com horário
feriastime = datetime.combine(ferias, datetime.min.time())
feriastime = pytz.timezone('America/Sao_Paulo').localize(feriastime)

# Atualização automática a cada segundo
st.empty()
placeholder = st.empty()

dias_faltando = (feriastime - datetime.now(pytz.timezone('America/Sao_Paulo'))).days
placeholder.header(f"{dias_faltando} dias", anchor=False)


menu()