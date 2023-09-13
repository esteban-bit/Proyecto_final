# Proyecto_final
### WorkConnect

  <a href="https://github.com/esteban-bit/Proyecto_final">
    <img src= "/Users/esteban/Phyton/Proyecto_final/images/Work.png" alt="Logo" width="500" height="200">
</a>

## CONTENIDO 📑
[1 - Objetivo ](#O)<br />
[2 - Enrequecimiento del dato](#ENR) <br />
[3 - Streamlit ](#DS) <br />
&nbsp;&nbsp;&nbsp;&nbsp; [3.1 - Menu](#CT) <br />
&nbsp;&nbsp;&nbsp;&nbsp; [3.2 - Vivienda](#CT) <br />
&nbsp;&nbsp;&nbsp;&nbsp; [3.3 - Trabajo](#CI) <br />
&nbsp;&nbsp;&nbsp;&nbsp; [3.4 - Ciudad](#AIR) <br />
&nbsp;&nbsp;&nbsp;&nbsp; [3.5 - Temperatura](#TEM) <br />
&nbsp;&nbsp;&nbsp;&nbsp; [3.6 - Carril bici](#BICI) <br />
[4 - Conclusiones ](#CONC) <br />

## 1. OBJETIVO. <a name="O"/>   

- El objetivo de mi proyecto final es poner en práctica todo lo que he aprendido en Ironhack, creando una web interactiva  y alimentando las bases de datos extraidas en los dos proyectos anteriores.

- ETL (Extracción, Transformación y Carga de datos) Linkedin.

- Visualización interactiva utilizando Streamlit.

## 2. Enriquecimiento del dato.<a name="ENR"/> 

- 2.1 Se utilizaron técnicas de web scraping con Selenium para extraer datos de empleos remotos. 
Proporcionando información detallada sobre oportunidades laborales que permiten trabajar de forma remota.

- 2.2 Se limpian los valores para asegurar su calidad y coherencia.

- 2.3 Se guardan el nuevo CSV.

- 2.4 Se crea nueva base de datos en SQL.


## 3. Streamlit.  <a name="DS"/>
### 3.1 Menu. <a name="CT"/>

En la pagina "Menu.py" del proyecto podemos ver:

  - 3.1.1 Importación de las librerias a utilizar.
  - 3.1.2 Se crea una función de Lottie para enriquecer visualmente la experiencia.
  - 3.1.3 Se crea un primer contendor para exponer el prototipo de la aplicación:
    - Columna izquierda: Se da a conocer la aplicación.
    - Columnda derecha: Se llama a la funcion de Lottie para visualizar.

- 3.1.4 El ultimo contenedor se añade video explicativo del prototipo expuesto.
- 3.1.5 Para mejorar el estilo, se crea una variable de CSS para añadir a Streamlit y se aplica en Markdown.
- 3.1.6 Importamos imagen de marca para que se muestre en streamlit.

### 3.2 Vivienda. <a name="CT"/>

En la pagina "Vivienda.py" del proyecto podemos ver:

- 3.2.1 Se crea una función de Lottie para enriquecer visualmente la experiencia.
  
- 3.2.2 Se crea un primer contenedor para exponer el prototipo de la aplicación:
  - Columna izquierda: Se da a conocer la aplicación: "Guía para encontrar la vivienda ideal al mejor precio"
  - Columnda derecha: Se llama a la funcion de Lottie para visualizar.
  
- 3.2.3 Variable con coordenadas de municipios de España y poder utilizar Folium.
- 3.2.4 Se procede a crear un def de color, para los banderines del mapa.
- 3.2.5 Empezamos con la carga de datos de SQL.
- 3.2.6 Con st.sidebar.radio crea pestañas para alquileres y ventas, la cual generamos un bucle segun se realice el filtro.
- 3.2.7 Procedemos con el codigo de alquileres y su visualización con Folium:
- 3.2.8 Procedemos con el codigo ventas de alquileres
- 3.2.9 Procedemos con la visualización grafica:


- 3.2.10 Para mejorar el estilo, se crea una variable de CSS para añadir a Streamlit y se aplica en Markdown.
- 3.2.11 Importamos imagen de marca para que se muestre en streamlit.

### 3.3 Trabajo. <a name="CI"/>

- 3.3.1 Se renderiza un primer link con HTML para enlazar con mi perfil de linkedin.
  
- 3.3.1 Se crea una función de Lottie para enriquecer visualmente la experiencia.
  
- 3.3.2 Se crea un primer contenedor para exponer el prototipo de la aplicación:
  - Columna izquierda: Se da a conocer la aplicación: "Guía para encontrar tu trabajo remoto ideal"
  - Columnda derecha: Se llama a la funcion de Lottie para visualizar.
  
- 3.3.4 Empezamos con la carga de datos de SQL.
- 3.3.5 Nos aseguramos de tener el formato fecha.
- 3.3.6 Creamos dos columnas con mes y año.
- 3.3.7 Se ordena el dataframe para que se muestre lo importante.
- 3.3.8 Establecemos el titulo.
- 3.3.9 Mostramos el DF con el orden deseado.
- 3.3.10 se crea un filtro por ubicacion.
- 3.3.11 Se crea codigo donde muestra sección solo cuando se aplique el filtro por ubicación.
- 3.3.12 Filtro por rango de fechas.
- 3.3.13 Convertir objetos date a objetos datetime.
- 3.3.14 Enlaces interactivos
- 3.3.15 Descripcion del empleo: se crea un bucle for dese index donde aparece el titulo con el link del empleo. 
- 3.3.16 Contador de empleos por mes.

### 3.4 Ciudad <a name="AIR"/>

En la pagina "Ciudad.py" del proyecto podemos ver:

- 3.4.1 Se crea una función de Lottie para enriquecer visualmente la experiencia.
  
- 3.4.2 Se crea un primer contenedor para exponer el prototipo de la aplicación:
  - Columna izquierda: Se da a conocer la aplicación: "Guía para encontrar la vivienda ideal al mejor precio"
  - Columnda derecha: Se llama a la funcion de Lottie para visualizar.