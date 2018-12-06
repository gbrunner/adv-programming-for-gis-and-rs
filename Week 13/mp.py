import arcpy
import os
import multiprocessing
import uuid
import time

arcpy.CheckOutExtension("3D")

def run_viewshed(processs_list):
    #arg = ProcessList.split(',')
    #in_fc = arg[0]
    in_fc = processs_list
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

    pool = multiprocessing.Pool()


    results = pool.map(run_viewshed, view_locations) #, maxtasksperchild=10)

    pool.close()
    pool.join()

    t1 = (time.clock() - t0)/60
    print("This process took " + str(t1) + " minutes to run the entire process")
    #Took 3.74 minutes to run this