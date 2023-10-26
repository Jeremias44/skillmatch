# Aplicación de Búsqueda de currículums con Streamlit y Pinecone

Esta aplicación utiliza `Streamlit` para crear una interfaz web que permite buscar currículums en una base de datos utilizando `Pinecone` como motor de búsqueda. Los currículums se almacenan en Pinecone con sus correspondientes metadatos y se pueden buscar por palabras clave.

## Requisitos Previos

Se requiere tener instaladas las bibliotecas de Python que se encuentran en `requirements.txt`

```bash
pip install -r requirements.txt
```

## Configuración

Antes de utilizar la aplicación, se deben configurar las credenciales de `Pinecone`. Se debe definir la variable de entorno `PINECONE_API_KEY` con la clave API de Pinecone y `PINECONE_ENVIROMENT` con el entorno deseado.

## Uso de la App

Para ejecutar la aplicación de manera local, se utiliza el siguiente comando:

```bash
streamlit run app.py
```

## Acceso a la Aplicación

La aplicación permite el acceso a través de un nombre de usuario y una contraseña. Para acceder, puedes utilizar las siguientes credenciales de muestra:

- Usuario: usuario1
- Clave: clave1

```python
usuario = st.sidebar.text_input("Usuario")
clave = st.sidebar.text_input("Clave", type="password")

if (usuario == 'usuario1' and clave == "clave1"):
    st.sidebar.write("¡Acceso permitido!")
```

## Búsqueda en el Índice de Pinecone

La aplicación se conecta al índice de Pinecone y realiza búsquedas de documentos similares a una consulta (query) enviada por el usuario. Aquí hay un ejemplo de cómo se realiza una búsqueda en Pinecone:

```python
query = f' {experiencias} {herramientas}'
docs = docSearch.similarity_search(query, k=k, filter= {
    # Puedes agregar filtros de metadatos aquí
})
```

## Filtrado por Metadatos


La aplicación permite filtrar los resultados de la búsqueda utilizando metadatos asociados a los documentos almacenados en Pinecone. Algunos de los metadatos disponibles para filtrar incluyen:

category: Categoría del currículo.
user: Usuario que cargó el currículo.
Puedes especificar estos filtros en el código de búsqueda como se muestra a continuación:

```python
docs = docSearch.similarity_search(query, k=k, filter= {
    'category': {'$eq': 'data'},
    'user': {'$in': ['usuario1', 'usuario2']}
})
```
En este ejemplo, se busca por documentos de la categoría "data" y se filtra por usuarios seleccionados.

Se pueden personalizar los filtros de metadatos según las necesidades del desarrollador o del usuario.

## Licencia y Contacto

El proyecto se distribuye bajo la licencia MIT, lo que significa que es de código abierto y se puede utilizar y modificar libremente. Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto.

* Linkedin: [Jeremías Pombo](https://www.linkedin.com/in/jeremiaspombo/)
* GitHub: [GitHub](https://github.com/Jeremias44)
* Correo electrónico: jeremiaspombo@outlook.com

---

Estos son solo ejemplos de muestra, la implementación real puede variar según los requisitos y la estructura de los datos en Pinecone.
