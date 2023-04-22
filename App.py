import streamlit as st
import pandas as pd
import streamlit_

from PIL import Image

st.title('Professional Fighters League Stats')
st.text('    This web application displays PFL Statistics of fighters'
        '')
image = Image.open('/Users/m.l.brown80886/Downloads/PFL_Logo.jpg')
st.image(image,
         caption='PFL',
         use_column_width=True)


df_stats = pd.read_csv('/Users/m.l.brown80886/Downloads/PFL - PFL.csv')
df_stats



st.header('Fastest Punch Speed')
df_stats[['Name','Country', 'Class', 'Max Punch Speed(MPS)' ]]
st.header('Most Losses')
df_stats[['Name', 'Country', 'Class', 'Losses' ]]
st.header('Most Punches Completed')
df_stats[['Name', 'Country', 'Class', 'Total Strikes' ]]
st.header('Most Arm Strikes Completed')
df_stats[['Name', 'Country', 'Class', 'Arm Strikes' ]]
st.header('Most Leg Strikes Completed')
df_stats[['Name', 'Country', 'Class', 'Leg strikes' ]]
st.header('Most Takedowns Completed')
df_stats[['Name', 'Country', 'Class', 'Takedowns' ]]



st.header('Featherweight statistics')
st.text(' Featherweight charts for Max punch speed, arm strikes, leg strikes and takedowns '
        '')

image = Image.open('/Users/m.l.brown80886/Downloads/MPS(FW).jpg')
st.image(image,
         caption='PFL',
         use_column_width=True)


image = Image.open('/Users/m.l.brown80886/Downloads/Canva/ArmStrikes(FW).jpg')
st.image(image,
         caption='PFL',
         use_column_width=True)

image = Image.open('/Users/m.l.brown80886/Downloads/Canva/LegStrikes(FW).jpg')
st.image(image,
         caption='PFL',
         use_column_width=True)

image = Image.open('/Users/m.l.brown80886/Downloads/Canva/Takedowns(FW).jpg')
st.image(image,
         caption='PFL',
         use_column_width=True)


st.header('Heavyweight statistics')
st.text(' Heavyweight charts for Max punch speed, arm strikes, leg strikes and takedowns '
        '')
image = Image.open('/Users/m.l.brown80886/Downloads/Canva/MaxPunchSpeed(HW).jpg')
st.image(image,
         caption='PFL',
         use_column_width=True)


image = Image.open('/Users/m.l.brown80886/Downloads/Canva/ArmStrikes(HW).jpg')
st.image(image,
         caption='PFL',
         use_column_width=True)


image = Image.open('/Users/m.l.brown80886/Downloads/Canva/LegStrikes.jpg')
st.image(image,
         caption='PFL',
         use_column_width=True)


image = Image.open('/Users/m.l.brown80886/Downloads/Canva/Takedowns(HW).jpg')
st.image(image,
         caption='PFL',
         use_column_width=True)


st.header('Light Heavyweight statistics')
st.text(' Light Heavyweight charts for Max punch speed, arm strikes, leg strikes and takedowns '
        '')
image = Image.open('/Users/m.l.brown80886/Downloads/Canva/MPS(LHW).jpg')
st.image(image,
         caption='PFL',
         use_column_width=True)


image = Image.open('/Users/m.l.brown80886/Downloads/Canva/ArmStrikes(LHW).jpg')
st.image(image,
         caption='PFL',
         use_column_width=True)


image = Image.open('/Users/m.l.brown80886/Downloads/Canva/LegStrikes(LHW).jpg')
st.image(image,
         caption='PFL',
         use_column_width=True)


image = Image.open('/Users/m.l.brown80886/Downloads/Canva/Takedowns(LHW).jpg')
st.image(image,
         caption='PFL',
         use_column_width=True)


st.header('Lightweight statistics')
st.text(' Lightweight charts for Max punch speed, arm strikes, leg strikes and takedowns '
        '')
image = Image.open('/Users/m.l.brown80886/Downloads/Canva/MPS(LW).jpg')
st.image(image,
         caption='PFL',
         use_column_width=True)


image = Image.open('/Users/m.l.brown80886/Downloads/Canva/ArmStrikes(LW).jpg')
st.image(image,
         caption='PFL',
         use_column_width=True)


image = Image.open('/Users/m.l.brown80886/Downloads/Canva/LegStrikes(LW).jpg')
st.image(image,
         caption='PFL',
         use_column_width=True)


image = Image.open('/Users/m.l.brown80886/Downloads/Canva/Takedowns(LW).jpg')
st.image(image,
         caption='PFL',
         use_column_width=True)


st.header('Welterweight statistics')
st.text(' Welterweight charts for Max punch speed, arm strikes, leg strikes and takedowns '
        '')
image = Image.open('/Users/m.l.brown80886/Downloads/Canva/MPS(WW).jpg')
st.image(image,
         caption='PFL',
         use_column_width=True)


image = Image.open('/Users/m.l.brown80886/Downloads/Canva/ArmStrikes(WW).jpg')
st.image(image,
         caption='PFL',
         use_column_width=True)


image = Image.open('/Users/m.l.brown80886/Downloads/Canva/LegStrikes(WW).jpg')
st.image(image,
         caption='PFL',
         use_column_width=True)


image = Image.open('/Users/m.l.brown80886/Downloads/Canva/Takedowns(WW).jpg')
st.image(image,
         caption='PFL',
         use_column_width=True)