# This is the python_file sample that contains script and comments that provide background and examples ....

# In this module we will cover reading from and writing to external, non-geospatial
# files such as text files or spreadsheets.

# Let's focus of text files for now, and let's write to the file.

# First you'll need to open an instance of the file

import arcpy

arcpy.env.workspace = "C:"

arcpy.env.overwriteOutput = True

out = "text.txt"

open(infile, w) # This creates and instance and allows it to be written to.

# using "w" will overwrite the file, to simply add to it, use "a" (Append)


# Using a similar code to Module 4...
with arcpy.da.SearchCursor(cities, ["NAME", "X_CO", "Y_CO" "SHAPE@X", "SHAPE@Y"]) as cursor:
    for row in cursor:
        NAME = row[0]
        x = row[4]
        y = row[5]

# If we would like to write city names along with X Y coordinates
# all we need to do from here to write to the document is...

        out.write("{0}, {1}, {2}".format(NAME, x, y,)) # writes the data in correct format
        out.write("\n") # Serves as a line return function

out.close() # If you don't close the instance it will not save correctly

# Easy enough, right? The reverse is a bit more tricky
# Reading spatial data from text files and creating geospatial files from them can be done.

shp = trails.shp
infile = open(trailstxt.txt, r)

# for this scenario the .shp exists and contains a "Name" field but no data.
# You could create the file from scratch here if you needed to though.

# The text file contains lines with data as Name, X, Y with one entry per row.

# We will use an insert cursor for this task

cursor - arcpy.da.InsertCursor(shp, ["Name", "SHAPE@"])
PList = arcpy.Array() # This creates a place to store all the coordinates for a line before we create  it.

for item in infile:

    Segment = item.split(", ") # This creates individual items per line that we can call,
                            # splitting the lines at the specified point (", ")

    # since each line has a name, and each row contains that name, we can store our line data based on that name

    # Used when a new name is present in line
    if LName <> Segment[0]:

        # Writes current array to shp
        if len(PList) > 0:
            pL = arcpy.Polyline(PList)
            cursor.insertRow((LName, pL))
            print "Added " + LName

        # defines lineName
        LName = lineSeg[0]
        # Creates empty array for next polyline
        PList = arcpy.Array()

        # Populates coordinates of current line
        point = arcpy.Point(Segment[1], Segment[2])
        pointList.add(point)


    # Loop for lines where name if already defined
    else:
        # Populates coordinates of current line
        point = arcpy.Point(Segment[1], Segment[2])
        PList.add(point)

# Writes final polyline to shapefile.
pL = arcpy.Polyline(PList)
cursor.insertRow((LName, p:))
print "Added " + LName

# Close file and delete cursor
infile.close()
del cursor
