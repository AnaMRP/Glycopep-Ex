""" Project work for Python course - HT2017"""
""" Script that takes up feature files from mass spectrometry raw data processed through PEAKS StudioTM and extracts those ions (rows) containing GlcNAc as"""
""" post-translational modification (+203.08), either in the DB sequence or the de novo sequence. For those, outpus simple plots to understand the data"""

import pandas as pd
import numpy as np
import matplotlib as plt
import matplotlib.pyplot as pltpy

from pandas import read_csv
data = read_csv('C:/Users/xrodan/Desktop/2017_Python/Project/test.txt', delimiter='\t')
print (data)
print (data.columns.values)
data = data.rename(columns={' Area_Intensity': 'Area_intensity'})
print (data.columns.values)
print (data.Area_intensity)

data['DB_seq'] = data['DB_seq'].astype('str')
data['de_novo_seq'] = data['de_novo_seq'].astype('str')
data['DB_seq'].fillna(0)
data['de_novo_seq'].fillna(0)
print (data)

data1 = data[data['de_novo_seq'].str.contains('203.08')]
data2 = data[data['DB_seq'].str.contains('203.08')]
print (data1)
print (data2)
filt_data = pd.merge(data1, data2, how='outer')
print (filt_data)
filt_data.to_csv('C:/Users/xrodan/Desktop/2017_Python/Project/filtered.csv')

pltpy.figure()
pltpy.hist([filt_data['m/z']], 
    bins = 100,
    range=(400,450))
pltpy.xlabel('m/z, Th')
pltpy.ylabel('# of ions')
pltpy.show()

pltpy.figure()
pltpy.hist([filt_data['z']],
    bins = 20,
    range=(0,10))
pltpy.xlabel('charge, e')
pltpy.ylabel('# of ions')
pltpy.show()