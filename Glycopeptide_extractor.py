""" Script that takes up feature files from mass spectrometry raw data processed through PEAKS StudioTM and extracts those ions (rows) containing GlcNAc as"""
""" post-translational modification (+203.08), either in the DB sequence or the de novo sequence. For those, outpus simple plots to understand the data"""

import pandas as pd
import matplotlib.pyplot as plt

from pandas import read_csv
data = read_csv('C:/Users/xrodan/Desktop/2017_Python/Project/peptide_features_1.txt', delimiter='\t')
print (data)
print (data.columns.values)
data = data.rename(columns={' Area_Intensity': 'Area_intensity'})

data['DB_seq'] = data['DB_seq'].astype('str')
data['de_novo_seq'] = data['de_novo_seq'].astype('str')
data['DB_seq'].fillna(0)
data['de_novo_seq'].fillna(0)

data1 = data[data['de_novo_seq'].str.contains('203.08')]
data2 = data[data['DB_seq'].str.contains('203.08')]
filt_data = pd.merge(data1, data2, how='outer')
print (filt_data)
filt_data.to_csv('C:/Users/xrodan/Desktop/2017_Python/Project/filtered.csv')

plt.figure()
plt.hist([filt_data['m/z']], 
    bins = 25,
    range=(400,1600))
plt.xlabel('m/z, Th')
plt.ylabel('# of ions')
plt.show()

plt.figure()
plt.hist([filt_data['z']],
    bins = 10,
    range=(0,10))
plt.xlabel('charge, e')
plt.ylabel('# of ions')
plt.show()
