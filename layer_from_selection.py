# A script to automate making layers from a selection. In this case, I'm looking for specific retailers from an existing attribute table.
# Script by Alexandria Washington, alex@awanalysis.com
# Last updated: 02/01/2021
# TODO: Make "major_chains" user input OR tie to a DB
# TODO: Allow user to determine where features are copied to (handle sublayers)

import arcpy

# Set env, subject table, and selection type
# arcpy.env.workspace = 'C:\\Users\\aowas\\Documents\\Work\\Vertique\\carwashes\\Carwashes.gdb'

subject_table= arcpy.management.SelectLayerByAttribute('table_in_workspace','NEW_SELECTION') # Change 'table_in_workspace' to actual table

major_chains= ['Retailer1','Retailer2','Retailer3'] # Populate with retailers

# Select & output to layers
# TODO: Implement something more precise than LIKE
for chain in major_chains:
    print("Current retailer: {}\n".format(chain))
    arcpy.env.overwriteOutput=True
    sub_select= arcpy.management.SelectLayerByAttribute(subject_table, 'NEW_SELECTION','"column_in_table" LIKE \'%{}%\''.format(chain)) # Change "column-in-table" to relevant column
    # TODO: More elegantly handle illegal characters (spaces, dashes, and apostrophes)
    chain= chain.replace(" ","_")
    chain= chain.replace("-","_")
    chain= chain.replace("&","_")
    arcpy.CopyFeatures_management(sub_select, "{}".format(chain))