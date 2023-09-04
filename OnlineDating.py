import streamlit as st
import pandas as pd
import altair as alt

st.header("Online-Dating: Die Hälfte sucht nach langfristiger Partnerschaft")
st.subheader("Mit welchem Ziel nutzen Sie Online-Dating-Angebote?")

source = pd.DataFrame({
        'Anteil (%)': [54, 45, 33, 28],
        'Ziel': ['Um eine langfristige Beziehung zu finden', 'Um neue Menschen kennenzulernen', 'Für lockere Flirts und gelegentliche Dates', 'Zum Zeitvertreib']
})
bar_chart = alt.Chart(source).mark_bar().encode(
        y='Anteil (%):Q',
        x='Ziel:O',
    )
st.altair_chart(bar_chart, use_container_width=True)


txt = st.text_area('', '''
    Basis: n=528; ab 16 Jahren; Deutschland; Mehrfachnennung möglich
    ''')
st.text("Klicke an die Balken um die Daten genauer anzuschauen. Du kannst auch die Diagramm vergrößern und ein Bild davon machen")
st.text("Quelle: Bitkom Research 2023")