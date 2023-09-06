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


# Primer cuadro con logo lottie para mostrar la presentacion de la primera parte: 

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl('https://lottie.host/637f0c3c-9a90-4e67-944f-9015b5d7b4b2/TkI5LindFy.json')
imagen_video= Image.open('/Users/esteban/Phyton/Proyecto_final/images/Work.png')


# Empezamos explicando y abriendo el primer container sobre la aplicación 

with st.container():
    st.write("---")
    
    left_column, right_column = st.columns(2)
    
    with left_column:
        st.title("Guía sobre municipios españoles." )
        st.write("""
        
        "Esta aplicación proporciona información sobre municipios españoles, incluyendo datos sobre calidad del aire, temperatura, tiempo de viaje a Madrid y número de conexiones del aeropuerto internacional más cercano.
 
        """
                )
        
        st.write("[Github >](https://github.com/esteban-bit)")
                     
    with right_column:
                 
        st_lottie(lottie_coding, height = 300, key ="coding")
        


# Se procede a la conexión a la base de datos
str_conn = 'mysql+pymysql://root:Marconi1991@localhost:3306/Teletrabajo'  
engine = create_engine(str_conn)

consulta_sql = 'SELECT * FROM Teletrabajo.ciudades'
df = pd.read_sql(consulta_sql, engine)


# Procedemos con la primera tabla de entrada, quiero que se seleccione del listado que tengo.
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

def get_colors(df):
    colors = {
        "Muy buena": "green",
        "Buena": "blue",
        "Razonablemente buena": "yellow",
        "Regular": "orange",
        "Desfavorable": "red",
        "Muy desfavorable": "purple",
    }
    return colors

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
    color_discrete_map=get_colors(df),
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

# Gráfico de la distancia a Madrid
fig_distancia_madrid = px.scatter(
    df,
    x="DistanciaaMadrid(km)",
    y="Municipio",
    color="Municipio",
    size="DistanciaaMadrid(km)",
)

# Gráfico de la distancia a Barcelona
fig_distancia_barcelona = px.scatter(
    df,
    x="DistanciaaBarcelona(km)",
    y="Municipio",
    color="Municipio",
    size="DistanciaaBarcelona(km)",
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
        # Combinar las columnas de tiempo en una sola columna
        df_melted = pd.melt(
            df,
            id_vars=["Municipio"],
            value_vars=[
                "TiempomediodeviajeaMadridencoche",
                "TiempomediodeviajeaMadridentrenoautobús",
                "TiempomediodeviajeaBarcelonaencoche",
                "TiempomediodeviajeaBarcelonaentrenoautobús",
            ],
            var_name="Tipo_Transporte",
            value_name="Tiempo_de_viaje",
        )

        fig_tiempo_viaje = px.bar(
            df_melted,
            x="Municipio",
            y="Tiempo_de_viaje",
            color="Tipo_Transporte",
            title="Tiempo de viaje a Madrid y Barcelona para {}".format(municipios[0]),
        )

        fig_tiempo_viaje.update_yaxes(type="category", autorange="reversed")

    else:
        st.warning("No se ha seleccionado ningún municipio")

# Mostrar los gráficos

st.subheader("Información sobre municipios españoles")

st.markdown(
    """
    Introduce los nombres de los municipios para ver información sobre los mismos.
    """
)

# Muestra los graficos según se haya filtrado previamente:

if municipios:
    st.write("**Calidad del aire**")
    st.plotly_chart(fig_calidad_aire)

    st.write("**Temperatura mínima y máxima media**")
    st.plotly_chart(fig_temperatura)

    st.write("**Distancia a Madrid**")
    st.plotly_chart(fig_distancia_madrid)

    st.write("**Distancia a Barcelona**")
    st.plotly_chart(fig_distancia_barcelona)

    st.write("**Aeropuerto más cercano**")
    st.plotly_chart(fig_aeropuerto)

    if len(municipios) > 0:
        st.plotly_chart(fig_tiempo_viaje)

else:
    st.warning("No has seleccionado ningún municipio")


        
css = """

p {
    color: #fff;
}
.css-1y4p8pa {
    max-width: 95%;
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
        top: -230px;
}

.css-1v0mbdj img {
    width: 190px;
}

span.st-ds {
    background-color: rgb(128 89 243);
}


span.st-ds {
    background-color: rgb(128 89 243)!important;
}

.st-d2 {
    border-left-color: rgb(128 89 243);
}

.st-d3 {
    border-right-color: rgb(128 89 243);
}
.st-d4 {
    border-top-color: rgb(128 89 243);
}
.st-d5 {
    border-bottom-color: rgb(128 89 243);
}

.st-i:hover {
    color:#ffffff ;
    
}


.css-1v0mbdj img {
    width: 190px;
}

.css-nahz7x a {
    color: rgb(128 89 243);
}

hr {
    margin: 20px 0;
}

.css-1cypcdb {

    width: 220px !important;
    min-width: 220px!important;
    max-width: 220px!important;
}

"""


imagen = "/Users/esteban/Phyton/Proyecto_final/images/Work.png"
st.image(imagen)

# Aplicar estilos CSS a través de la función st.markdown
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)  

st.sidebar.markdown(""" <img class="work-connect-custom" src="http://localhost:8501/media/a02dd0fdec9cb585f8f97023966e081bf905e601705ef6ee4dbe3edc.png"> """, unsafe_allow_html=True)





