from qgis.analysis import QgsZonalStatistics
from qgis.core import QgsProject, QgsRasterLayer

chemin = r"C:\Users\Papa Magatte Diop\Desktop\Etude AS3\QGIS AVANCE\Projet Final"

indices = ["NDVI", "NDWI", "NDBI", "SAVI", "BSI"]
annees = ["2015", "2025"]

for annee in annees:
    bd = QgsProject.instance().mapLayersByName(f"bd_train_{annee}")[0]
    
    for nom in indices:
        path = f"{chemin}\\{nom}_{annee}.tif"
        raster_layer = QgsRasterLayer(path, nom)
        zs = QgsZonalStatistics(bd, raster_layer, nom+"_", 1, QgsZonalStatistics.Mean)
        zs.calculateStatistics(None)
        print(f"{annee} - {nom} ✅")

print("Tout terminé !")