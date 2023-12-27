import arcpy

pro_project_path = r"D:\Programming for GIS-3\P9_Automating_Map_Production\ProProject_Mapping\ProProject_Mapping.aprx"

my_project = arcpy.mp.ArcGISProject(pro_project_path)

maps_list = my_project.listMaps()

for map in maps_list:
    if map.name == "CURRENT":
        lyr_list = map.listLayers()
        for lyr in lyr_list:
            print(lyr.name)


print(".............................................................")

layout_list = my_project.listLayouts()

for layout in layout_list:
     if layout.name == "SAN_DIEGO_MAP":
         output_path = r"D:\Programming for GIS-3\P9_Automating_Map_Production\Outout"

         layout.exportToPDF(output_path)

print("Process Completed")

