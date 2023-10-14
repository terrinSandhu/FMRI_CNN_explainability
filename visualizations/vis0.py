import numpy as np
import matplotlib.pyplot as plt
import nibabel as nib
import nipraxis

plt.rcParams['image.cmap'] = 'gray' # Set 'gray' as the default colormap
np.set_printoptions(precision=4, suppress=True) # Display array values to 4 digits of precision
path = "C:/Users/tssan/OneDrive/Desktop/EngPsych/scans35/s008_anat.nii"

structural_fname = nipraxis.fetch_file('ds114_sub009_highres.nii')

img = nib.load(structural_fname)
img

