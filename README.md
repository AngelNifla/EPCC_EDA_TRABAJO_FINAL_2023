# EPCC_EDA_TRABAJO_FINAL_2023
Repositorio del Trabajo Final del curso Estructura de Datos Avanzados 2023 correspondiente al PARCIAL III


# Árbol KD y Visualización 3D para Datos de Salud Pública
Este proyecto tiene como objetivo implementar un Árbol KD (K-Dimensional) y una visualización tridimensional para datos relacionados con la salud pública, específicamente en el contexto de la pandemia de SARS-Cov-2. El Árbol KD se utiliza para organizar y estructurar datos multidimensionales, facilitando operaciones como inserción, eliminación y actualización, así como consultas de rango eficientes.

## Propósito y Alcance
- **Árbol KD:** Se implementa un Árbol KD para organizar y gestionar datos relacionados con la salud pública. Este árbol proporciona una estructura eficiente para realizar operaciones en conjuntos de datos multidimensionales, como los obtenidos de pruebas de laboratorio y evaluaciones médicas.

- **Visualización 3D:** Se incluye una visualización tridimensional de los datos utilizando matplotlib. La visualización permite observar la distribución de puntos en un espacio tridimensional, lo que puede ser útil para identificar patrones o agrupamientos en los datos.


## Instrucciones de Uso
1. **Lectura de Datos:**
   - Asegúrate de tener el archivo `covid_DB.xlsx` en la carpeta `Files`.
   - Ejecuta el script `DataProcessing.py` para preparar los datos.

2. **Árbol KD y Visualización 3D:**
   - Ejecuta el script `Kdtree.py` para construir y visualizar el árbol KD.

3. **Dependencias:**
   - Asegúrate de tener las bibliotecas necesarias instaladas. Puedes instalarlas con `pip install -r requirements.txt`.

## Estructura del Proyecto
- `DataProcessing.py`: Prepara los datos desde `covid_DB.xlsx`.
- `Kdtree.py`: Implementa el árbol KD y la visualización 3D.
- `FetchedData.csv`: Archivo CSV con datos seleccionados.
- `PSA3Def.csv`: Archivo CSV con componentes principales.
- `PSADef.csv`: Archivo CSV con componentes principales y etiquetas.

## Requisitos del Sistema y Dependencias
- Python 3.8
- Bibliotecas: pandas, scikit-learn, matplotlib

## Contribuidores
Este proyecto fue implementado por un equipo de 5 estudiantes EPCC UNSA.

- **Katherine Nikole Béjar Román**
- **Sennayda Rimache Choquehuanca**
- **Manuel Angel Nifla Llallacachi**
- **Leonardo Montoya Choque**
- **Antony Aroni Jarata**

