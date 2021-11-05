import os

os.system('gfortran flibrary.f90 map_henon.f90 -o drive.x')
os.system('./drive.x')
