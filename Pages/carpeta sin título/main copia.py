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

imagen_video= Image.open('/Users/esteban/Phyton/Proyecto_final/images/Work.png')
st.image(imagen_video)
# linkedin_html = '''
# <a href="https://www.linkedin.com/in/esteban-cardona-60163685/">
#    <img src="https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555" # alt="LinkedIn">
# </a>
# '''

# Renderizar enlace con logo en Streamlit
# st.markdown(linkedin_html, unsafe_allow_html=True)


# funcion para animacion

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl('https://lottie.host/29fd4acf-1345-4bd1-93ce-803c7b5f6a4b/ujDllOSwfx.json')
imagen_video= Image.open('/Users/esteban/Phyton/Proyecto_final/images/Work.png')

with st.container():
    st.subheader('¡Hola! Bienvenido a mi prototipo de WorkConnect: 📲')
    #st.title('WorkConnect')
    st.write("""
             WorkConnect: La libertad de trabajar a tu manera. 
             Tu aplicación móvil para unirte a una comunidad laboral en constante crecimiento. Encuentra oportunidades laborales, conecta con personas con ideas similares y expande tu red profesional.
             
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
"""

# Aplicar estilos CSS a través de la función st.markdown
st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

# Contenido con los estilos aplicados
st.markdown('<h1>Título con estilo</h1>', unsafe_allow_html=True)
st.markdown('<p>Este es un párrafo con estilo.</p>', unsafe_allow_html=True)

st.title('Work Connect')


st.header('WorkConnect: La libertad de trabajar a tu manera')


st.subheader('Existen varios metodos para el texto')


st.write('introducir texto')

st.write('# Si ponemos "#" es como un h1')
st.write('## Si ponemos "##" es como un h2')
st.write('### Si ponemos "###" es como un h3')


st.info('Esto ya casi esta')
st.error('Esta clase ya casi esta.')
st.success('Esta clase ya casi esta.')
st.warning('Esta clase ya casi esta.')


df=pd.read_csv('src/data/comunio_J6.csv')
st.caption('# Podemos cargar un dataframe y mostrarlo')


filtros, equipos, pos, goles = st.columns(4)


with filtros:
    columnas = df.columns
    selection = st.multiselect('Filtrar Columnas', columnas, default=['Team',
                                                                      'Player', 
                                                                      'Position', 
                                                                      'Matchs', 
                                                                      'Goals',
                                                                      'Total_Points'])


with equipos:
    equipo = st.selectbox('Filtrar Equipos', df.Team.unique())

with pos:
    player_pos = st.selectbox('Filtrar Posicion', df.Position.unique())



with goles:
    gol_min, gol_max = st.select_slider('Filtrar por Goles', 
                                        options=[i for i in range(0,df.Goals.max()+1)],
                                        value=[0, df.Goals.max()])



st.sidebar.header('Menu')
st.sidebar.subheader('WorkConnect')
st.sidebar.image(Image.open('/Users/esteban/Phyton/Proyecto_final/images/Work.png'))
st.sidebar.info('Aquí puedes poner una barra de navegación o zonas para cargar archivos')



uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
upload_image = st.sidebar.file_uploader('Upload an Image', type=['png', 'jpeg', 'jpg'])



if uploaded_file is not None:
    df1 = pd.read_csv(uploaded_file)

else:
    df1 = df[selection]

    var = df1[(df1.Team == equipo) &
              (df1.Goals >= gol_min) &
              (df1.Goals <= gol_max) &
              (df1.Position == player_pos)]

    st.dataframe(var)

    df_plot = df1[(df1.Team == equipo) &
        (df1.Goals >= gol_min) &
        (df1.Goals <= gol_max) &
        (df1.Position == player_pos)]
    
    fig, ax = plt.subplots()
    plt.title(f'Puntos Totales del {equipo} por Jugador - Posición {player_pos}')
    ax.barh(y=df_plot.Player, width=df_plot.Total_Points)

    st.caption('## También podemos mostrar gráficos')
    st.pyplot(fig)


    
st.caption('## Imágenes')
if upload_image is not None:
    st.image(upload_image)
else:
    st.image(Image.open('src/images/ih.png'))



url = 'https://www.ironhack.com'
st.caption('## Podemos incluir un boton de redireccion')

if st.button('WEB IRON'):
    webbrowser.open_new_tab(url)

df_plot = df1[(df1.Team == equipo) &
        (df1.Goals >= gol_min) &
        (df1.Goals <= gol_max) &
        (df1.Position == player_pos)]
    
fig, ax = plt.subplots()
plt.title(f'Puntos Totales del {equipo} por Jugador - Posición {player_pos}')
ax.barh(y=df_plot.Player, width=df_plot.Total_Points)

img=io.BytesIO()
plt.savefig(img, format='png')
img.seek(0)
plot_url=base64.b64encode(img.getvalue()).decode()

html = f"<a href='{url}'><img src='data:image/png;base64,{plot_url}'></a>"
st.markdown(html, unsafe_allow_html=True)


st.video('https://www.youtube.com/watch?v=zS5pjxseTQM&list=RDzS5pjxseTQM&start_radio=1&ab_channel=JoanAsPoliceWoman')


import folium

from streamlit_folium import st_folium

# center on Liberty Bell, add marker
m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
folium.Marker(
    [39.949610, -75.150282], popup="Liberty Bell", tooltip="Liberty Bell"
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)
    


