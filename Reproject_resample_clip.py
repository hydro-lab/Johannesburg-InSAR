#!/bin/bash

import glob
from osgeo import gdal

ls = (glob.glob("/Volumes/hydro3-raid/Will_InSAR/hype/*/*_clip.tif"))

for fn in ls:
    split = fn.split(".")
    out = split[0]+"_rpclip.tif"
    shpin = "/Volumes/hydro3-raid/Will_InSAR/Will_InSAR_Study_Area/Johannesburg_Study_Area.shp"
    gdal.Warp(out,fn,srcSRS='EPSG:22293',dstSRS='EPSG:4326', xRes = 0.000766570302388142, yRes = -0.000766570302388142, cutlineDSName = shpin, cropToCutline = True)
