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

from PIL import Image
# Obtener la ruta absoluta del directorio actual
current_directory = os.path.dirname(__file__)

# Construir la ruta completa a la imagen
image_path = os.path.join(current_directory, 'src', '1.jpg')

# Cargar la imagen y mostrarla
imagen = Image.open(image_path)
st.image(imagen, caption='', use_column_width=True)

#from PIL import Image
# Cargar una imagen desde un archivo .jpg o .png
#imagen = Image.open('src/1.jpg')
# Mostrar la imagen en la aplicación
#st.image(imagen, caption='', use_column_width=True)

# Cargar una imagen desde un archivo .jpg o .png
#imagen = Image.open('src/2.jpg') 
# Mostrar la imagen en la aplicación
#st.image(imagen, caption='', use_column_width=True)



#Ejemplos de llenado (Help)
experiencias_help = "Texto de Ejemplo: Que tenga experiencia en análisis de datos, machine learning y big data"
herramientas_help = "Texto de Ejemplo: Que utilice Python avanzado: Pandas, NumPy, PyTorch, TensorFlow, Keras, Matplotlib, Seaborn, Scikit-Learn, Transformers"
# Cajas de entrada de texto
experiencias = st.text_area("Background y Experiencias Laborales", max_chars=200, help=experiencias_help)
herramientas = st.text_area("Herramientas Técnicas Para el Puesto", max_chars=200, help=herramientas_help)

# Caja para elegir un número del 1 al 50
k = st.number_input("Escribí el número de CVs que deseás traer (1 a 50)", min_value=1, max_value=50, value=3)


# Filtro
st.markdown("Indicá a la base de datos de cuál o cuáles usuarios deseás acceder (1 a 5) 🔍")
opcion = st.multiselect("Elegir usuarios:", ["usuario1", "usuario2", "usuario3", "usuario4", "usuario5"])


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

st.write('🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀')
st.subheader('🚀🚀 Estos son los Match de tu Búsqueda Actual 🚀🚀')
st.write('🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀')
for i, doc in enumerate(docs):
    st.write(f'Documento {i+1}: ')
    st.write(doc.metadata['name'])
    st.write(doc.page_content)
    st.write('🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀')