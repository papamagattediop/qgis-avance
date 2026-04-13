from osgeo import gdal
import numpy as np
from skimage.filters import threshold_otsu

chemin = r"C:\Users\Papa Magatte Diop\Desktop\Etude AS3\QGIS AVANCE\Projet Final"

indices = ["NDVI_2015", "NDVI_2025", "NDWI_2015", "NDWI_2025",
           "NDBI_2015", "NDBI_2025", "SAVI_2015", "SAVI_2025",
           "BSI_2015", "BSI_2025"]

for indice in indices:
    # Charge raster
    raster = gdal.Open(f"{chemin}\\{indice}.tif")
    array = raster.GetRasterBand(1).ReadAsArray().astype(float)
    
    # Filtrage valeurs valides
    array_filtre = array[~np.isnan(array)]
    array_filtre = array_filtre[np.isfinite(array_filtre)]
    array_filtre = array_filtre[(array_filtre >= -1) & (array_filtre <= 1)]
    
    # Calcul seuil Otsu
    seuil = threshold_otsu(array_filtre)
    print(f"{indice} → Seuil Otsu : {seuil:.6f}")
    
    # Applique seuillage binaire
    binaire = (array > seuil).astype(np.uint8)
    
    # Sauvegarde
    driver = gdal.GetDriverByName("GTiff")
    sortie = driver.Create(
        f"{chemin}\\{indice}_bin.tif",
        raster.RasterXSize, raster.RasterYSize, 1, gdal.GDT_Byte
    )
    sortie.SetGeoTransform(raster.GetGeoTransform())
    sortie.SetProjection(raster.GetProjection())
    sortie.GetRasterBand(1).WriteArray(binaire)
    sortie.FlushCache()
    print(f"{indice}_bin.tif créé ✅")
    
import glob

fichiers_bin = glob.glob(f"{chemin}\\*_bin.tif")
for f in fichiers_bin:
    iface.addRasterLayer(f, f.split("\\")[-1].replace(".tif",""))

print("Terminé !")