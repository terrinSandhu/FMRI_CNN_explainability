import nibabel as nib
import numpy as np
import matplotlib.pyplot as plt

path = "C:/Users/tssan/OneDrive/Desktop/EngPsych/scans35/s008_anat.nii"

test_load = nib.load(path).get_fdata()
print(test_load.shape)


show = 100
test = test_load[:,:,1]

if show ==1:
    plt.imshow(test)
    plt.show()

for i in range(50,show,5):
    test = test_load[:,:,i]
    plt.imshow(test)
    plt.show()
