# Proceso de Carga de currículums en Pinecone

Este documento explica el proceso de carga de currículums en el servicio Pinecone utilizando un Jupyter Notebook con Python. Pinecone es una plataforma de búsqueda y recuperación de vectores que se utiliza para buscar similitud en datos vectoriales. Este notebook se encarga de cargar documentos de currículums en Pinecone, extraer sus metadatos y texto, y mantener un registro de los currículums cargados en un DataFrame.

## Inicialización de Pinecone

El proceso comienza con la inicialización de la conexión a Pinecone utilizando una API Key proporcionada a través de la variable de entorno `PINECONE_API_KEY`. Se crea un índice en Pinecone con un nombre específico (en este caso, `index-skill-matchcv`) si no existe previamente.

## Descarga del Modelo de Embeddings

El script descarga un modelo de embeddings de HuggingFace llamado `sentence-transformers/all-MiniLM-L6-v2`. Estos embeddings se utilizan para representar el contenido de los documentos de currículums.

## Directorios y Configuración de Usuario

El script define varios directorios, como el directorio de carga de documentos (`documentsUploadPath`) y el directorio donde se moverán los documentos cargados (`loadedDocumentsPath`). Además, el usuario que carga los currículums debe proporcionar un nombre de usuario y contraseña, y elegir una categoría para los currículums a cargar.

## Carga de Documentos

El script comprueba si ya existe un DataFrame de currículums (`cv_df.csv`). Si existe, lo carga. Si no existe, crea un DataFrame vacío.

Luego, el script accede a los registros en Pinecone para verificar si los archivos ya han sido cargados en el índice. Si un archivo no está en Pinecone, se extrae su texto, se generan vectores y se cargan en Pinecone junto con los metadatos correspondientes.

Si un archivo ya ha sido cargado en Pinecone, se elimina del directorio de carga de documentos.

## Extracción de Metadatos y Texto

Los metadatos extraídos para cada currículum incluyen la categoría, fecha de carga, formato del archivo, nombre del archivo, ruta del archivo, hora de carga y el nombre de usuario que lo cargó. El texto se extrae de los mismos currículums.

## Almacenamiento en DataFrame

Los metadatos y el texto de cada currículum se almacenan en un nuevo registro en el DataFrame. El DataFrame se actualiza con cada currículum cargado.

## Guardado del DataFrame

El DataFrame se guarda en un archivo CSV llamado `cv_df.csv` para mantener un registro histórico de los currículums cargados.

## Licencia y Contacto

El proyecto se distribuye bajo la licencia MIT, lo que significa que es de código abierto y se puede utilizar y modificar libremente. Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto.

* Email: jeremiaspombo@outlook.com
* LinkedIn: Jeremías Pombo en LinkedIn
* GitHub: Jeremías Pombo en GitHub

---

Este proceso automatiza la carga de currículums en Pinecone y permite buscar similitudes en documentos de currículums. Se puede utilizar para indexar y buscar currículums con facilidad. En nuestro caso se utiliza junto a un script de python que creará una app de consulta web a través de Streamlit.


