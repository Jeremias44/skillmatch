# Proceso de Creación de currículums Sintéticos

Este documento explica el proceso de creación de currículums sintéticos utilizando un notebook de Python. Los currículums generados son ficticios y se utilizan con fines de pruebas, ejemplos o cualquier otro propósito necesario. 

## Función `crear_cv`

El proceso comienza con una función llamada `crear_cv`. Esta función toma como entrada listas de nombres, apellidos, experiencias, habilidades, herramientas y puestos de trabajo. A continuación, se detalla cómo se crea un currículo sintético:

- Se selecciona un nombre y un apellido al azar de las listas proporcionadas.
- Se elige una experiencia y habilidades al azar de las listas proporcionadas.
- Se selecciona un número aleatorio de 3 a 12 herramientas técnicas de la lista proporcionada.
- Se elige un número aleatorio de 1 a 7 puestos de trabajo de la lista proporcionada.

Luego, se crea el contenido del currículo en formato de texto, que incluye:

- Nombre y apellido.
- Correo electrónico basado en el nombre y apellido.
- Información de experiencia y habilidades.
- Lista de herramientas técnicas utilizadas.
- Historial de experiencia laboral con puestos y años de experiencia.
- Idiomas (español nativo y, en algunos casos, otros idiomas).

Finalmente, el currículo se guarda en un archivo de texto con un nombre autoincremental en la carpeta "CV".

## Personalización de las Categorías

El proceso es altamente personalizable. Puedes ajustar las categorías de nombres, experiencias, habilidades, herramientas y puestos de trabajo editando los archivos en la carpeta "caracteristicas". Esto te permite adaptar el generador a tus necesidades específicas.

## Contador de Archivos

Para garantizar que cada currículum tenga un nombre único, el generador lleva un contador de archivos. El contador se guarda en un archivo "000contador.txt" y se actualiza automáticamente.

## Estructura de Carpetas

Los currículums se organizan en carpetas según la categoría a la que están orientados. Estas categorías incluyen:

- `data`: currículums orientados a Data Science.
- `full_stack`: currículums orientados a Full Stack.
- `finanzas`: currículums orientados a Finanzas.
- `RRHH`: currículums orientados a Recursos Humanos.

## Generación de currículums

El notebook genera currículums en lotes de 25 para cada categoría mencionada. Se puede ajustar la cantidad de currículums generados cambiando los números en los bucles.

## Licencia y Contacto

El proyecto se distribuye bajo la licencia MIT, lo que significa que es de código abierto y se puede utilizar y modificar libremente. Si tienes alguna pregunta o sugerencia, no dudes en ponerte en contacto.

* Email: jeremiaspombo@outlook.com
* LinkedIn: Jeremías Pombo en LinkedIn
* GitHub: Jeremías Pombo en GitHub

---

Este proceso permite crear currículums sintéticos para diferentes categorías de empleo de manera automatizada. Se puede utilizar para generar datos de prueba o ejemplos en entornos de trabajo.

