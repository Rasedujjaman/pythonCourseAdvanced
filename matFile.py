# This python script will load a mat file 

import scipy.io as sio
import matplotlib.pyplot as plt


# data = sio.loadmat('scan1.mat')
data = sio.loadmat('Scan20210902_3.mat')

print(type(data))


print(data.keys())
# print(data.values())

dd = data['scan_data']
print(type(dd))
print(type(dd.shape))
sz = dd.shape
for ii in range (0, 1):
    plt.figure()
    plt.imshow(dd[:,:,ii], cmap='gray')

plt.show()




