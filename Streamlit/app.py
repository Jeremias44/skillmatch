import streamlit as st
import pinecone
from langchain.vectorstores import Pinecone
from langchain.embeddings import HuggingFaceEmbeddings
import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIROMENT = os.getenv('PINECONE_ENVIROMENT')

pinecone.init(api_key=PINECONE_API_KEY, environment=PINECONE_ENVIROMENT) # key de Jeremias44
indexName = 'index-skill-matchcv' # indexName de Jeremias44
# Conexión con index
index = pinecone.Index(index_name=indexName)
embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2') # modelo de embeddings
docSearch = Pinecone.from_existing_index(indexName, embeddings)

st.title('¡Encontrá el Talento Que Buscás!🚀')
from PIL import Image
# Obtener la ruta absoluta del directorio actual
current_directory = os.path.dirname(__file__)
# Construir la ruta completa a la imagen 1
image_path = os.path.join(current_directory, 'media', '1.png')
# Cargar la imagen y mostrarla
imagen = Image.open(image_path)
st.image(imagen, caption='', use_column_width=True)
# Construir la ruta completa a la imagen 2
image_path = os.path.join(current_directory, 'media', '2.png')
# Cargar la imagen y mostrarla
imagen = Image.open(image_path)
st.image(imagen, caption='', use_column_width=True)

# Crear una columna lateral
# Construir la ruta completa a la imagen 3
image_path = os.path.join(current_directory, 'media', '3.png')
# Cargar la imagen y mostrarla en la columna lateral
imagen2 = Image.open(image_path)
st.sidebar.image(imagen2, caption='', use_column_width=True)

usuario = st.sidebar.text_input("Usuario")
clave = st.sidebar.text_input("Clave", type="password")

# Verificar las credenciales
if (usuario == 'usuario1' and clave == "clave1"):
    st.sidebar.write("¡Acceso permitido!")

    #Ejemplos de llenado (Help)
    experiencias_help = "Texto de Ejemplo: Que tenga experiencia en análisis de datos, machine learning y big data"
    herramientas_help = "Texto de Ejemplo: Que utilice Python avanzado: Pandas, NumPy, PyTorch, TensorFlow, Keras, Matplotlib, Seaborn, Scikit-Learn, Transformers"
    # Cajas de entrada de texto
    experiencias = st.text_area("Background y Experiencias Laborales", max_chars=200, help=experiencias_help)
    herramientas = st.text_area("Herramientas Técnicas Para el Puesto", max_chars=200, help=herramientas_help)

    # Caja para elegir un número del 1 al 50
    k = st.number_input("Escribí el número de CVs que deseás traer (1 a 50)", min_value=1, max_value=50, value=3)

    # Filtro
    opcion = st.multiselect("Indicá a la base de datos de cuál o cuáles usuarios deseás acceder (1 a 5) 🔍:", ["usuario1", "usuario2", "usuario3", "usuario4", "usuario5"])

    query = f' {experiencias} {herramientas}'
    docs=docSearch.similarity_search(query, k=k, filter=
                                    {
                                        #'category': {'$eq': str},
                                        #'chunk_n': {'$gte': int},
                                        #'chunk_size': {'$gte': int},
                                        #'chunks_total': {'$gte': int},
                                        #'dateYear': {'$gte': int},
                                        #'dateMonth': {'$gte': int},
                                        #'dateDay': {'$gte': int},
                                        #'format': {'$eq': str},
                                        #'name': {'$eq': str},
                                        #'path': {'$eq': str},
                                        #'timeHour': {'$eq': int},
                                        #'timeMinutes': {'$eq': int},
                                        #'timeSeconds': {'$eq': int},
                                        'user': {'$in': opcion}
                                        })
    
if st.button("Ver Currículums Seleccionados"):
    st.write('🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀')
    st.subheader('🚀🚀 Estos son los Match de tu Búsqueda Actual 🚀🚀')
    st.write('🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀')
    try:
        for i, doc in enumerate(docs):
            st.write(f'Documento {i+1}: ')
            st.write(doc.metadata['name'])
            st.write(doc.page_content)
            st.write('🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀')
    except:
        st.write('Se solicita acceder con credenciales (usuario y clave)')

else:
    st.sidebar.write("Sin acceso. Coloque un usuario y clave válidos o ingrese como invitado")


st.sidebar.markdown("### Contacta con el autor del sitio")
st.sidebar.markdown("[Jeremías Pombo en LinkedIn](https://www.linkedin.com/in/jeremiaspombo/)")
st.sidebar.markdown("### Visita el repositorio del proyecto")
st.sidebar.markdown("[Repositorio de GitHub](https://github.com/Jeremias44/skillmatch)")