# Title: IT-338 Custom Tool Project
# Name: John A. Murray
# Course: IT-338
# Date: 2/15/2020

# Project number: 6-1

# Description: Build a custom tool, to use inside ArcGIS, to complete the task in
# Scripting Project Five. The tool should be
# capable of being added to a custom toolbar. It should be fully completed including
# directions and tooltips.



# Import arcpy module

print "Importing arcpy..."
import arcpy
print "[Done]"
print "Setting environment workspace and variables..."
arcpy.env.workspace = 'C:/SNHU/Geospatial Programming/module_5_data/mod 5.gdb'
arcpy.env.overwriteOutput = True


# Local variables:
Trails_Clip = "Trails_Clip"
Trails_Buffer = "Trails_Buffer"
Roads_Clip = "Roads_Clip"
Roads_Buffer = "Roads_Buffer"
Campsites_Clip = "Campsites_Clip"
Campsites_Buffer = "Campsites_Buffer"
print "[Done]"
Trails = arcpy.GetParameterAsText(0)
Roads = arcpy.GetParameterAsText(1)
Campsites = arcpy.GetParameterAsText(2)
Park = arcpy.GetParameterAsText(3)


# Process: Buffer Roads
arcpy.Buffer_analysis(Roads_Clip, Roads_Buffer, "2000 Feet", "FULL", "ROUND",
"ALL", "", "PLANAR")


# Process: Buffer Trails
arcpy.Buffer_analysis(Trails_Clip, Trails_Buffer, "100 Feet", "FULL", "ROUND",
"NONE", "", "PLANAR")


# Process: Buffer Campsites
arcpy.Buffer_analysis(Campsites_Clip, Campsites_Buffer, "500 Feet", "FULL",
"ROUND", "ALL", "", "PLANAR")


# Merge all Buffers
arcpy.Merge_management([Roads_Buffer, Trails_Buffer, Campsites_Buffer],
'Buffer_Merge')


#Erase Park and Buffers, rename Wilderness
Wilderness = arcpy.GetParameterAsText(4)
arcpy.Erase_analysis(Park,'Buffer_Merge','Wilderness')
