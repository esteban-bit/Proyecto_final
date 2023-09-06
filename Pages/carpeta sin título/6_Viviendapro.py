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

#linkedin_html = '''
#<a href="https://www.linkedin.com/in/esteban-cardona-60163685/">
#    <img src="https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555" alt="LinkedIn">
#</a>

# Renderizar enlace con logo en Streamlit
#st.markdown(linkedin_html, unsafe_allow_html=True)

imagen = "/Users/esteban/Phyton/Proyecto_final/images/Work.png"
st.image(imagen) 


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl('https://lottie.host/def2fef1-7b55-4b5e-9f80-e17e87b763ab/cazK1a3rLp.json')
imagen_video= Image.open('/Users/esteban/Phyton/Proyecto_final/images/Work.png')

with st.container():
    st.write("---")
    
    left_column, right_column = st.columns(2)
    
    with left_column:
        st.subheader("Guía para encontrar la vivienda ideal al mejor precio." )
        st.write("""
        
        "Encuentra el alquiler más barato por metro cuadrado y explora opciones de compra para encontrar la vivienda ideal que se ajuste a tus necesidades y presupuesto. 
        """
                )
        
        st.write("[Github >](https://github.com/esteban-bit)")
                     
    with right_column:
                 
        st_lottie(lottie_coding, height = 300, key ="coding")
        
        




def main():
    str_conn = 'mysql+pymysql://root:Marconi1991@localhost:3306/Teletrabajo'
    engine = create_engine(str_conn)
    consulta_sql = 'SELECT * FROM Teletrabajo.alquiler'
    df = pd.read_sql(consulta_sql, engine)

    with st.container():
        st.write("---")
        st.header("Busca tu alquiler ideal")
        
        filtros, localizacion, precio = st.columns(3)
        
        with filtros:
            columnas = df.columns
            selection = st.multiselect('Filtrar Columnas Alquiler', columnas, default=['Localización', 'Precio m2 jul', 'Máximo histórico'])
        
#         with localizacion:
#             equipo = st.selectbox('Filtrar Localización', df.Localización.unique())
        
        with precio:
            options = np.linspace(df['Precio m2 jul'].min(), df['Precio m2 jul'].max(), num=100).tolist()

            prec_min, prec_max = st.select_slider('Filtrar por Precio m2',
                                                  options=options,
                                                  value=[df['Precio m2 jul'].min(), df['Precio m2 jul'].max()],
                                                  format_func=lambda x: round(x, 2))
        
        # Aplicar filtros solo si están seleccionados
        if selection:
            df = df[selection]
        
#         if equipo:
#             df = df[df['Localización'] == equipo]
        
        if prec_min != df['Precio m2 jul'].min() or prec_max != df['Precio m2 jul'].max():
            df = df[(df['Precio m2 jul'] >= prec_min) & (df['Precio m2 jul'] <= prec_max)]
        
        # Mostrar el DataFrame en Streamlit
        st.write(df)

if __name__ == '__main__':
    main()
    
# Compra de casa    
    
    
def main():
    str_conn = 'mysql+pymysql://root:Marconi1991@localhost:3306/Teletrabajo'
    engine = create_engine(str_conn)
    consulta_sql = 'SELECT * FROM Teletrabajo.ventas'
    df = pd.read_sql(consulta_sql, engine)

    with st.container():
        st.write("---")
        st.header("Si buscas comprar casa:")
        
        filtros, localizacion, precio = st.columns(3)
        
        with filtros:
            columnas = df.columns
            selection = st.multiselect('Filtrar Columnas', columnas, default=['Localización', 'Precio m2 jul', 'Máximo histórico'])
        
#         with localizacion:
#             equipo = st.selectbox('Filtrar Localización', df.Localización.unique())
        
        with precio:
            options = np.linspace(df['Precio m2 jul'].min(), df['Precio m2 jul'].max(), num=100).tolist()

            prec_min, prec_max = st.select_slider('Filtrar por Precio m2',
                                                  options=options,
                                                  value=[df['Precio m2 jul'].min(), df['Precio m2 jul'].max()],
                                                  format_func=lambda x: round(x, 2))
        
        # Aplicar filtros solo si están seleccionados
        if selection:
            df = df[selection]
        
#         if equipo:
#             df = df[df['Localización'] == equipo]
        
        if prec_min != df['Precio m2 jul'].min() or prec_max != df['Precio m2 jul'].max():
            df = df[(df['Precio m2 jul'] >= prec_min) & (df['Precio m2 jul'] <= prec_max)]
        
        # Mostrar el DataFrame en Streamlit
        st.write(df)

if __name__ == '__main__':
    main()
    
    
    
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