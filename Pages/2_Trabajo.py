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


# Link a mi linkedin: 

linkedin_html = '''
<a href="https://www.linkedin.com/in/esteban-cardona-60163685/">
    <img src="https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555" alt="LinkedIn">
</a>
'''

# Renderizar enlace con logo en Streamlit
st.markdown(linkedin_html, unsafe_allow_html=True)


# Primer cuadro con logo lottie para mostrar la presentacion de la primera parte: 

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl('https://lottie.host/05f75412-c03a-4cb4-a390-63ec8731339d/aMRDZ5kgjB.json')
imagen_video= Image.open('/Users/esteban/Phyton/Proyecto_final/images/Work.png')


# Empezamos explicando y abriendo el primer container sobre la aplicación 

with st.container():
    st.write("---")
    
    left_column, right_column = st.columns(2)
    
    with left_column:
        st.title("Guía para encontrar tu trabajo remoto ideal." )
        st.write("""
        
        En esta guía, te proporcionaremos consejos y estrategias prácticas para encontrar el trabajo remoto ideal. Descubrirás cómo identificar las oportunidades laborales adecuadas, mejorar tu perfil profesional, y maximizar tus posibilidades de éxito en el mundo del trabajo remoto. ¡Prepárate para comenzar tu aventura en el trabajo remoto y alcanzar tu libertad laboral. 
        """
                )
        
        st.write("[linkedin >](https://www.linkedin.com/jobs/search?keywords=&location=España&locationId=&geoId=105646813&f_TPR=&f_WT=2&position=1&pageNum=0)")
                     
    with right_column:
                 
        st_lottie(lottie_coding, height = 300, key ="coding")
        
#  Empezamos con la carga de datos de SQL:        

def main():
    str_conn = 'mysql+pymysql://root:Marconi1991@localhost:3306/Teletrabajo'
    engine = create_engine(str_conn)
    consulta_sql = 'SELECT * FROM Teletrabajo.linkedin'
    df = pd.read_sql(consulta_sql, engine)

    # Convertir la columna de fecha a formato de fecha y hora
    df['Date'] = pd.to_datetime(df['Date'])

    # Necesito agregar columnas de mes y año
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year

    # Necesito reordenar las columnas en el DataFrame
    df = df[['Company', 'Title', 'Type', 'Level', 'Industry','Location','Link','Description','Date', 'Month', 'Year']]

    # Título de la aplicación
    st.header("Empleos")

    # Mostrar el DataFrame con las columnas en el orden deseado
    st.subheader("Listado de empleos")
    st.dataframe(df)


    # Agruego un filtro por ubicación
    st.subheader("Filtro por ubicación")
    ubicaciones = st.multiselect('Selecciona ubicaciones', df['Location'].unique())
    df_filtered_ubicacion = df[df['Location'].isin(ubicaciones)]
    st.dataframe(df_filtered_ubicacion)

    # Se muestra sección solo cuando se aplique el filtro por ubicación:
    if len(ubicaciones) > 0:
        # Filtro por rango de fechas
        st.subheader("Filtro por rango de fechas")
        fecha_inicio = st.date_input("Selecciona fecha de inicio")
        fecha_fin = st.date_input("Selecciona fecha de fin")

        # Convertir objetos date a objetos datetime
        fecha_inicio_dt = pd.to_datetime(fecha_inicio)
        fecha_fin_dt = pd.to_datetime(fecha_fin)

        df_date_filtered = df_filtered_ubicacion[(df_filtered_ubicacion['Date'] >= fecha_inicio_dt) & (df_filtered_ubicacion['Date'] <= fecha_fin_dt)]
        st.dataframe(df_date_filtered)

        # Se Muestra sección solo cuando se aplique el filtro por fecha
        #if not df_date_filtered.empty:
            # Enlaces interactivos
            #st.subheader("Descripción de empleos")
           # for index, row in df_date_filtered.iterrows():
                #st.write(f"[{row['Title']}]({row['Link']})")
                #st.write(row['Description'])


        # Se muestra sección solo cuando se aplique el filtro por fecha
        if not df_date_filtered.empty:
            # Enlaces interactivos
            st.subheader("Descripción de empleos")
            for index, row in df_date_filtered.iterrows():
                st.write(f"[{row['Title']}]({row['Link']})")
                descripcion = row['Description']
                descripcion_corta = descripcion[:250]  # Obtener los primeros 250 caracteres

                with st.expander(f"Descripción del empleo: {row['Title']}"):
                    st.write(descripcion_corta)
                    if len(descripcion) > 250:
                        if st.button(f"Leer más {index}..."):  # Assign a unique key based on the index
                            st.write(descripcion)
                        else:
                            st.write("...")  # Agregar texto de resumen o un indicador de que hay más contenido
                

    # Contador de empleos por mes
    st.header("Contador de empleos por mes")
    jobs_by_month = df.groupby('Month').size()
    st.bar_chart(jobs_by_month, color="rgb(128 89 243)")

    # Contador de empleos por año
    #st.header("Contador de empleos por año")
    #jobs_by_year = df.groupby('Year').size()
    #st.line_chart(jobs_by_year)

if __name__ == '__main__':
    main()

    
    
    
    
# Para mejorar el estilo, modifico algunas cosas del css de la pagina :    
    
    
css = """

}
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


.css-nahz7x a {
    color: rgb(128 89 243);
    
}

.st-fj {
    background-color: rgb(128 89 243)!important;
}

.st-bv {
    border: 1px solid  #8059f3 !important;
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
    
st.sidebar.markdown(""" <img class="work-connect-custom" src="http://localhost:8501/media/a02dd0fdec9cb585f8f97023966e081bf905e601705ef6ee4dbe3edc.png"> """,unsafe_allow_html=True)

                   

