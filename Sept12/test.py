fileh = open('textdata.txt', 'r')
print(fileh.read())

import numpy as np

file = np.genfromtxt('en_climate_hourly_AB_3031094_09-2023_P1H.csv', delimiter=',', names=True,dtype='str')

print(file)