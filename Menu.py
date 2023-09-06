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



# linkedin_html = '''
# <a href="https://www.linkedin.com/in/esteban-cardona-60163685/">
#    <img src="https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555" # alt="LinkedIn">
# </a>
# '''

# Renderizar enlace con logo en Streamlit
# st.markdown(linkedin_html, unsafe_allow_html=True)



# funcion para animacion con lottie 

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl('https://lottie.host/29fd4acf-1345-4bd1-93ce-803c7b5f6a4b/ujDllOSwfx.json')
imagen_video= Image.open('/Users/esteban/Phyton/Proyecto_final/images/Work.png')

# Empezamos explicando y abriendo el primer container sobre la aplicación 

with st.container():
    st.title('¡Hola! Bienvenido a mi prototipo de WorkConnect: 📲')
    #st.title('WorkConnect')
    st.write("""
             WorkConnect: La libertad de trabajar a tu manera. 
             Tu aplicación móvil para unirte a una comunidad laboral en constante crecimiento.
             Encuentra oportunidades laborales, conecta con personas con ideas similares y expande tu red profesional.
             
            """)
    st.write("[Mas información >](https://github.com/esteban-bit)")

with st.container():
    st.write("---")
    
    left_column, right_column = st.columns(2)
    
    with left_column:
        st.subheader("WorkConnect es una empresa emergente que busca cambiar la forma de conectar a las personas." )
        st.write("""
        
        "Tu aplicación móvil para unirte a una comunidad laboral en constante crecimiento. Encuentra oportunidades laborales, conecta con personas con ideas similares y expande tu red profesional.   
        """
                )
        
        st.write("[Github >](https://github.com/esteban-bit)")
                     
    with right_column:
                 
        st_lottie(lottie_coding, height = 300, key ="coding")
                 
                

with st.container():
    st.write("---")
    st.header("WorkConnect")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(imagen_video)
    with text_column:
        st.write( """
        En este video, te mostraré el prototipo de funciones de la aplicación Workconect.
        
        """
            )
        st.markdown("[Ver video... ](https://www.youtube.com/watch?v=zeS2FlxF_0s)")


                 
                 
# Para mejorar el estilo, modifico algunas cosas del css de la pagina :                  
                 
                
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
       top: -230px;
       left: 0;
       width: 190px;
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


st.sidebar.markdown(""" <img class="work-connect-custom" src="http://localhost:8501/media/269d7b43cfaa846409b0ac9c6513fb40aaf87116f3f3c29392aef7b6.png"> """, unsafe_allow_html=True)

# Aplicar estilos CSS a través de la función st.markdown
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)





    


