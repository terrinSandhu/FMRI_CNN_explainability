import nibabel as nib
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import glob
import os

import glob

def get_nii_files_glob(directory):
    # This will search for .nii files in the directory and all its subdirectories
    search_path = os.path.join(directory, '**', '*.nii')
    return glob.glob(search_path, recursive=True)

import os

def get_nii_files_os(directory):
    nii_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.nii'):
                nii_files.append(os.path.join(root, file))
    return nii_files

# Function to load and preprocess .nii data
def load_nii_data(file_path):
    # Load the .nii file
    nii_data = nib.load(file_path)
    # Get the data as a numpy array
    data_array = nii_data.get_fdata()
    # Preprocess the data (e.g., normalization, reshaping)
    # ... your preprocessing steps here ...
    return data_array

# Load your .nii files (replace with your file paths)
file_paths = get_nii_files_glob("scans35")
#print(file_paths)
data = [load_nii_data(path) for path in file_paths]

# Flatten the data if necessary
flattened_data = [d.reshape(-1) for d in data]

# Apply t-SNE
tsne = TSNE(n_components=3, random_state=0,perplexity=10,n_iter_without_progress=5)
tsne_results = tsne.fit_transform(flattened_data)

# Visualize the results
plt.scatter(tsne_results[:, 0], tsne_results[:, 1])
plt.xlabel('t-SNE feature 1')
plt.ylabel('t-SNE feature 2')
plt.title('t-SNE visualization of .nii data')
plt.show()
