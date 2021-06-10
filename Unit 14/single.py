#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      greg6750
#
# Created:     02/12/2018
# Copyright:   (c) greg6750 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import arcpy
import os
#import multiprocessing
import uuid
import time

arcpy.CheckOutExtension("3D")

def run_viewshed(in_fc):
    out_gdb = r'C:\Users\greg6750\Documents\IPython Notebooks\Advanced_Python_for_GIS_and_RS\Week 13\results.gdb'
    dem = r'C:\Users\greg6750\Downloads\USGS_NED_13_n48w122_ArcGrid\grdn48w122_13'
    out_fc = os.path.join(out_gdb, in_fc[-5:]+'_'+ uuid.uuid4().hex)
    print(out_fc)
    arcpy.Viewshed_3d(dem, in_fc, out_fc)

if __name__ == '__main__':

    t0 = time.clock()

    gdb = r'C:\Users\greg6750\Documents\IPython Notebooks\Advanced_Python_for_GIS_and_RS\Week 13\ViewLocations.gdb'
    arcpy.env.workspace = gdb

    view_locations = [os.path.join(gdb, fc) for fc in arcpy.ListFeatureClasses()]

    for view in view_locations:
        run_viewshed(view)


    t1 = (time.clock() - t0)/60
    print("This process took " + str(t1) + " minutes to run the entire process")
    #This process took 10.2682547693 minutes to run the entire process