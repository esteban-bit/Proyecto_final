import streamlit as st
import requests
import pandas as pd
import numpy as np
from PIL import Image
import pylab as plt
import webbrowser
import base64
import io
import sqlalchemy
from sqlalchemy import create_engine
from streamlit_lottie import st_lottie
import folium
import streamlit_folium
from streamlit_folium import folium_static

imagen = "/Users/esteban/Phyton/Proyecto_final/images/Work.png"
st.image(imagen)

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

lottie_coding = load_lottieurl('https://lottie.host/c9d477b9-23b2-4f12-9fcb-c632d1631113/m78ovw9rzi.json')
imagen_video= Image.open('/Users/esteban/Phyton/Proyecto_final/images/Work.png')

with st.container():
    st.write("---")
    
    left_column, right_column = st.columns(2)
    
    with left_column:
        st.subheader("Guía para encontrar la vivienda ideal al mejor precio." )
        st.write("""
        
        "Encuentra el alquiler más barato por metro cuadrado y explora opciones de compra para encontrar la vivienda ideal que se ajuste a tus necesidades y presupuest. 
        """
                )
        
        st.write("[Github >](https://github.com/esteban-bit)")
                     
    with right_column:
                 
        st_lottie(lottie_coding, height = 300, key ="coding")
        
provincias_lat_lon = {
    "España": (40.4168, -3.7038),
    "A Coruña": (43.3623, -8.4115),
    "A Coruña provincia": (43.3623, -8.4115),
    "Andalucía": (36.7213, -4.4214),
    "Álava": (42.8467, -2.7022),
    "Albacete": (39.0000, -1.8677),
    "Albacete provincia": (39.0000, -1.8677),
    "Alicante / Alacant": (38.3452, -0.4810),
    "Alicante/Alacant": (38.3452, -0.4810),
    "Almería": (36.8402, -2.4679),
    "Almería provincia": (36.8402, -2.4679),
    "Aragón": (41.6561, -0.8773),
    "Asturias": (43.3614, -5.8593),
    "Ávila": (40.6562, -4.7000),
    "Ávila provincia": (40.6562, -4.7000),
    "Badajoz": (38.8794, -6.9706),
    "Badajoz provincia": (38.8794, -6.9706),
    "Barcelona": (41.3851, 2.1734),
    "Barcelona provincia": (41.3851, 2.1734),
    "Bilbao": (43.2630, -2.9340),
    "Burgos": (42.3439, -3.6969),
    "Burgos provincia": (42.3439, -3.6969),
    "Cáceres": (39.4766, -6.3722),
    "Cáceres provincia": (39.4766, -6.3722),
    "Cádiz": (36.5299, -6.2924),
    "Cádiz provincia": (36.5299, -6.2924),
    "Canarias": (28.2916, -16.6291),
    "Cantabria": (43.1828, -3.9878),
    "Castellón": (39.9864, -0.0513),
    "Castilla y León": (41.6827, -4.1570),
    "Castilla-La Mancha": (39.2796, -3.0977),
    "Castellón de la Plana / Castello de la Plana": (39.9864, -0.0513),
    "Castellón/Castelló": (39.9864, -0.0513),
    "Cataluña": (41.5912, 1.5209),
    "Ceuta": (35.8893, -5.3198),
    "Ceuta provincia": (35.8893, -5.3198),
    "Ciudad Real": (38.9866, -3.9292),
    "Ciudad Real provincia": (38.9866, -3.9292),
    "Comunitat Valenciana": (39.4699, -0.3763),
    "Córdoba": (37.8882, -4.7794),
    "Córdoba provincia": (37.8882, -4.7794),
    "Cuenca": (40.0696, -2.1348),
    "Cuenca provincia": (40.0696, -2.1348),
    "Donostia-San Sebastián": (43.3183, -1.9812),
    "Extremadura": (39.4919, -6.3663),
    "Euskadi": (43.2630, -2.9340),
    "Galicia": (42.5751, -8.1339),
    "Girona": (41.9793, 2.8191),
    "Girona provincia": (41.9793, 2.8191),
    "Granada": (37.1773, -3.5986),
    "Granada provincia": (37.1773, -3.5986),
    "Guadalajara": (40.6318, -3.1661),
    "Guadalajara provincia": (40.6318, -3.1661),
    "Guipúzcoa": (43.3208, -1.9829),
    "Huelva": (37.2576, -6.9499),
    "Huelva provincia": (37.2576, -6.9499),
    "Huesca": (42.1347, -0.4125),
    "Huesca provincia": (42.1347, -0.4125),
    "Baleares": (39.5734, 2.6502),
    "Jaén": (37.7793, -3.7841),
    "Jaén provincia": (37.7793, -3.7841),
    "La Coruña": (43.3713, -8.3960),
    "La Rioja": (42.2871, -2.5396),
    "Las Palmas": (28.1248, -15.4300),
    "Las Palmas de Gran Canaria": (27.9202, -15.5474),                      
    "León": (42.5987, -5.5671),
    "León provincia": (42.5987, -5.5671),
    "Lleida": (41.6148, 0.6250),
    "Lleida provincia": (41.6148, 0.6250),
    "Logroño": (42.4624, -2.4447),
    "Lugo": (43.0121, -7.5560),
    "Lugo provincia": (43.0121, -7.5560),
    "Madrid": (40.4168, -3.7038),
    "Madrid provincia": (40.4168, -3.7038),
    "Madrid Comunidad": (40.4168, -3.7038),
    "Málaga": (36.7213, -4.4214),
    "Málaga provincia": (36.7213, -4.4214),
    "Melilla": (35.2922, -2.9381),
    "Melilla provincia": (35.2922, -2.9381),
    "Murcia": (37.9838, -1.1283),
    "Murcia provincia": (37.9838, -1.1283),
    "Murcia región": (37.9922, -1.1307),
    "Navarra": (42.6954, -1.6761),
    "Ourense": (42.3409, -7.8648),
    "Ourense provincia": (42.3409, -7.8648),
    "Oviedo": (43.3614, -5.8494),
    "Palencia": (42.0096, -4.5277),
    "Palma de Mallorca": (39.5696, 2.6502),
    "Pamplona/Iruña": (42.8125, -1.6458),
    "Pontevedra": (42.4328, -8.6490),
    "Pontevedra provincia": (42.4328, -8.6490),
    "Salamanca": (40.9688, -5.6631),
    "Salamanca provincia": (40.9688, -5.6631),
    "Santa Cruz de Tenerife": (28.4636, -16.2518),
    "Santander":(  43.4623, -3.8103),                  
    "Segovia": (40.9429, -4.1088),
    "Segovia provincia": (40.9429, -4.1088),
    "Sevilla": (37.3891, -5.9845),
    "Sevilla provincia": (37.3891, -5.9845),
    "Soria": (41.7631, -2.4649),
    "Soria provincia": (41.7631, -2.4649),
    "Tarragona": (41.1189, 1.2445),
    "Tarragona provincia": (41.1189, 1.2445),
    "Teruel": (40.3459, -1.1063),
    "Teruel provincia": (40.3459, -1.1063),                      
    "Toledo": (39.8561, -4.0247),
    "Toledo provincia": (39.8561, -4.0247),
    "València": (39.4699, -0.3763),
    "Valencia/Valéncia": (39.4699, -0.3763),
    "Valladolid": (41.6521, -4.7284),
    "Valladolid provincia": (41.6521, -4.7284),
    "Vitoria-Gasteiz": (42.8467, -2.6726),
    "Vizcaya": (43.2630, -2.9340),
    "Zamora": (41.5034, -5.7442),
    "Zamora provincia": (41.5034, -5.7442),
    "Zaragoza": (41.6488, -0.8891),
    "Zaragoza provincia": (41.6488, -0.8891),                      
    "Ceuta": (35.8884, -5.3050),
    "Melilla": (35.2923, -2.9381)
}  



# Conexión a la base de datos
str_conn = 'mysql+pymysql://root:Marconi1991@localhost:3306/Teletrabajo'  # Asegúrate de configurar correctamente la conexión
engine = create_engine(str_conn)

# Lectura de los datos
consulta_sql_alquileres = 'SELECT * FROM Teletrabajo.alquiler'
df_alquileres = pd.read_sql(consulta_sql_alquileres, engine)

consulta_sql_ventas = 'SELECT * FROM Teletrabajo.ventas'
df_ventas = pd.read_sql(consulta_sql_ventas, engine)

# Funciones para filtrar los datos
def filtrar_alquileres(df, provincia):
    """
    Esta función filtra los alquileres por provincia.

    Args:
        df: El DataFrame original.
        provincia: La provincia a filtrar.

    Returns:
        El DataFrame filtrado.
    """
    return df.loc[df['Localización'] == provincia]


def filtrar_ventas(df, provincia):
    """
    Esta función filtra las ventas por provincia.

    Args:
        df: El DataFrame original.
        provincia: La provincia a filtrar.

    Returns:
        El DataFrame filtrado.
    """
    return df.loc[df['Localización'] == provincia]


def mapa_alquileres(df_filtered):
    """
    Esta función muestra un mapa con los alquileres por m2.

    Args:
        df_filtered: El DataFrame filtrado.
    """
    # Crear un mapa de Folium
    mapa = folium.Map(location=[40.4168, -3.7038], zoom_start=6, title="Alquileres por m2 en España")

    # Añadir marcadores al mapa
    for index, row in df_filtered.iterrows():
        provincia = row['Localización']
        precio = row['Precio m2 jul']
        if provincia in provincias_lat_lon:
            lat, lon = provincias_lat_lon[provincia]
            folium.Marker(location=[lat, lon], icon=folium.Icon(color=get_color(precio)),
                          popup=f"Precio: {precio} €/m2").add_to(mapa)

    # Renderizar el mapa en Streamlit
    folium_static(mapa)

# En lugar de utilizar st.pyplot(plt), utilizamos:
def folium_static(mapa):
    """
    Esta función renderiza el mapa de Folium en Streamlit.

    Args:
        mapa: El mapa creado con Folium.
    """
    from streamlit_folium import folium_static
    import streamlit.components.v1 as components

    folium_static(mapa)
    components.html("<style>#map_0{height:40rem;}</style>")
    
def get_color(precio):
    if precio < 1000:
        return 'blue'
    elif precio >= 1000 and precio < 2000:
        return 'green'
    else:
        return 'red'


# Llama a la función mapa_alquileres para mostrar el mapa
mapa_alquileres(df_alquileres)




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
        top: -250px;
}

.css-1v0mbdj img {
    width: 190px;
}

"""

# Aplicar estilos CSS a través de la función st.markdown
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)  

st.sidebar.markdown(""" <img class="work-connect-custom" src="http://localhost:8501/media/cc756b324e15fab25f009aa9e96f51cfdb55e3025029dfce3c2549ea.png"> """, unsafe_allow_html=True)
