# A script to automate buffering of sites.
# Script by Alexandria Washington, alex@awanalysis.com
# Last updated: 02/01/2021
# TODO: Dynamic paths
# TODO: Honestly... probably gonna need to connect to a db

import arcpy

# Each state has a list of locations.
# TODO: Develop naming/file schema so each list is populated by iterating over layers instead of hard-coding them
state1_locations= ['Location1','Location2','Location3'] # Populate these as relevant, and add as many as you need
state2_locations= ['Location1','Location2','Location3']
state3_locations= ['Location1','Location2','Location3']


# Dictionary so user can choose which locations to cover.
# TODO: Develop module/db that has a dictionary/list combo for all states and sites for a given client
location_dict= {"ST1": state1_locations,
"ST2": state2_locations,
"ST3": state3_locations
} # I recommend keeping the keys simple (ex., for states, use the two-letter abbrev)

# User inputs variables here
# TODO: Make it possible for user to process multiple buffer distances at a time
state= input("What state are your sites in? Please use two-letter abbreviations. \n")
state= state.upper()
locations= location_dict.get(state)
distance= input("How many miles do you want this buffer to encompass? \n")

# TODO: Group output layer with input layer
for location in locations:
    full_location= "layer_path_{}".format(state,location,location)
    print("Working on: {}...\n".format(full_location))
    buff_output= "path\\{}_{}mi".format(location,distance)
    distance_unit= "MILES" # MURICA
    side_type= "FULL"
    end_type= "ROUND"
    buffer_test= arcpy.Buffer_analysis(full_location, buff_output, "{} {}".format(distance,distance_unit), side_type, end_type)