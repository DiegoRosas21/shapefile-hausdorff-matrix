# shapefile-hausdorff-matrix
Python script to calculate the pairwise Hausdorff distance between multiple shapefiles in a directory and output the results as a CSV distance matrix. Uses GeoPandas and Shapely.

Script de Python para calcular la distancia de Hausdorff por pares entre múltiples shapefiles en un directorio y exportar los resultados como una matriz de distancias CSV. Usa GeoPandas y Shapely.

## Descripción

Este script de Python calcula la distancia de Hausdorff por pares entre múltiples shapefiles (.shp) ubicados dentro de un directorio especificado. Combina todas las geometrías dentro de cada shapefile en una sola geometría representativa (`union_all`) antes de calcular la distancia. El resultado es un archivo CSV que contiene una matriz de distancias simétrica, donde cada celda (i, j) representa la distancia de Hausdorff entre el shapefile `i` y el shapefile `j`.

## Características

*   Lee todos los archivos `.shp` de un directorio de entrada.
*   Fusiona las geometrías dentro de cada shapefile usando `union_all()`.
*   Calcula las distancias de Hausdorff por pares utilizando `shapely`.
*   Genera una matriz de distancias en formato CSV, fácil de leer y usar, con los nombres de los shapefiles como cabeceras y etiquetas de fila.

## Requisitos

*   Python 3.x
*   Bibliotecas de Python:
    *   `geopandas`
    *   `shapely`
    *   `numpy`
    *   `pandas` (generalmente instalado como dependencia de geopandas)

Puedes instalar todas las dependencias fácilmente usando el archivo `requirements.txt` (si lo creas):
`pip install -r requirements.txt`

## Configuración ⚠️ ¡Importante!

Antes de ejecutar el script, **DEBES** modificar las siguientes variables directamente dentro del archivo `main.py`:

1.  **`directory`**:
    *   **Qué es:** La ruta a la carpeta que contiene tus archivos shapefile (`.shp`, `.shx`, `.dbf`, etc.).
    *   **Acción:** Reemplaza el valor actual (`'C:\\haus'`) con la **ruta absoluta** a tu directorio.
    *   **Formato:**
        *   En Windows: Usa doble barra invertida (`\\`) o una barra inclinada (`/`). Ejemplo: `'C:/Users/TuUsuario/MisDocumentos/MisShapefiles'` o `'C:\\Users\\TuUsuario\\MisDocumentos\\MisShapefiles'`.
        *   En macOS/Linux: Usa barras inclinadas (`/`). Ejemplo: `'/home/tu_usuario/datos/shapefiles'`.

2.  **`output_file` (Nombre del archivo de salida):**
    *   **Qué es:** El nombre del archivo CSV que se generará.
    *   **Comportamiento Actual:** El script define inicialmente una ruta completa para `output_file`, pero **luego la sobrescribe** cerca del final para que sea simplemente `'dist_haus_2.csv'`. Esto significa que el archivo CSV se guardará en el **mismo directorio desde donde ejecutes el script `python main.py`**, no necesariamente en la carpeta de los shapefiles.
    *   **Acción (Opcional):** Si deseas un nombre de archivo diferente o guardarlo en una ubicación específica, modifica la línea *cerca del final del script*:
        ```python
        # Cambia 'dist_haus.csv' por la ruta y nombre deseados
        output_file = 'ruta/deseada/mi_matriz_distancias.csv'
        ```

## Uso

1.  Asegúrate de haber **configurado correctamente la variable `directory`** en `main.py`.
2.  Abre tu terminal o línea de comandos.
3.  Navega hasta el directorio donde guardaste el archivo `main.py`.
4.  (Si usas un entorno virtual, asegúrate de que esté activado).
5.  Ejecuta el script:
    ```bash
    python main.py
    ```
6.  El script procesará los archivos y, si todo va bien, imprimirá un mensaje de confirmación:
    `Los resultados se han guardado en el archivo 'dist_haus_2.csv'` (o el nombre que hayas configurado).
7.  Busca el archivo CSV de salida en el directorio desde donde ejecutaste el script.

## Descripción del Archivo de Salida (CSV)

El archivo CSV generado (`dist_haus.csv` por defecto) contendrá:

*   **Primera fila (Cabecera):** Una celda vacía seguida por los nombres base (sin la extensión `.shp`) de los shapefiles de entrada.
*   **Filas siguientes:** Cada fila comienza con el nombre base de un shapefile (etiqueta de fila), seguido por los valores de la distancia de Hausdorff calculada entre ese shapefile y cada uno de los shapefiles listados en la cabecera (en orden).
*   **Diagonal:** La distancia de un shapefile a sí mismo siempre será `0`.
*   **Simetría:** La matriz es simétrica (la distancia de A a B es igual a la distancia de B a A).

**Ejemplo de Salida:**

```csv
,Austroriparianprv,Chihuahuanprv,Oregonianprv
Austroriparianprv,0,27.016049229381334,46.66163362381724
Chihuahuanprv,27.016049229381334,0,30.50748108358096
Oregonianprv,46.66163362381724,30.50748108358096,0
