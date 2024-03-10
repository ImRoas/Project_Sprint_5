import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

# car_data['model_year'] = car_data['model_year'].fillna(value='')
# car_data['model_year'] = car_data['model_year'].replace('', 0)
# car_data['model_year'] = car_data['model_year'].astype('int')

st.header('Gráficos de autos')
st.write('Tabla de datos')  
st.write(car_data)

hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón

    # escribir un mensaje
    st.subheader('_Condiciones de los autos_')
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')   

    # crear un histograma
    fig = px.histogram(
        car_data, 
        x="model_year",
        color='condition'
    )

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# crear una casilla de verificación
build_histogram = st.checkbox('Construir un histograma')

if build_histogram: # si la casilla de verificación está seleccionada
    st.write('Construir un histograma para los modelos de auto')

    # crear un gráfico de dispersión
    fig = px.bar( 
        car_data, 
        x="model", 
        y="model_year",
        color='type'
    )

    # crear gráfico de dispersión
    fig.show()  
    st.plotly_chart(fig, use_container_width=True)

    # st.line_chart(car_data, x='odometer', y='price')
