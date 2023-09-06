import streamlit as st
import requests
import pandas as pd
from PIL import Image
import pylab as plt
import webbrowser
import base64
import io
import sqlalchemy
from sqlalchemy import create_engine
from streamlit_lottie import st_lottie
import streamlit_folium
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px



#linkedin_html = '''
#<a href="https://www.linkedin.com/in/esteban-cardona-60163685/">
#    <img src="https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555" alt="LinkedIn">
#</a>
#'''

# Renderizar enlace con logo en Streamlit
#st.markdown(linkedin_html, unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl('https://lottie.host/1b1fb30e-c7cb-46d7-a867-7b473bbdcd31/G5yPgKev94.json')
imagen_video= Image.open('/Users/esteban/Phyton/Proyecto_final/images/Work.png')

with st.container():
    st.write("---")
    
    left_column, right_column = st.columns(2)
    
    with left_column:
        st.subheader("Guía sobre municipios españoles." )
        st.write("""
        
        "Esta aplicación proporciona información sobre municipios españoles, incluyendo datos sobre calidad del aire, temperatura, tiempo de viaje a Madrid y número de conexiones del aeropuerto internacional más cercano.
 
        """
                )
        
        st.write("[Github >](https://github.com/esteban-bit)")
                     
    with right_column:
                 
        st_lottie(lottie_coding, height = 300, key ="coding")
        


# Establecer la conexión a la base de datos
str_conn = 'mysql+pymysql://root:Marconi1991@localhost:3306/Teletrabajo'  # Asegúrate de configurar correctamente la conexión
engine = create_engine(str_conn)

# Consultar la base de datos
consulta_sql = 'SELECT * FROM Teletrabajo.ciudades'
df = pd.read_sql(consulta_sql, engine)





# Crear los widgets de entrada
municipios = st.multiselect(
    "Introduce los nombres de los municipios:", df["Municipio"].tolist()
)

# Filtrar los datos
if municipios:
    df = df[df["Municipio"].isin(municipios)]

# Convertir la columna TiempomediodeviajeaMadridencoche a datetime64[ns]
df["TiempomediodeviajeaMadridencoche"] = pd.to_datetime(
    df["TiempomediodeviajeaMadridencoche"], format="%H:%M:%S"
)

# Crear los gráficos

# Gráfico de la calidad del aire
df["Municipio"] = df["Municipio"].astype(str)
fig_calidad_aire = px.bar(
    df.pivot_table(
        index="Municipio",
        values=[
            "%díascalidaddelaireBuena",
            "%díascalidaddelaireRazonablementeBuena",
            "%díascalidaddelaireRegular",
            "%díascalidaddelaireDesfavorable",
            "%díascalidaddelaireMuyDesfavorable",
            "%díascalidaddelaireExtremadamenteDesfavorable",
        ],
        aggfunc="mean",
    ),
    title="Calidad del aire en los municipios españoles",
)

# Gráfico de la temperatura mínima y máxima media
fig_temperatura = px.bar(
    df,
    x="Municipio",
    y=["Temperaturamínimamedia(ºC)", "Temperaturamáximamedia(ºC)"],
    title="Temperatura mínima y máxima medias en los municipios españoles",
    barmode="stack",
)

# Gráfico de la distancia a Madrid y Barcelona
fig_distancia = px.scatter(
    df,
    x="DistanciaaMadrid(km)",
    y="DistanciaaBarcelona(km)",
    color="Municipio",
    title="Distancia a Madrid y Barcelona",
)

# Gráfico del aeropuerto más cercano
fig_aeropuerto = px.bar(
    df,
    x="AeropuertoInternacionalmáscercano",
    y="Númerodeconexionesdelaeropuertointernacionalmáscercano",
    title="Aeropuerto más cercano",
)

# Gráfico del tiempo de viaje
if municipios:
    if len(municipios) > 0:
        fig_tiempo_viaje = px.line(
            df,
            x="Municipio",
            y=["TiempomediodeviajeaMadridencoche"],
            title="Tiempo de viaje a Madrid para {} ".format(municipios[0]),
        )
    else:
        st.warning("No se ha seleccionado ningún municipio")

# Mostrar los gráficos

st.title("Información sobre municipios españoles")

st.markdown(
    """
    Introduce los nombres de los municipios para ver información sobre los mismos.
    """
)

if municipios:
    st.write("**Calidad del aire**")
    st.plotly_chart(fig_calidad_aire)

    st.write("**Temperatura mínima y máxima media**")
    st.plotly_chart(fig_temperatura)

    st.write("**Distancia a Madrid y Barcelona**")
    st.plotly_chart(fig_distancia)

    st.write("**Aeropuerto más cercano**")
    st.plotly_chart(fig_aeropuerto)

    if len(municipios) > 0:
        st.plotly_chart(fig_tiempo_viaje)

else:
    st.warning("No has seleccionado ningún municipio")


        
css = """
h1 {
    color: red;
    font-size: 24px;
}
p {
    color: #fff;
}
.css-1y4p8pa {
    max-width: 100%;
    padding-top: 55px;
}
.css-1kyxreq {
    justify-content: center;
    margin-bottom: 15px;
}
.css-1kyxreq img {
    width: 330px;
}

.css-6qob1r {
        position: relative;
}

.work-connect-custom {
        position: absolute;
        left: 0;
        width: 190px;
        top: -300px;
}

.css-1v0mbdj img {
    width: 190px;
}

"""
imagen = "/Users/esteban/Phyton/Proyecto_final/images/Work.png"
st.image(imagen)

# Aplicar estilos CSS a través de la función st.markdown
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)  

st.sidebar.markdown(""" <img class="work-connect-custom" src="http://localhost:8501/media/cc756b324e15fab25f009aa9e96f51cfdb55e3025029dfce3c2549ea.png"> """, unsafe_allow_html=True)