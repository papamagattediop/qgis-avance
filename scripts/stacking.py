from osgeo import gdal
import numpy as np

chemin = r"C:\Users\Papa Magatte Diop\Desktop\Etude AS3\QGIS AVANCE\Projet Final"

# Liste des fichiers à empiler (indices bruts + binaires)
fichiers_2015 = [
    "NDVI_2015.tif", "NDWI_2015.tif", "NDBI_2015.tif", "SAVI_2015.tif", "BSI_2015.tif",
    "NDVI_2015_bin.tif", "NDWI_2015_bin.tif", "NDBI_2015_bin.tif", "SAVI_2015_bin.tif", "BSI_2015_bin.tif"
]

fichiers_2025 = [
    "NDVI_2025.tif", "NDWI_2025.tif", "NDBI_2025.tif", "SAVI_2025.tif", "BSI_2025.tif",
    "NDVI_2025_bin.tif", "NDWI_2025_bin.tif", "NDBI_2025_bin.tif", "SAVI_2025_bin.tif", "BSI_2025_bin.tif"
]

def empiler(fichiers, sortie_nom):
    rasters = [gdal.Open(f"{chemin}\\{f}") for f in fichiers]
    cols = rasters[0].RasterXSize
    rows = rasters[0].RasterYSize
    
    driver = gdal.GetDriverByName("GTiff")
    sortie = driver.Create(f"{chemin}\\{sortie_nom}", cols, rows, len(rasters), gdal.GDT_Float32)
    sortie.SetGeoTransform(rasters[0].GetGeoTransform())
    sortie.SetProjection(rasters[0].GetProjection())
    
    for i, r in enumerate(rasters):
        array = r.GetRasterBand(1).ReadAsArray().astype(float)
        sortie.GetRasterBand(i+1).WriteArray(array)
        print(f"Bande {i+1} ajoutée : {fichiers[i]}")
    
    sortie.FlushCache()
    print(f"{sortie_nom} créé ✅")

empiler(fichiers_2015, "stack_2015.tif")
empiler(fichiers_2025, "stack_2025.tif")