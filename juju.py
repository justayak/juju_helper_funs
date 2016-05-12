import matplotlib.pyplot as plt
import matplotlib.cm as cm
from PIL import Image
import numpy as np
from os import listdir
from os.path import isfile, join
import math
import cv2

def plot_mats(mats, cols=5, cmap=plt.get_cmap('gray'), size=16):
    """
    plot a set of matrices close to each other
    """
    SUBSTITUTE = np.zeros_like(mats[0])
    rows = []
    currentRow = []
    cols = float(cols)

    def add_to_rows():
        while len(currentRow) < cols:
            currentRow.append(SUBSTITUTE)
        rows.append(np.hstack(currentRow))
    
    for i in range(0, len(mats)):
        M = mats[i]
        minv = np.min(M)
        maxv = np.max(M)
        if minv < 0 or minv > 255 or maxv < 0 or maxv > 255:
            M = translate(M, minv, maxv, 0, 255)

        if i%cols == 0:
            if len(currentRow) > 0:
                add_to_rows()
            currentRow = []
        currentRow.append(M)
    if len(currentRow) > 0:
        add_to_rows()
    I = np.vstack(rows)
    f, ax = plt.subplots(ncols=1)
    f.set_size_inches(size, size)
    ax.imshow(I, cmap=cmap)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

def plot(I):
    f, ax = plt.subplots(ncols=1, nrows=1)
    f.set_size_inches(32, 16)
    ax.imshow(I)
    ax.axis('off')
    plt.tight_layout()
    plt.show()

def imread(List, folder_file, ext='jpg'):
    for i in range(1, 8):
        I = cv2.imread(folder_file + str(i) + '.' + ext)
        I = cv2.cvtColor(I, cv2.COLOR_BGR2RGB)
        List.append(I)
    return List
