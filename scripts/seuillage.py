from osgeo import gdal
import numpy as np
from skimage.filters import threshold_otsu

chemin = r"C:\Users\Papa Magatte Diop\Desktop\Etude AS3\QGIS AVANCE\Projet Final"

indices = ["NDVI_2015", "NDVI_2025", "NDWI_2015", "NDWI_2025",
           "NDBI_2015", "NDBI_2025", "SAVI_2015", "SAVI_2025",
           "BSI_2015", "BSI_2025"]

for indice in indices:
    raster = gdal.Open(f"{chemin}\\{indice}.tif")
    array = raster.GetRasterBand(1).ReadAsArray().astype(float)
    
    # Filtrage strict des valeurs aberrantes
    array = array[~np.isnan(array)]
    array = array[np.isfinite(array)]
    array = array[(array >= -1) & (array <= 1)]  # plage valide indices
    
    seuil = threshold_otsu(array)
    print(f"{indice} → Seuil Otsu : {seuil:.6f}")