#!/usr/bin/env python3
import os

# Initialize Constants
PPD_DIR = os.path.join(os.getcwd(), "ppds")
PCLM_ROOT_DIR = os.path.join(os.getcwd(), "pclm-files")
RASTER_ROOT_DIR = os.path.join(os.getcwd(), "raster-images")
CUPSFILTER = "cupsfilter"
PPDFLAG = "-P"
OUTMIMETYPE = "application/PCLm"
MEDIA = "-o media=A4"

# Convert all raster files in raster_dir to PCLm files in pclm_dir
def convert_raster(ppd_file, pclm_dir, raster_dir):
  for raster_file in os.listdir(raster_dir):
    raster_addr = os.path.join(raster_dir, raster_file)
    command = CUPSFILTER + " " +\
              PPDFLAG + " " +\
              ppd_file + " " +\
              raster_addr + " " +\
              "-m " + OUTMIMETYPE + " " +\
              MEDIA + " " +\
              "> " + os.path.join(pclm_dir, raster_file) + ".pclm"
    os.system(command)

# Generate PCLm files for each PPD using cupsfilter
for ppd in os.listdir(PPD_DIR):
  ppd_file = os.path.join(PPD_DIR, ppd)
  filename = os.path.splitext(ppd)[0]
  strip_height = filename.split("-")[0]
  dpi = filename.split("-")[1]
  compression_method = filename.split("-")[2]
  pclm_dir = os.path.join(PCLM_ROOT_DIR, strip_height, dpi, compression_method)
  raster_dir = os.path.join(RASTER_ROOT_DIR, dpi)
  if not os.path.exists(pclm_dir):
    os.makedirs(pclm_dir)
  convert_raster(ppd_file, pclm_dir, raster_dir)
