import os
import shapely
from shapely.geometry import MultiPolygon
import geopandas as gpd
import numpy as np
import csv

# Ruta del directorio donde se encuentran los shapefiles
directory = 'C:\\haus'
#'C:\Users\Zephyrus G15 2023\Downloads\hausdo\h2\haus

# Ruta y nombre del archivo de salida
output_file = 'C:\\haus\\dist_haus.csv'

# Obtener una lista de todos los archivos shapefiles en el directorio
shapefiles = [os.path.splitext(f)[0] for f in os.listdir(directory) if f.endswith('.shp')]
# Cargar todas las capas de polígonos
layers = []
for shapefile in [f"{s}.shp" for s in shapefiles]:
    layer = gpd.read_file(os.path.join(directory, shapefile))
    layer = layer.to_crs(layer.crs)  # Asegurarse de que todas las capas estén en el mismo sistema de coordenadas
    layers.append(layer)

# Crear una matriz cuadrada para almacenar las distancias
n = len(layers)
distances = [[0 for _ in range(n)] for _ in range(n)]

# Calcular las distancias de Hausdorff entre todas las combinaciones de capas
for i in range(n):
    multi_poly1 = layers[i].geometry.union_all()
    for j in range(n):
        if i == j:
            distances[i][j] = 0
        else:
            multi_poly2 = layers[j].geometry.union_all()
            hausdorff_distance = multi_poly1.hausdorff_distance(multi_poly2)
            distances[i][j] = hausdorff_distance
            distances[j][i] = hausdorff_distance  # Asegurar la simetría de la matriz

# Guardar los resultados en un archivo CSV
output_file = 'dist_haus.csv'
with open(output_file, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow([''] + shapefiles)  # Escribir los encabezados de columna
    for i, row in enumerate(distances):
        writer.writerow([shapefiles[i]] + [str(elem) for elem in row])

# Imprimir un mensaje indicando que los resultados se han guardado en el archivo
print(f"Los resultados se han guardado en el archivo '{output_file}'")

