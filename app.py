import streamlit as st
import pinecone
from langchain.vectorstores import Pinecone
from langchain.embeddings import HuggingFaceEmbeddings
import os

pinecone.init(api_key='98dca4b8-ad18-44c2-a874-d9089eaf079c', environment='gcp-starter') # key de Jeremias44
indexName = 'index-skill-matchcv' # indexName de Jeremias44
# Conexión con index
index = pinecone.Index(index_name=indexName)
embeddings=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2') # modelo de embeddings
docSearch = Pinecone.from_existing_index(indexName, embeddings)





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
st.subheader("🚀🚀 Estos son los Match de tu Búsqueda Actual 🚀🚀")
st.write('🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀')
for i, doc in enumerate(docs):
    st.write(f'Documento {i+1}: ')
    st.write(doc.metadata['name'])
    st.write(doc.page_content)
    st.write('🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀🚀')